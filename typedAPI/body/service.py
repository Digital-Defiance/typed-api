import typedAPI.endpoint.schema
import starlette.requests






def parse(
    endpoint_specification: typedAPI.endpoint.schema.EndpointSpecification,
    request: starlette.requests.Request
) -> dict | None:
    request.body
