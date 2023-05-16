
import typing
import pydantic
import typedAPI.resource_path.schema
import typedAPI.headers.schema

import typedAPI.body.schema


HttpMethods = typing.Literal["GET", "POST", "PATCH", "PUT", "DELETE", "OPTIONS", "HEAD"]


class EndpointSpecification(pydantic.BaseModel):
    http_method: HttpMethods
    resource_path: typedAPI.resource_path.schema.ResourcePath
    header_lines: typedAPI.headers.schema.Headers | None
    body: typedAPI.body.schema.MultiPartFormData | typing.Callable | typing.Literal[str] | typing.Literal[int] | typing.Literal[dict] | typing.Literal[bytes] | None
    executor: typing.Callable


    def __init__(self, endpoint_executer: typing.Any):

        
        if not callable(endpoint_executer):
            raise ValueError("Must be callable.")

        annotations = typing.get_type_hints(endpoint_executer)
        body = annotations.get('body', None)
        print(body)
        super().__init__(
            executor=endpoint_executer,
            http_method=endpoint_executer.__name__.upper(), #type:ignore
            resource_path=annotations.get('resource_path', None), #type:ignore
            header_lines=annotations.get('headers', None), #type:ignore
            body = body # type: ignore
        )

    
