# typed-api
A small, python backend framework that leverages Pythons type hinting to concisely define an api.


What I'm aiming for:

```Python

router = Router()

@router.post()
def as_admin_create_a_user(
    endpoint: Endpoint("/abc/[param: str]/[param2: int]?[param3: int][param4: str]"),
    headers: Headers({
        "X-Auth-Header": str,
        "asdasd": int
    }),
    body: int
):
    
    if headers["asdasd"] == 2:
        print("user is admin")
    
    if endpoint.param == "":
        pass

    return 200, {
        "Set-Cookie": "asdasdsada",
        "content-type": "application/json"
    }, {
        "status": "OK",
        "date": "asdsadsdafads7689adsf",
        "body": body,
    }
    
```
