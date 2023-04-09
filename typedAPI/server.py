

import typing
import starlette.applications
import starlette.responses
import uvicorn
import typedAPI



http_status_codes = {
    100: "Continue",
    101: "Switching Protocols",
    102: "Processing",
    103: "Early Hints",
    200: "OK",
    201: "Created",
    202: "Accepted",
    203: "Non-Authoritative Information",
    204: "No Content",
    205: "Reset Content",
    206: "Partial Content",
    207: "Multi-Status",
    208: "Already Reported",
    226: "IM Used",
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Found",
    303: "See Other",
    304: "Not Modified",
    305: "Use Proxy",
    307: "Temporary Redirect",
    308: "Permanent Redirect",
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Timeout",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Payload Too Large",
    414: "URI Too Long",
    415: "Unsupported Media Type",
    416: "Range Not Satisfiable",
    417: "Expectation Failed",
    418: "I'm a teapot",
    421: "Misdirected Request",
    422: "Unprocessable Entity",
    423: "Locked",
    424: "Failed Dependency",
    425: "Too Early",
    426: "Upgrade Required",
    428: "Precondition Required",
    429: "Too Many Requests",
    431: "Request Header Fields Too Large",
    451: "Unavailable For Legal Reasons",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    505: "HTTP Version Not Supported",
    506: "Variant Also Negotiates",
    507: "Insufficient Storage",
    508: "Loop Detected",
    510: "Not Extended",
    511: "Network Authentication Required"
}



class Server(starlette.applications.Starlette):
    
    
    def __init__(self, *args, **kwargs):
        super().__init__()

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
                    headers_are_valid, data_or_response = header_lines.validate(request.headers)
                    path_executer_args["headers"] = data_or_response
                else:
                    headers_are_valid = True
                    data_or_response = None
                    
                print(data_or_response)

                if headers_are_valid:
                    response = await endpoint_executer(**path_executer_args)
                    
                    ok, data = typedAPI.response.normalise_response(response)

                    if data is None:
                        raise TypeError('Innapropriate response.')
                else:
                    if data_or_response is not None:
                        data = data_or_response 
                    else:
                        raise RuntimeError
            

                status, headers, body = data


                if status == ...:
                    status = 200

                if (is_ellipsis := headers == ...) or headers.get("content-type", None) is None:

                    if is_ellipsis:
                        headers = {}

                        if body == ...:
                            body = http_status_codes[status]

                    if isinstance(body, dict):
                        headers['content-type'] =  'application/json'
                        startlette_response = starlette.responses.JSONResponse(
                            body, status_code = status, headers = headers,
                        )

                    elif isinstance(body, str):
                        headers['content-type'] =  'text/plain'
                        startlette_response = starlette.responses.Response(
                            body, status_code = status, headers = headers,
                        )
                    else:
                        raise NotImplementedError()

                else:
                    content_type = headers.get("content-type")
                    
                    if content_type == 'application/json':
                        startlette_response = starlette.responses.JSONResponse(
                            body, status_code = status, headers = headers,
                        )

                    elif content_type == 'text/plain':
                        startlette_response = starlette.responses.Response(
                            str(body), status_code = status, headers = headers,
                        )
                        
                    else:
                        startlette_response = starlette.responses.Response(
                            body, status_code = status, headers = headers,
                        )
                
                return startlette_response

            wrapper.__annotations__ = annotations
            
            self.add_route(str(resource_path), wrapper, methods=[endpoint_executer.__name__.upper()])
            return wrapper
        return decorator


    def append(self, protocol='http'):
        if protocol == 'http':
            return self._http_endpoint_register

        raise NotImplementedError(f'Unknown protocol: {protocol}')


