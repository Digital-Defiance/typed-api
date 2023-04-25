

from typedAPI.http.response.schema import Response, Status, Body, Headers, NormalisedResponse
from typedAPI.http.response.factory import make_response_from_status, make_complete_headers_response, make_response_from_complete_spec
from typedAPI.http.response.processors import guess_content_type_from_body, cast_from_content_type
import typing
import starlette.responses


def is_response(values: typing.Any) -> typing.TypeGuard[Response]:
    
    if isinstance(values, Status):
        return True
    
    if not isinstance(values, tuple):
        return False
    
    size = len(values)

    if size > 3 or size == 0:
        return False

    status = values[0]
    
    if not isinstance(status, Status):
        return False
    
    if size == 1:
        return True
    
    headers = values[1]
    
    if not isinstance(headers, Headers):
        return False

    if size == 2:
        return True
    
    body = values[3]
    
    if not isinstance(body, Body):
        return False

    return True



def normalise_response(response: Response) -> NormalisedResponse:
    
    if isinstance(response, int):
        return response, ..., ...
    
    size = len(response)
    
    if size == 2:
        return response[0], response[1], ...
    
    return response[0], response[1], response[2] # type: ignore



def to_starlette_response(normalised_response: NormalisedResponse) -> starlette.responses.Response:
    status, headers, body = normalised_response
    
    complete_headers = headers == ...
    complete_body = body == ...

    if complete_headers:
        if complete_body:
            return make_response_from_status(status)

        content_type = guess_content_type_from_body(body)
        body_as_byes = cast_from_content_type(body, content_type)
        return make_complete_headers_response(status, body_as_byes, content_type)
    

    if complete_body:
        
        content_type = headers.get("content-type", None) # type: ignore

        if content_type == None:
            return make_response_from_status(status, content_type=content_type, headers=headers)

        return make_response_from_status(status, content_type=content_type)

    return make_response_from_complete_spec(status, headers, body)

