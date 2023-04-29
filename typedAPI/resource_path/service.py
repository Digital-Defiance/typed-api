

import starlette.requests
import typedAPI.endpoint.schema


def parse(
    endpoint_specification: typedAPI.endpoint.schema.EndpointSpecification,
    request: starlette.requests.Request
) -> str:
    """ Generate an object that is usable by the user """

    

    for part in endpoint_specification.resource_path:
        pass

    return ""
