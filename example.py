# type: ignore

import typedAPI

server = typedAPI.Server()

v1 = typedAPI.ResourcePath("/api/v1")



# This is the simplest form

@server.append(protocol='http')
async def get(resource_path: v1 / "examples" / "hello-world"):
    return 200


# the complete way to define a response is like so

@server.append(protocol='http')
async def get(resource_path: v1 / "examples" / "hello-world" / "complete-response"):
    return 200, {'content-type': "text/plain"}, "hello world !"


# but you can ommit elements from the right, in this case no body is sent

@server.append(protocol='http')
async def get(resource_path: v1 / "examples" / "hello-world" / "ommited-body"):
    return 200, {'content-type': "text/plain"}

# you can also ommit other elements by using `...`. typedAPI will go ahead
# and replace them by looking at the context, a string in the body implies `text/plain` and a `200` code

@server.append(protocol='http')
async def get(resource_path: v1 / "examples" / "hello-world" / "with-ellipsies"):
    return ..., ..., "hello world !"

# if you place a dictionary in the body, typedAPI will assume application/json

@server.append(protocol='http')
async def get(resource_path: v1 / "examples" / "hello-world" / "with-ellipsies"):
    return ..., ..., { "data": "hello world !"}

# resource path gives you access to queries as a pydantic model

@server.append(protocol='http')
async def get(resource_path: v1 / "examples" / "hello-world" / "with-ellipsies"):
    return 200, ..., { "queries": resource_path.queries.dict()}

# and you can also define path parameters using the notation {foo: int}

@server.append(protocol='http')
async def get(resource_path: v1 / "examples" / "hello-world" / "with-ellipsies"):
    return 200, ..., { 
        "queries": resource_path.queries.dict(),
        "parameters": resource_path.parameters.dict(),
    }
    
# you can leave the 200, but the default parameters are something you are
# able to change at various levels, so it is good practice to do DRY and 
# just leave `...`

@server.append(protocol='http')
async def get(resource_path: v1 / "examples" / "hello-world" / "with-ellipsies"):
    return ..., ..., { 
        "queries": resource_path.queries.dict(),
        "parameters": resource_path.parameters.dict(),
    }


# if you want access to the headers:

@server.append(protocol='http')
async def get(
    resource_path: v1 / "examples" / "hello-world" / "with-ellipsies",
    headers: typedAPI.Headers(...)
):
    return ..., ..., { 
        "resource_path":{
            "queries": resource_path.queries.dict(),
            "parameters": resource_path.parameters.dict(),
        },
        "headers": headers
    }

# here, `...` has the same meaning, typedAPI will fill in the details
# in this case it just passes everything

# but let's say you want to do something with the headers, maybe
# validate an api key ? 

@server.append(protocol='http')
async def get(
    resource_path: v1 / "examples" / "hello-world" / "with-ellipsies",
    headers: typedAPI.Headers({
        'x-api-key': lambda api_key: api_key if api_key == "afajsnrars" else 401
    })
):
    return ..., ..., { 
        "resource_path":{
            "queries": resource_path.queries.dict(),
            "parameters": resource_path.parameters.dict(),
        },
        "headers": headers
    }

# note how the anonymous function may return a response like object, in this
# case an integer. When the anonymous function returns a reponse, that response
# is sent. 


if __name__ == "__main__":
    server.listen(host='127.0.0.1', port=8000)
