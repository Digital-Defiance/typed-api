# Typed-API

A lightweight Python backend framework that leverages Python's type hinting to concisely define an API. Heavily inspired by FastAPI.

## Goal

To create a simple and intuitive way to build APIs using Python's type hinting feature.

```Python
# typed_api_example.py

# type: ignore

import typedAPI

listener = typedAPI.Server()
base = typedAPI.Endpoint("/api/v1")

MOCK_DB = {
    "id": [1, 2, 3],
    "title": ["title1", "title2", "title3"],
    "content": ["Aas fadsfads f", "asdfasfdf", "dfasdfsdaf"]
}

@listener.append
async def get(endpoint: base / "posts"):
    db_values = MOCK_DB.values()
    db_entries = zip(*db_values)

    return 200, {
        "content-type": "application/json"
    }, {
        "status": "OK",
        "endpoint": endpoint.path,
        "data": [
            {
                "id": id,
                "title": title,
                "content": content
            } for id, title, content in db_entries
        ]
    }

if __name__ == "__main__":
    listener.serve(host='127.0.0.1', port=8000)
    
```

**Note**: Despite the name "TypedAPI", # type: ignore is required until static analysis tools can be adapted to this usage of type annotations.


    
# Usage

1. Import the typedAPI module.
2. Create an instance of the Server class.
3. Define your API endpoints using the Endpoint class.
4. Use the @listener.append decorator to add your route handlers.
5. Run the server using the listener.serve() method.
6. Refer to the example code above for a basic example of how to use TypedAPI.
    


# License

This project is licensed under the MIT License