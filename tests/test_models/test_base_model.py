#!/usr/bin/python3
"""Test File for the base model class"""
import unittest
from models.base_model import BaseModel
import os
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the base model"""

    def setUp(self):
        """set up method for the base model"""
        self.model = BaseModel()
        self.model_2 = BaseModel(id="12-345-678",
                                 created_at='2017-09-28T21:05:54.119427',
                                 updated_at='2017-09-28T21:05:54.119427')
        return super().setUp()

    def tearDown(self):
        """tear down method for the base model"""
        del(self.model)
        del(self.model_2)
        if os.path.exists("file.json"):
            os.remove("file.json")
        return super().tearDown()

    def test_basemodel(self):
        """Tests to verify the base model"""
        self.assertEqual(type(self.model).__name__, "BaseModel")
        self.assertEqual(type(self.model_2).__name__, "BaseModel")
        self.assertIsInstance(self.model, object)
        self.assertIsInstance(self.model_2, object)

    def test_basemodel_attributes(self):
        """Tests to verify the base model attributes"""
        self.assertIn("id", self.model.to_dict().keys())
        self.assertIn("created_at", self.model.to_dict().keys())
        self.assertIn("updated_at", self.model.to_dict().keys())
        self.assertIn("__class__", self.model.to_dict().keys())
        self.assertNotIn("my_number", self.model.to_dict().keys())
        self.model.my_number = 903
        self.assertIn("my_number", self.model.to_dict().keys())

    def test_basemodel_dates(self):
        """Tests to verify the date attributes of the base model"""
        format = "%Y-%m-%dT%H:%M:%S.%f"
        dict_date = self.model.to_dict()["updated_at"]
        updated_at = self.model.updated_at

        self.assertIsInstance(dict_date, str)
        self.assertIsInstance(updated_at, datetime)
        self.assertEqual(dict_date, updated_at.isoformat())
        self.assertEqual(updated_at, datetime.strptime(dict_date, format))

    def test_basemodel_dict(self):
        """Tests to verify the to_dict method of the base model"""
        self.assertIsInstance(self.model.to_dict(), dict)
        self.assertIsInstance(self.model_2.to_dict(), dict)

    def test_basemodel_str(self):
        """Tests to verify the str method of the base model"""
        class_name = type(self.model).__name__
        string_format = "[{}] ({}) {}".format(class_name, self.model.id,
                                              self.model.__dict__)
        self.assertEqual(str(self.model), string_format)

    def test_basemodel_save(self):
        """Tests to verify the save method of the base model"""
        updated_at = self.model.updated_at
        self.assertEqual(updated_at, self.model.updated_at)
        self.model.save()
        self.assertLessEqual(updated_at, self.model.updated_at)


if __name__ == '__main__':
    unittest.main()
