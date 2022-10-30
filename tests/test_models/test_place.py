#!/usr/bin/python3
"""Test File for the place class"""
import unittest
from models.place import Place
from models.base_model import BaseModel
import os
from datetime import datetime


class TestPlaceModel(unittest.TestCase):
    """Test cases for the place model"""

    def setUp(self):
        """set up method for testing the place model"""
        self.place = Place()
        self.place_2 = Place(id="12-345-678",
                             created_at='2017-09-28T21:05:54.119427',
                             updated_at='2017-09-28T21:05:54.119427')
        return super().setUp()

    def tearDown(self):
        """tear down method for testing the place model"""
        del(self.place)
        del(self.place_2)
        if os.path.exists("file.json"):
            os.remove("file.json")
        return super().tearDown()

    def test_placemodel(self):
        """Tests for verifying the place model"""
        self.assertIsInstance(self.place, BaseModel)
        self.assertIsInstance(self.place, Place)
        self.assertEqual(type(self.place).__name__, "Place")
        self.assertEqual(type(self.place_2).__name__, "Place")
        self.assertIsInstance(self.place, object)
        self.assertIsInstance(self.place_2, object)

    def test_placemodel_attributes(self):
        """Tests for verifying the attributes of the place model"""
        self.assertIn("id", self.place.to_dict().keys())
        self.assertIn("created_at", self.place.to_dict().keys())
        self.assertIn("updated_at", self.place.to_dict().keys())
        self.assertIn("__class__", self.place.to_dict().keys())
        self.assertNotIn("my_number", self.place.to_dict().keys())
        self.place.my_number = 45
        self.assertIn("my_number", self.place.to_dict().keys())

    def test_placemodel_dates(self):
        """Tests for verifying the date attributes of the place model"""
        format = "%Y-%m-%dT%H:%M:%S.%f"
        dict_date = self.place.to_dict()["updated_at"]
        updated_at = self.place.updated_at

        self.assertIsInstance(dict_date, str)
        self.assertIsInstance(updated_at, datetime)
        self.assertEqual(dict_date, updated_at.isoformat())
        self.assertEqual(updated_at, datetime.strptime(dict_date, format))

    def test_placemodel_dict(self):
        """Tests for verifying the to_dict methods of the place model"""
        self.assertIsInstance(self.place.to_dict(), dict)
        self.assertIsInstance(self.place_2.to_dict(), dict)

    def test_placemodel_str(self):
        """Tests for verifying the str method of the place model"""
        class_name = type(self.place).__name__
        string_format = "[{}] ({}) {}".format(class_name, self.place.id,
                                              self.place.__dict__)
        self.assertEqual(str(self.place), string_format)

    def test_placemodel_save(self):
        """Tests for verifying the save method of the place model"""
        updated_at = self.place.updated_at
        self.assertEqual(updated_at, self.place.updated_at)
        self.place.save()
        self.assertLessEqual(updated_at, self.place.updated_at)


if __name__ == '__main__':
    unittest.main()
