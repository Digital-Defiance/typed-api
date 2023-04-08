# type: ignore

import typedAPI

server = typedAPI.Server()

base = typedAPI.ResourcePath("/api/v1")

MOCK_DB = {
    "id": [1, 2, 3],
    "title": ["title1", "title2", "title3"],
    "content": ["Aas fadsfads f", "asdfasfdf", "dfasdfsdaf"]
}


@server.append(protocol='http')
async def get(resource_path: base / "test" / "{some_id:int}"):

    db_values = MOCK_DB.values()
    db_entries = zip(*db_values)

    return 200, {
        "content-type": "application/json"
    }, {
        "status": "OK",
        "resource_path": {
            "value": str(resource_path),
            "parameters": resource_path.parameters.dict(),
            "queries": resource_path.queries.dict()
        },
        "data": [
            {
                "id": id,
                "title": title,
                "content": content
            } for id, title, content in db_entries
        ]
    }

if __name__ == "__main__":
    server.listen(host='127.0.0.1', port=8000)