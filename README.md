# typed-api
A small, python backend framework that leverages Pythons type hinting to concisely define an api.

I'm drawing tons of inspiration from fastapi. 

What I'm aiming for:

```Python

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
  
```

Despite the name "typedAPI", `# type: ignore` is obligatory until I get around to adapting static analysis tools to this usage of type annotations.