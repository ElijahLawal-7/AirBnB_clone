#!/usr/bin/python3
"""Test File for the state class"""
import unittest
from models.state import State
from models.base_model import BaseModel
import os
from datetime import datetime


class TestStateModel(unittest.TestCase):
    """Test cases for the state model"""

    def setUp(self):
        """set up method for testing the state model"""
        self.state = State()
        self.state_2 = State(id="12-345-678",
                             created_at='2017-09-28T21:05:54.119427',
                             updated_at='2017-09-28T21:05:54.119427')
        return super().setUp()

    def tearDown(self):
        """tear down method for testing the state model"""
        del(self.state)
        del(self.state_2)
        if os.path.exists("file.json"):
            os.remove("file.json")
        return super().tearDown()

    def test_statemodel(self):
        """Tests for verifying the state model"""
        self.assertIsInstance(self.state, BaseModel)
        self.assertIsInstance(self.state, State)
        self.assertEqual(type(self.state).__name__, "State")
        self.assertEqual(type(self.state_2).__name__, "State")
        self.assertIsInstance(self.state, object)
        self.assertIsInstance(self.state_2, object)

    def test_statemodel_attributes(self):
        """Tests for verifying the attributes of the dtate model"""
        self.assertIn("id", self.state.to_dict().keys())
        self.assertIn("created_at", self.state.to_dict().keys())
        self.assertIn("updated_at", self.state.to_dict().keys())
        self.assertIn("__class__", self.state.to_dict().keys())
        self.assertNotIn("my_number", self.state.to_dict().keys())
        self.state.my_number = 45
        self.assertIn("my_number", self.state.to_dict().keys())

    def test_statemodel_dates(self):
        """Tests for verifying the date attributes of the state model"""
        format = "%Y-%m-%dT%H:%M:%S.%f"
        dict_date = self.state.to_dict()["updated_at"]
        updated_at = self.state.updated_at

        self.assertIsInstance(dict_date, str)
        self.assertIsInstance(updated_at, datetime)
        self.assertEqual(dict_date, updated_at.isoformat())
        self.assertEqual(updated_at, datetime.strptime(dict_date, format))

    def test_statemodel_dict(self):
        """Tests for verifying the to_dict method of the state model"""
        self.assertIsInstance(self.state.to_dict(), dict)
        self.assertIsInstance(self.state_2.to_dict(), dict)

    def test_statemodel_str(self):
        """Tests for verifying the str method of the state model"""
        class_name = type(self.state).__name__
        string_format = "[{}] ({}) {}".format(class_name, self.state.id,
                                              self.state.__dict__)
        self.assertEqual(str(self.state), string_format)

    def test_statemodel_save(self):
        """Tests for verifying the save method of the state model"""
        updated_at = self.state.updated_at
        self.assertEqual(updated_at, self.state.updated_at)
        self.state.save()
        self.assertLessEqual(updated_at, self.state.updated_at)


if __name__ == '__main__':
    unittest.main()
