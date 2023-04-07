# type: ignore

import re
import typing

class Endpoint:
    params: dict["str", type]
    param_pattern: str = r"\[(\w+):\s*(\w+)\]"
    type_dict = {
        'str': str,
        'int': int
    }

    def __init__(self, path: str):
    
        params = {}

        for param_match in re.findall(self.param_pattern, path):
            param_name = param_match[0]
            param_type = param_match[1]

            param_type = self.type_dict.get(param_type, object)

            params[param_name] = param_type

        self.paht = path
        self.params = params



class Router:

    endpoint_definitions: dict
    
    def __init__(self):
        self.endpoint_definitions = {}
    

    @staticmethod
    def _handle_endpoint_definition(annotations, ):
        endpoint_annotation: Endpoint = annotations.get('endpoint', None)
        
        if endpoint_annotation is None:
            raise TypeError("Method requires endpoint definition.")

        if not isinstance(endpoint_annotation, Endpoint):
            raise TypeError("Wrong type")

        annotations["endpoint"] = typing.TypedDict("EndpointDefinition", endpoint_annotation.params)

        print("params: ", endpoint_annotation.params)


    @staticmethod
    def _handle_header_definition(annotations):

        header_annotation: Endpoint = annotations.get('headers', None)

        if header_annotation is None:
            return
        
        print("headers: ", header_annotation.headers)
        

    @staticmethod
    def _handle_body_definition(annotations):

        body_annotation: Endpoint = annotations.get('body', None)

        if body_annotation is None:
            return

        print("body:", body_annotation)


    def _method(self, method: str, *args, **kwargs):
        def decorator(route_executer: typing.Callable):
            annotations = typing.get_type_hints(route_executer)
            
            self._handle_endpoint_definition(annotations)
            self._handle_header_definition(annotations)
            self._handle_body_definition(annotations)



            def wrapper(*_args, **_kwargs):
                return route_executer(*_args, **_kwargs)

            wrapper.__annotations__ = annotations

            wrapper.__endpoint__ = {
                "method": method
            }

            self.endpoint_definitions["path"] = wrapper

            return wrapper
        return decorator

    def post(self, *args, **kwargs):
        return self._method('POST', *args, **kwargs)


class Headers:
    def __init__(self, headers):
        self.headers = headers



# example        

router = Router()

@router.post()
def as_admin_create_a_user(
    endpoint: Endpoint("/abc/[param: str]/[param2: int]?[param3: int][param4: str]"),
    headers: Headers({
        "X-Auth-Header": str,
        "asdasd": int
    }),
    body: int
):
    
    if headers["asdasd"] == 2:
        print("user is admin")
    
    if endpoint.param == "":
        pass

    return 200, {
        "Set-Cookie": "asdasdsada",
        "content-type": "application/json"
    }, {
        "status": "OK",
        "date": "asdsadsdafads7689adsf",
        "body": body,
    }


   
