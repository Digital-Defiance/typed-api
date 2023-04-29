import starlette.requests
import typedAPI.endpoint.schema


def parse(
    endpoint_specification: typedAPI.endpoint.schema.EndpointSpecification,
    request: starlette.requests.Request
) -> dict | None:
    
    import typing

    headers = endpoint_specification.header_lines

    annotations = typing.get_type_hints(endpoint_specification.executor)
    
    print(annotations)
    headers_dict = {}
    
    if headers is None:
        return None

    for header_name, header_processor in headers.items():
        header_value = request.headers.get(header_name, None)
        processed_header_value = header_processor(header_value)
        headers_dict[header_name] = processed_header_value

    return headers_dict


    


