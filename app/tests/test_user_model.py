import sys
import unittest

sys.path.append('.')

from app.models import users as user_model


class TestUserModel(unittest.TestCase):
    def test_create_user_and_get_user_by_id_email(self):
        user_json = {
            "id": 1,
            "name": "Mike",
            "email": "myemail@google.com",
            "password": "kdsjflkjflsk",
            "created_at": user_model.datetime.utcnow()
        }
        user = user_model.UserCreate(**user_json)
        user_id = user_model.create_user(user)
        user_2 = user_model.get_user_by_id(user_id)
        user_3 = user_model.get_user_by_email(user_json['email'])
        self.assertEqual(user_2, user_3)
        self.assertEqual(user_2.id, user_json['id'])
        self.assertEqual(user_2.name, user_json['name'])
        self.assertEqual(user_2.email, user_json['email'])


    def test_create_and_decode_token(self):
        id = 372
        auth_token = user_model.create_token(id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(user_model.decode_token(auth_token) == id)



if __name__ == '__main__':
    unittest.main()
