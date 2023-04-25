import starlette.responses
from typedAPI.http.response.data import http_status_codes


def make_response_from_status(status: int, content_type = "application/json") -> starlette.responses.Response:
    
    message = http_status_codes[status]

    if content_type == "application/json":
        body = { "detail": message }
    elif content_type == "text/plain":
        body = message
    elif content_type == "application/xml":
        body = "<detail>" + message + "</detail>"
    elif content_type == "text/html":
        body = "<html><body><p>" + message + "</p></body></html>"
    else:
        body = { "error": "Unsupported content type: " + content_type }
    
    return starlette.responses.Response(body, status_code=status, media_type=content_type)



def make_complete_headers_response(status, body_as_byes, content_type) -> starlette.responses.Response:
    return starlette.responses.Response(
        body_as_byes,
        status_code = status,
        headers = { "content-type": content_type }
    )


def make_response_from_complete_spec(status, headers, body) -> starlette.responses.Response:
    return starlette.responses.Response(
        body,
        status_code = status,
        headers = headers
    )

