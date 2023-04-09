# Typed-API

A lightweight Python backend framework that leverages Python's type hinting to concisely define an API. Heavily inspired by FastAPI.

## Goal

To create a simple and intuitive way to build APIs using Python's type hinting feature.

```Python
# type: ignore

import typedAPI

server = typedAPI.Server({
    'profile': 'http-openapi',
    'defaults.request.headers': {
        'host': lambda host: host if host == 'localhost:8000' else 503,
        'accept': lambda accept: accept if 'text/html' in accept else 503,
    }
})

v1 = typedAPI.ResourcePath("/api/v1")

@unprotected_router.append(protocol='http')
async def get(
    resource_path: v1 / "test-typed-api",
    headers: typedAPI.Headers({
        ...: str | None
        'Authorisation': ...,
    }),
):
    return 302, { 'location': '/docs' }


@server.append(protocol='http')
async def get(
    resource_path: v1 / "test-typed-api" / "{some_id:int}",
    headers: typedAPI.Headers({
        'host': lambda host: host if host == 'localhost:8000' else 503,
        'accept': lambda accept: accept if 'text/html' in accept else 503,
    }),
):

    if not headers["Authorisation"].role == "ADMIN":
        return 401

    return ..., {
        "status": "OK",
        "resource_path": {
            "value": str(resource_path),
            "parameters": resource_path.parameters.dict(),
            "queries": resource_path.queries.dict()
        },
        "headers": headers,
    }

if __name__ == "__main__":
    server.listen(host='127.0.0.1', port=8000)


```

# License

This project is licensed under the MIT License