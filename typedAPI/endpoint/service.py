import typing

import starlette
from typedAPI.endpoint.schema import EndpointSpecification

import functools
import starlette.requests

import typedAPI.headers.service
import typedAPI.headers.service
import typedAPI.response.service
import typedAPI.response.schema



def generate_full_executor(endpoint_executer: typing.Callable) -> typing.Tuple[typing.Callable, EndpointSpecification]:

    endpoint_specification = EndpointSpecification(endpoint_executer)

    @functools.wraps(endpoint_executer)
    async def full_executor(request: starlette.requests.Request):
        typedapi_response = typedAPI.response.service.to_typedapi_response(request, endpoint_specification, endpoint_executer)
        starlette_response = typedAPI.response.service.to_starlette_response(typedapi_response)
        return starlette_response

    return full_executor, endpoint_specification








