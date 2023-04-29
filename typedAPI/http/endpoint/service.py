import typing

import starlette
from typedAPI.http.endpoint.schema import EndpointSpecification

import functools
import starlette.requests

import typedAPI.http.headers.service
import typedAPI.http.headers.service
import typedAPI.http.response.service
import typedAPI.http.response.schema



def generate_full_executor(endpoint_executer: typing.Callable) -> typing.Tuple[typing.Callable, EndpointSpecification]:

    endpoint_specification = EndpointSpecification(endpoint_executer)

    @functools.wraps(endpoint_executer)
    async def full_executor(request: starlette.requests.Request):
        typedapi_response = typedAPI.http.response.service.to_typedapi_response(request, endpoint_specification, endpoint_executer)
        starlette_response = typedAPI.http.response.service.to_starlette_response(typedapi_response)
        return starlette_response

    return full_executor, endpoint_specification








