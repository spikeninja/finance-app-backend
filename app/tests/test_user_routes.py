import sys
import unittest
from fastapi.testclient import TestClient

sys.path.append('.')

from main import app


client = TestClient(app)


class TestUserRoutes(unittest.TestCase):
    def test_register(self):
        user_json = {
            "name": "some_name",
            "email": "some_email",
            "password": "kfjalks"
        }
        response = client.post('/register',
            json=user_json
        )
        self.assertTrue(response.status_code == 200)

    def test_auth(self):
        form_request = {
            "username": "some_email",
            "password": "kfjalks"
        }
        response = client.get('/auth',
            json=form_request
        )
        print(response)
        self.assertTrue(response.status_code == 200)

    def test_me(self):
        form_request = {
            "username": "some_email",
            "password": "kfjalks"
        }
        auth_token = client.get('/auth',
            json=form_request
        )
        print(auth_token)
        self.assertTrue(auth_token.status_code == 200)
        user = client.get('/me',
            headers=auth_token.json()
        )
        self.assertTrue(user.status_code == 200)


if __name__ == "__main__":
    unittest.main()
