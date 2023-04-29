import starlette.responses
from typedAPI.response.data import http_status_codes

from typedAPI.response.schema import Status, Body, Headers



def guess_body(status: Status, headers: Headers) -> Body:
    content_type = headers.get("content-type", "application/json")
    
    message = http_status_codes[status]

    if content_type == "application/json":
        return { "detail": message }
    if content_type == "text/plain":
        return message
    if content_type == "application/xml":
        return "<detail>" + message + "</detail>"
    if content_type == "text/html":
        return "<html><body><p>" + message + "</p></body></html>"

    return { "error": f"Unsupported content type: `{content_type}`" }




def make_response(status: Status, headers: Headers, body: Body) -> starlette.responses.Response:  # type: ignore
    starlette_response = starlette.responses.Response(
        body,
        status_code = status,
        headers = headers # type: ignore
    )

def guess_headers(status: Status, body: Body) -> Headers: # type: ignore
    pass
