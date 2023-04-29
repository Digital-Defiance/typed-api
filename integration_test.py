import pytest
from starlette.testclient import TestClient
from example import server

@pytest.fixture
def client():
    return TestClient(server)

def test_hello_world(client):
    response = client.get('/api/v1/examples/hello-world')
    assert response.status_code == 200

def test_complete_response(client):
    response = client.get('/api/v1/examples/hello-world/complete-response')
    assert response.status_code == 200
    assert response.text == "hello world !"

def test_omitted_body(client):
    response = client.get('/api/v1/examples/hello-world/ommited-body')
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/plain"

def test_with_ellipsies(client):
    response = client.get('/api/v1/examples/hello-world/with-ellipsies')
    assert response.status_code == 200
    assert response.json() == {"data": "hello world !"}

def test_with_queries(client):
    response = client.get('/api/v1/examples/hello-world/with-ellipsies', params={'key': 'value'})
    assert response.status_code == 200
    assert response.json() == {"queries": {"key": "value"}}

def test_with_parameters(client):
    response = client.get('/api/v1/examples/hello-world/with-ellipsies')
    assert response.status_code == 200

def test_with_headers(client):
    headers = {'Custom-Header': 'custom_value'}
    response = client.get('/api/v1/examples/hello-world/with-ellipsies', headers=headers)
    assert response.status_code == 200

def test_with_api_key(client):
    headers = {'x-api-key': 'afajsnrars'}
    response = client.get('/api/v1/examples/hello-world/with-ellipsies', headers=headers)
    assert response.status_code == 200

    headers = {'x-api-key': 'wrong_api_key'}
    response = client.get('/api/v1/examples/hello-world/with-ellipsies', headers=headers)
    assert response.status_code == 401
