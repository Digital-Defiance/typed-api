
import typing


EllipsisType = type(...)

Status = int

Headers = dict

Body = str | dict | bytes

Response = Status | typing.Tuple[Status, Headers] | typing.Tuple[Status, Headers, Body]

NormalisedResponse = typing.Tuple[Status, Headers | EllipsisType | None, Body | EllipsisType | None]


