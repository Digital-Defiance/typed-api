# TypedAPI

This is a Python library that makes it easier to build a typed API. The library makes use of Starlette for ASGI application framework and Pydantic for data validation and settings management using Python type annotations.

The library is built around the `TypedAPI` class which provides HTTP method handlers (GET, POST, HEAD, DELETE, PUT, PATCH, OPTIONS, TRACE, CONNECT) to define endpoints and the parameters they receive. 

## Features

- Generation of Pydantic models from dictionaries, helping in dynamic data modeling.
- Content-type validation in requests.
- Parsing and validation of request body depending on the specified type such as JSON or form data.
- Utilizes Python type annotations for defining the structure of HTTP requests and responses.
- It provides a `ResourcePath` class to construct API paths.

## Prerequisites

The project requires the following packages:

- [Starlette](https://www.starlette.io/): for the web application.
- [Pydantic](https://pydantic-docs.helpmanual.io/): for data validation and settings management.
- [uvicorn](https://www.uvicorn.org/): an ASGI server to run the application.

## Example Usage

```python
if __name__ == "__main__":
    app = TypedAPI()
    v1 = ResourcePath("/api/v1")

    @app.http
    def get(
        resource_path: v1 / "a",
        headers: {
            'host': str
        },
        body: ...
    ):
        print("???", headers)
        return 200, ..., { "test": 123 }


    @app.http
    def post(
        resource_path: v1 / "a",
        headers: {
            'host': str
        },
        body: [
            ('test1', int),
            ('test2', str)
        ]
    ):
        print("???", headers)
        print("body??????", body)
        return 200, ..., { "test": 123 }

    import uvicorn
    uvicorn.run(app.app, host="0.0.0.0", port=8000)
```

This will start a server and setup two endpoints, `GET /api/v1/a` and `POST /api/v1/a`. The headers and bodies for these requests are validated as per the parameters of the respective handler functions. If the validation passes, the handlers are executed. 

## How to Install

1. Clone this repository.
2. Make sure you have Python 3.6+ installed. Install dependencies by running `pip install -r requirements.txt`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
