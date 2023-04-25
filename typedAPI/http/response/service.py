

from typedAPI.http.response.schema import Response, Status, Body, Headers, NormalisedResponse
from typedAPI.http.response.factory import make_empty_reponse


import typing

import starlette.responses


def is_response(values: typing.Any) -> typing.TypeGuard[Response]:
    
    if isinstance(values, Status):
        return True
    
    if not isinstance(values, tuple):
        return False
    
    size = len(values)

    if size > 3:
        return False
    
    if size == 0:
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

    return response # type: ignore


def to_starlette_response(normalised_response: NormalisedResponse) -> starlette.responses.Response:
    status, headers, body = normalised_response

    if headers == None and body is None:
        return make_empty_reponse(status)
    
    complete_headers = headers == ...

    complete_body = body == ...
    
    

    

    
