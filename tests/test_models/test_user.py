#!/usr/bin/python3
"""Test File for the user class"""
import unittest
from models.user import User
from models.base_model import BaseModel
import os
from datetime import datetime


class TestUserModel(unittest.TestCase):
    """Test cases for the user model"""

    def setUp(self):
        """set up method for testing the user model"""
        self.user = User()
        self.user_2 = User(id="12-345-678",
                           created_at='2017-09-28T21:05:54.119427',
                           updated_at='2017-09-28T21:05:54.119427')
        return super().setUp()

    def tearDown(self):
        """tear down method for testing the user model"""
        del(self.user)
        del(self.user_2)
        if os.path.exists("file.json"):
            os.remove("file.json")
        return super().tearDown()

    def test_usermodel(self):
        """Tests for verifying the user model"""
        self.assertIsInstance(self.user, BaseModel)
        self.assertIsInstance(self.user, User)
        self.assertEqual(type(self.user).__name__, "User")
        self.assertEqual(type(self.user_2).__name__, "User")
        self.assertIsInstance(self.user, object)
        self.assertIsInstance(self.user_2, object)

    def test_usermodel_attributes(self):
        """Tests for verifying the attributes of the user model"""
        self.assertIn("id", self.user.to_dict().keys())
        self.assertIn("created_at", self.user.to_dict().keys())
        self.assertIn("updated_at", self.user.to_dict().keys())
        self.assertIn("__class__", self.user.to_dict().keys())
        self.assertNotIn("my_number", self.user.to_dict().keys())
        self.user.my_number = 987
        self.assertIn("my_number", self.user.to_dict().keys())

    def test_usermodel_dates(self):
        """Tests for verifying the date attributes of the user model"""
        format = "%Y-%m-%dT%H:%M:%S.%f"
        dict_date = self.user.to_dict()["updated_at"]
        updated_at = self.user.updated_at

        self.assertIsInstance(dict_date, str)
        self.assertIsInstance(updated_at, datetime)
        self.assertEqual(dict_date, updated_at.isoformat())
        self.assertEqual(updated_at, datetime.strptime(dict_date, format))

    def test_usermodel_dict(self):
        """Tests for verifying the to_dict method of the user model"""
        self.assertIsInstance(self.user.to_dict(), dict)
        self.assertIsInstance(self.user_2.to_dict(), dict)

    def test_usermodel_str(self):
        """Tests for verifying the str method of the user model"""
        class_name = type(self.user).__name__
        string_format = "[{}] ({}) {}".format(class_name, self.user.id,
                                              self.user.__dict__)
        self.assertEqual(str(self.user), string_format)

    def test_usermodel_save(self):
        """Tests for verifying the save method of the user model"""
        updated_at = self.user.updated_at
        self.assertEqual(updated_at, self.user.updated_at)
        self.user.save()
        self.assertLessEqual(updated_at, self.user.updated_at)


if __name__ == '__main__':
    unittest.main()
