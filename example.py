# type: ignore

import typedAPI

server = typedAPI.Server()

v1 = typedAPI.ResourcePath("/api/v1")


@server.append(protocol='http')
async def get(
    resource_path: v1 / "test-typed-api" / "{some_id:int}",
    headers: typedAPI.Headers({
        'host': lambda host: host == 'localhost:8000',
        'accept': lambda accept: 'ext/html' in accept
    })
):

    return 200, {
        "content-type": "application/json"
    }, {
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
