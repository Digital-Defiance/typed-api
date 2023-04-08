

import typing
import starlette.applications
import starlette.responses
import uvicorn

class Server(starlette.applications.Starlette):

    def listen(self, *args, **kwargs):
        uvicorn.run(self, *args, **kwargs)


    def _handler_wrapper_definition(self):
        pass

    @property
    def _http_endpoint_register(self) -> typing.Callable:
        def decorator(endpoint_executer: typing.Callable) -> typing.Callable:
            

            if endpoint_executer.__name__ not in ["get", "post", "delete", "head", "put"]:
                raise TypeError("Name of path executer must be an http method: `get`, `post`, etc...")

            endpoint_executer.__method__ = endpoint_executer.__name__.upper()

            annotations = typing.get_type_hints(endpoint_executer)

            resource_path = annotations.get('resource_path', None)
            
            if resource_path is None:
                raise TypeError("Must specify resource_path.")
            
            header_lines = annotations.get('headers', None)

            async def wrapper(request):

                # parse and validate request
                
                validated_resource_path = resource_path.validate(request.path_params, request.query_params)
                
                path_executer_args = {
                    "resource_path": validated_resource_path
                }

                if header_lines is not None:
                    headers_are_valid, data = header_lines.validate(request.headers)

                    if not headers_are_valid:
                        return starlette.responses.JSONResponse({"detail": f"Invalid header `{data}`"}, status_code=422)

                    path_executer_args["headers"] = data

                status, headers, body = await endpoint_executer(**path_executer_args)
                
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
            
            self.add_route(str(resource_path), wrapper, methods=[endpoint_executer.__name__.upper()])
            return wrapper
        return decorator


    def append(self, protocol='http'):
        if protocol == 'http':
            return self._http_endpoint_register

        raise NotImplementedError(f'Unknown protocol: {protocol}')


