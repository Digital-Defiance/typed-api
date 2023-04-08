# type: ignore

import re
import typing
import starlette.applications
import starlette.responses
import uvicorn

import pathlib

class Endpoint(pathlib.PosixPath):
    
    
    type_dict = {
        'int': int,
        'str': str
    }
    

    @property
    def path(self):
        return str(self)
    
    @property
    def params(self):
        parameters = {}

        for name in self.parts:
            if ":" in name:
                params = name.split(":")
                if not len(params) == 2:
                    raise ValueError("Invalid parameter specification.")

                param_name = params[0].strip()
                param_type = self.type_dict[params[1].strip()]
                parameters[param_name] = param_type
                
        return parameters


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


    @property
    def append(self, *args, **kwargs):
        
        def decorator(route_executer: typing.Callable) -> typing.Callable:

            if route_executer.__name__ not in ["get", "post", "delete", "head", "put"]:
                raise TypeError("Name of path executer must be an http method: `get`, `post`, etc...")

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
            
            self.add_route(path, wrapper, methods=[route_executer.__name__.upper()])
            return wrapper
        return decorator


class Headers:
    def __init__(self, headers):
        self.headers = headers


