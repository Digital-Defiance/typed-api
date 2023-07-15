from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import Response, JSONResponse
from starlette.requests import Request
from pydantic import ValidationError

from typing import Any, Callable, Type, Dict, Union
import inspect
from pydantic import create_model, BaseModel
from typing import Any
import json






status_to_message = {
    100: "Continue",
    101: "Switching Protocols",
    200: "OK",
    201: "Created",
    202: "Accepted",
    204: "No Content",
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Found",
    304: "Not Modified",
    307: "Temporary Redirect",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    408: "Request Timeout",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout"
}


class ResourcePath:
    def __init__(self, path: str):
        self.path = path

    def __truediv__(self, other):
        return ResourcePath(self.path + '/' + other)

class TypedAPI:
    def __init__(self):
        self.app = Starlette()
        self.routes = []

    def http(self, func: Callable[..., Any]) -> Callable[..., Any]:

        # EXTRACTING INFO FROM DEFINITION
        method_name = func.__name__.upper()
        assert method_name in ["GET", "POST", "HEAD", "DELETE", "PUT", "PATCH", "OPTIONS", "TRACE", "CONNECT"]
        signature = inspect.signature(func)
        params = signature.parameters

        # RESOURCE PATH VALIDATOR
        assert 'resource_path' in params
        resource_path = params['resource_path'].annotation
        assert isinstance(resource_path, ResourcePath)
        path = resource_path.path

        # HEADERS VALIDATOR
        assert "headers" in params
        headers_spec = params['headers'].annotation
        if headers_spec == ...:
            headers_spec = {}
        formatted_dict = {k: (v, ...) for k, v in headers_spec.items()}
        headers_model = create_model('Headers', **formatted_dict)

        # BODY VALIDATOR
        assert "body" in params
        body = params['body'].annotation
        if body == ...:
            body = None

        async def starlette_handler(request: Request):

            request_headers = dict(request.headers)
            
            try:
                request_headers_obj = headers_model(**request_headers)
            except ValidationError as exception:
                return JSONResponse( exception.errors())

            if body == bytes or body == ...:
                request_body = await request.body()
            elif body == dict:
                try:
                    request_body = await request.json()
                except json.decoder.JSONDecodeError:
                    return JSONResponse({"error": "Body not valid json."})
            else:
                raise NotImplementedError("Not implemented")

            status_code, response_headers, response_body = func(path, request_headers, request_body)
            
            if status_code == ...:
                status_code = 200

            if response_headers == ...:
                response_headers = None

            if response_body == ...:
                print(status_code)
                response_body = str(status_code) + " " + status_to_message[status_code]
                ResponseType = Response
                
            if isinstance(response_body, dict):
                ResponseType = JSONResponse
                
            response = ResponseType(response_body, status_code=status_code, headers=response_headers)
            print(response.headers)
            return response

        route = Route(path, starlette_handler, methods=[method_name])
        self.routes.append(route)
        self.app.routes.append(route)
        return starlette_handler


app = TypedAPI()
v1 = ResourcePath("/api/v1")

@app.http
def get(
    resource_path: v1 / "a",
    headers: ...,
    body: dict
):
    print("???", headers)
    return 200, ..., { "test": 123 }


# Run the server using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app.app, host="0.0.0.0", port=8000)
