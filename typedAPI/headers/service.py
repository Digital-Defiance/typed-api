import starlette.requests
from typedAPI.headers.schema import Headers


def parse(headers: Headers, request: starlette.requests.Request):
    
    headers_dict = {}

    for header_name, header_processor in headers.items():
        header_value = request.headers.get(header_name, None)
        processed_header_value = header_processor(header_value)
        headers_dict[header_name] = processed_header_value

    return headers_dict
        

    


