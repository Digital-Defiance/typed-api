
import typing

import typing
import typedAPI.http.endpoint.schema

http_methods = typing.get_args(typedAPI.http.endpoint.schema.HttpMethods)

def is_http_method(name: typing.Any) -> typing.TypeGuard[typedAPI.http.endpoint.schema.HttpMethods]:
    return name in http_methods
