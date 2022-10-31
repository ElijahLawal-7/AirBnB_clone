#!/usr/bin/python3
"""Test File for the city class"""
import unittest
from models.city import City
from models.base_model import BaseModel
import os
from datetime import datetime


class TestCityModel(unittest.TestCase):
    """Test cases for the city model"""

    def setUp(self):
        """set up method for the city model"""
        self.city = City()
        self.city_2 = City(id="12-345-678",
                           created_at='2017-09-28T21:05:54.119427',
                           updated_at='2017-09-28T21:05:54.119427')
        return super().setUp()

    def tearDown(self):
        """tear down method for the city model"""
        del(self.city)
        del(self.city_2)
        if os.path.exists("file.json"):
            os.remove("file.json")
        return super().tearDown()

    def test_citymodel(self):
        """Tests to verify the city model"""
        self.assertIsInstance(self.city, BaseModel)
        self.assertIsInstance(self.city, City)
        self.assertEqual(type(self.city).__name__, "City")
        self.assertEqual(type(self.city_2).__name__, "City")
        self.assertIsInstance(self.city, object)
        self.assertIsInstance(self.city_2, object)

    def test_citymodel_attributes(self):
        """Tests to verify the city model attributes"""
        self.assertIn("id", self.city.to_dict().keys())
        self.assertIn("created_at", self.city.to_dict().keys())
        self.assertIn("updated_at", self.city.to_dict().keys())
        self.assertIn("__class__", self.city.to_dict().keys())
        self.assertNotIn("my_number", self.city.to_dict().keys())
        self.city.my_number = 45
        self.assertIn("my_number", self.city.to_dict().keys())

    def test_citymodel_dates(self):
        """Tests to verify the date attributes of the city model"""
        format = "%Y-%m-%dT%H:%M:%S.%f"
        dict_date = self.city.to_dict()["updated_at"]
        updated_at = self.city.updated_at

        self.assertIsInstance(dict_date, str)
        self.assertIsInstance(updated_at, datetime)
        self.assertEqual(dict_date, updated_at.isoformat())
        self.assertEqual(updated_at, datetime.strptime(dict_date, format))

    def test_citymodel_dict(self):
        """Tests to verify the to_dict method of the city model"""
        self.assertIsInstance(self.city.to_dict(), dict)
        self.assertIsInstance(self.city_2.to_dict(), dict)

    def test_citymodel_str(self):
        """Tests to verify the str method of the city model"""
        class_name = type(self.city).__name__
        string_format = "[{}] ({}) {}".format(class_name, self.city.id,
                                              self.city.__dict__)
        self.assertEqual(str(self.city), string_format)

    def test_citymodel_save(self):
        """Tests to verify the save method of the city model"""
        updated_at = self.city.updated_at
        self.assertEqual(updated_at, self.city.updated_at)
        self.city.save()
        self.assertLessEqual(updated_at, self.city.updated_at)


if __name__ == '__main__':
    unittest.main()
