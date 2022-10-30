#!/usr/bin/python3
"""Test File for the amenity class"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import os
from datetime import datetime


class TestAmenityModel(unittest.TestCase):
    """Test cases for the amenity model"""

    def setUp(self):
        """The set up method"""
        self.amenity = Amenity()
        self.amenity_2 = Amenity(id="12-345-678",
                                 created_at='2017-09-28T21:05:54.119427',
                                 updated_at='2017-09-28T21:05:54.119427')
        return super().setUp()

    def tearDown(self):
        """The tear down method"""
        del(self.amenity)
        del(self.amenity_2)
        if os.path.exists("file.json"):
            os.remove("file.json")
        return super().tearDown()

    def test_amenitymodel(self):
        """Tests to verify the amenity model"""
        self.assertIsInstance(self.amenity, BaseModel)
        self.assertIsInstance(self.amenity, Amenity)
        self.assertEqual(type(self.amenity).__name__, "Amenity")
        self.assertEqual(type(self.amenity_2).__name__, "Amenity")
        self.assertIsInstance(self.amenity, object)
        self.assertIsInstance(self.amenity_2, object)

    def test_amenitymodel_attributes(self):
        """Tests to verify the attributes of the amenity model"""
        self.assertIn("id", self.amenity.to_dict().keys())
        self.assertIn("created_at", self.amenity.to_dict().keys())
        self.assertIn("updated_at", self.amenity.to_dict().keys())
        self.assertIn("__class__", self.amenity.to_dict().keys())
        self.assertNotIn("my_number", self.amenity.to_dict().keys())
        self.amenity.my_number = 45
        self.assertIn("my_number", self.amenity.to_dict().keys())

    def test_amenitymodel_dates(self):
        """Tests to verify date attributes in the amenity model"""
        format = "%Y-%m-%dT%H:%M:%S.%f"
        dict_date = self.amenity.to_dict()["updated_at"]
        updated_at = self.amenity.updated_at

        self.assertIsInstance(dict_date, str)
        self.assertIsInstance(updated_at, datetime)
        self.assertEqual(dict_date, updated_at.isoformat())
        self.assertEqual(updated_at, datetime.strptime(dict_date, format))

    def test_amenitymodel_dict(self):
        """Tests to verify the to_dict method of the amenity model"""
        self.assertIsInstance(self.amenity.to_dict(), dict)
        self.assertIsInstance(self.amenity_2.to_dict(), dict)

    def test_amenitymodel_str(self):
        """Tests to verify the str method of the amenity model"""
        class_name = type(self.amenity).__name__
        string_format = "[{}] ({}) {}".format(class_name, self.amenity.id,
                                              self.amenity.__dict__)
        self.assertEqual(str(self.amenity), string_format)

    def test_amenitymodel_save(self):
        """Tests to verify the save method of the amenity model"""
        updated_at = self.amenity.updated_at
        self.assertEqual(updated_at, self.amenity.updated_at)
        self.amenity.save()
        self.assertLessEqual(updated_at, self.amenity.updated_at)


if __name__ == '__main__':
    unittest.main()
