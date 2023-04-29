import unittest
from starlette.testclient import TestClient

from example import server

class TestTypedAPIExample(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(server)

    def test_hello_world(self):
        response = self.client.get('/api/v1/examples/hello-world')
        self.assertEqual(response.status_code, 200)

    def test_complete_response(self):
        response = self.client.get('/api/v1/examples/hello-world/complete-response')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "hello world !")


    def test_omitted_body(self):
        response = self.client.get('/api/v1/examples/hello-world/ommited-body')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["content-type"], "text/plain")


    """
    def test_with_ellipsies(self):
        response = self.client.get('/api/v1/examples/hello-world/with-ellipsies')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"data": "hello world !"})

    

    def test_with_queries(self):
        response = self.client.get('/api/v1/examples/hello-world/with-ellipsies', params={'key': 'value'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"queries": {"key": "value"}})

    def test_with_parameters(self):
        response = self.client.get('/api/v1/examples/hello-world/with-ellipsies')
        self.assertEqual(response.status_code, 200)

    def test_with_headers(self):
        headers = {'Custom-Header': 'custom_value'}
        response = self.client.get('/api/v1/examples/hello-world/with-ellipsies', headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_with_api_key(self):
        headers = {'x-api-key': 'afajsnrars'}
        response = self.client.get('/api/v1/examples/hello-world/with-ellipsies', headers=headers)
        self.assertEqual(response.status_code, 200)

        headers = {'x-api-key': 'wrong_api_key'}
        response = self.client.get('/api/v1/examples/hello-world/with-ellipsies', headers=headers)
        self.assertEqual(response.status_code, 401)
    """

if __name__ == '__main__':
    unittest.main()
