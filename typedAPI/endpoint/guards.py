

import typing
import typedAPI.http.endpoint.schema
import typedAPI.http.endpoint.data


def is_http_method(name: typing.Any) -> typing.TypeGuard[typedAPI.http.endpoint.schema.HttpMethods]:
    return name in typedAPI.http.endpoint.data.http_methods