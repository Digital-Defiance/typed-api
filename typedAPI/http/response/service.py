from typedAPI.http import resource_path
from typedAPI.http.response.schema import  NormalisedResponse
from typedAPI.http.response.guards import   is_headers, is_body, is_response
from typedAPI.http.response.factory import guess_body, guess_headers, make_response
import starlette.responses
import typedAPI.http.headers.service
import typedAPI.http.resource_path.service

def to_typedapi_response(request, endpoint_specification, endpoint_executer) -> NormalisedResponse:

    resource_path = typedAPI.http.resource_path.service.parse(endpoint_specification, request)

    headers = typedAPI.http.headers.service.parse(endpoint_specification, request)

    for value in headers.values():
        if is_response(value):
            return to_normalised_response(value)
    
    body = ...
    # body_values = typedAPI.http.body.service.parse(request)

    response = endpoint_executer(resource_path, headers, body)

    return to_normalised_response(value)


def to_starlette_response(normalised_response: NormalisedResponse) -> starlette.responses.Response:

    status = normalised_response.status
    headers = normalised_response.header_lines
    body = normalised_response.body

    if status == ...:
        status = 200

    # status, ..., ....
    if headers == ... and body == ...:
        headers = {'content-type': 'application/json' }
        return make_response(status, headers, None)
    
    # status, headers, ...
    if is_headers(headers) and body == ...:
        body = guess_body(status, headers)
        return make_response(status, headers, body)

    # status, ..., body
    if headers == ... and is_body(...):
        headers = guess_headers(status, body)
        return make_response(status, headers, body) 
    
    # status, headers, body
    return make_response(status, headers, body)

    