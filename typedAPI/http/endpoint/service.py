import typing

import starlette
from typedAPI.http.endpoint.schema import EndpointSpecification

import functools
import starlette.requests

import typedAPI.http.headers.service
import typedAPI.http.headers.service
import typedAPI.http.response.service
import typedAPI.http.response.schema

def make_response(request, endpoint_specification, endpoint_executer) -> typedAPI.http.response.schema.NormalisedResponse:
    resource_path_value = typedAPI.http.headers.service.parse(request)
    header_lines_values = typedAPI.http.headers.service.parse(request)
    body_values = ...
    # body_values = typedAPI.http.body.service.parse(request)

    response = endpoint_executer(resource_path_value, header_lines_values, body_values)

    return response


def generate_full_executor(endpoint_executer: typing.Callable) -> typing.Tuple[typing.Callable, EndpointSpecification]:

    endpoint_specification = EndpointSpecification(endpoint_executer)

    @functools.wraps(endpoint_executer)
    async def full_executor(request: starlette.requests.Request):
        response = make_response(request, endpoint_specification, endpoint_executer)
        starlette_response = typedAPI.http.response.service.to_starlette_response(response)
        return starlette_response

    return full_executor, endpoint_specification








