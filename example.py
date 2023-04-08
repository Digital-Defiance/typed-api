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