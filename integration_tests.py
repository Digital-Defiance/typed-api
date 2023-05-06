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



def test_with_ellipsies_1(client):
    response = client.get('/api/v1/examples/hello-world/with-ellipsies-1')
    assert response.status_code == 200

def test_with_ellipsies_2(client):
    response = client.get('/api/v1/examples/hello-world/with-ellipsies-2')
    assert response.status_code == 200
    assert response.json() == {"data": "hello world !"}
    
    

def test_with_queries(client):
    response = client.get('/api/v1/examples/hello-world/with-queries', params={'key': 'value'})
    assert response.status_code == 200
    assert response.json() == {"queries": {"key": "value"}}
    



def test_with_parameters(client):
    response = client.get('/api/v1/examples/asdad/with-parameters')
    assert response.status_code == 200
    assert response.json() == {'queries': {}, 'parameters': {'hello': 'asdad'}}

def test_with_parameters_and_queries(client):
    response = client.get('/api/v1/examples/asdad/with-parameters', params={'key': 'value'})
    assert response.status_code == 200
    assert response.json() == {"queries": {"key": "value"}, 'parameters': {'hello': 'asdad'}}



def test_with_parameters_and_queries_2(client):
    response = client.get('/api/v1/examples/asdad/with-parameters-2', params={'key': 'value'})
    assert response.status_code == 200
    assert response.json() == {"queries": {"key": "value"}, 'parameters': {'hello': 'asdad'}}


def test_with_headers(client):
    headers = {'Custom-Header': 'custom_value'}
    response = client.get('/api/v1/examples/asdad/with-headers', headers=headers, params={'key': 'value'})
    assert response.status_code == 200
    
    response_payload = response.json()
    
    assert "resource_path" in response_payload
    assert "headers" in response_payload

    
    resource_path = response_payload["resource_path"]

    assert "queries" in resource_path
    assert "parameters" in resource_path
    
    assert resource_path["queries"] == {"key": "value"}
    assert resource_path["parameters"] == {'hello': 'asdad'}
    
    assert 'custom-header' in response_payload["headers"]
    assert response_payload["headers"]['custom-header'] == 'custom_value'



def test_with_api_key(client):
    headers = {'x-api-key': 'afajsnrars'}
    response = client.get('/api/v1/examples/hello-world/auth', headers=headers)
    assert response.status_code == 200
    
    response_payload = response.json()
    
    assert "resource_path" in response_payload
    assert "headers" in response_payload

    
    resource_path = response_payload["resource_path"]

    assert "queries" in resource_path
    assert "parameters" in resource_path

    headers = {'x-api-key': 'wrong_api_key'}
    response = client.get('/api/v1/examples/hello-world/auth', headers=headers)
    assert response.status_code == 401
