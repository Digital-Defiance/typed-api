import typing

from typedAPI.http.response.schema import UnormalisedResponse, Status, Body, Headers
from types import EllipsisType




def is_ellipsis(value) -> typing.TypeGuard[EllipsisType]:
    return value == ...





def is_headers(value: typing.Any) -> typing.TypeGuard[Headers]:
    
    if not isinstance(value, dict):
        return False
    
    for key in value:
        if not isinstance(key, str):
            return False

    return True



def is_status(value: typing.Any) -> typing.TypeGuard[Status]:
    return isinstance(value, int)


def is_body(value: typing.Any) -> typing.TypeGuard[Body]:
    return isinstance(value, str) or isinstance(value, dict) or isinstance(value, bytes)



def is_response(values: typing.Any) -> typing.TypeGuard[UnormalisedResponse]:

    if is_status(values):
        return True

    if not isinstance(values, tuple):
        return False

    size = len(values)

    if size > 3 or size == 0:
        return False

    status = values[0]
    
    if not is_status(status):
        return False
    
    if size == 1:
        return True

    headers = values[1]

    if not is_headers(headers):
        return False

    if size == 2:
        return True
    
    body = values[3]
    
    if is_body(body):
        return True

    return False

