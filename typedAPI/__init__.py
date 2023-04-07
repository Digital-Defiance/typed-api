# type: ignore

import re
import typing
import starlette.applications
import starlette.responses
import uvicorn

class Endpoint:
    path: str
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

        self.path = path
        self.params = params



class Server(starlette.applications.Starlette):
    

    def serve(self, *args, **kwargs):
        uvicorn.run(self, *args, **kwargs)


    @staticmethod
    def _handle_endpoint_definition(annotations):
        endpoint_annotation: Endpoint = annotations.get('endpoint', None)

        if endpoint_annotation is None:
            raise TypeError("Method requires endpoint definition.")

        if not isinstance(endpoint_annotation, Endpoint):
            raise TypeError("Annotation of `endpoint` must be an `Endpoint` instance.")

        annotations["endpoint"] = typing.TypedDict("EndpointDefinition", endpoint_annotation.params)

        return endpoint_annotation


    @staticmethod
    def _handle_header_definition(annotations):

        header_annotation: Endpoint = annotations.get('headers', None)

        if header_annotation is None:
            return

        return header_annotation.headers
        

    @staticmethod
    def _handle_body_definition(annotations):

        body_annotation: Endpoint = annotations.get('body', None)

        if body_annotation is None:
            return

        print("body:", body_annotation)
        return body_annotation

    def _handler_wrapper_definition(self):
        pass

    def _method(self, method: str, *args, **kwargs):
        def decorator(route_executer: typing.Callable):
            annotations = typing.get_type_hints(route_executer)

            endpoint = self._handle_endpoint_definition(annotations)
            headers = self._handle_header_definition(annotations)
            body = self._handle_body_definition(annotations)
            
            path_executer_args = {
                "endpoint": endpoint
            }
            
            if headers is not None:
                path_executer_args["headers"] = headers

            if body is not None:
                path_executer_args["body"] = body


            async def wrapper(request):
                
                # parse and validate request

                status, headers, body = await route_executer(**path_executer_args)
                
                if headers.get("content-type", None).startswith("application/json"):
                    response_class = starlette.responses.JSONResponse
                else:
                    response_class = starlette.responses.Response


                return response_class(
                    body,
                    status_code = status,
                    headers = headers,
                )


            wrapper.__annotations__ = annotations
            
            path = path_executer_args["endpoint"].path
            self.add_route(path, wrapper, methods=[method])
            return wrapper
        return decorator


    def __getattr__(self, name: str):
        if name not in ["get", "post", "delete", "head", "put"]:
            super().__getattr__(name)

        def method(*args, **kwargs):
            return self._method(name, *args, **kwargs)

        return method

class Headers:
    def __init__(self, headers):
        self.headers = headers


