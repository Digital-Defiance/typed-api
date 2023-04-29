
import typing
import pydantic
import typedAPI.resource_path.schema
import typedAPI.headers.schema



HttpMethods = typing.Literal["GET", "POST", "PATCH", "PUT", "DELETE", "OPTIONS", "HEAD"]


class EndpointSpecification(pydantic.BaseModel):
    http_method: HttpMethods
    resource_path: typedAPI.resource_path.schema.ResourcePath
    header_lines: typedAPI.headers.schema.Headers
    executor: typing.Callable


    def __init__(self, endpoint_executer: typing.Any):
        
        if not isinstance(endpoint_executer, typing.Callable):
            raise ValueError("Must be callable.")
        

        annotations = typing.get_type_hints(endpoint_executer)

        super().__init__(
            http_method=endpoint_executer.__name__.upper(), #type:ignore
            resource_path=annotations.get('resource_path', None), #type:ignore
            header_lines=annotations.get('headers', None), #type:ignore
        )

    
