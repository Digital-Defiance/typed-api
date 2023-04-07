# type: ignore

import typedAPI

listener = typedAPI.Server()

@listener.get()
async def this_is_an_example_endpoint(
    endpoint: typedAPI.Endpoint("/"),
    headers: typedAPI.Headers({
        "X-Auth-Header": str,
        "asdasd": int
    }),
):

    return 200, {
        "Set-Cookie": "asdasdsada",
        "content-type": "application/json"
    }, {
        "status": "OK",
        "endpoint": endpoint.path,
        "data": {
            "title": "This is a test.",
            "message": "Typed API is a framework inspired on fastapi. It uses types to define data validation and much more.",
        }
    }

if __name__ == "__main__":
    listener.serve(host='127.0.0.1', port=8000)