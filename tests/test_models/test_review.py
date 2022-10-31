#!/usr/bin/python3
"""Test File for the review class"""
import unittest
from models.review import Review
from models.base_model import BaseModel
import os
from datetime import datetime


class TestReviewModel(unittest.TestCase):
    """Test cases for the review model"""

    def setUp(self):
        """set up method for the review model"""
        self.review = Review()
        self.review_2 = Review(id="12-345-678",
                               created_at='2017-09-28T21:05:54.119427',
                               updated_at='2017-09-28T21:05:54.119427')
        return super().setUp()

    def tearDown(self):
        """tear down method for the review model"""
        del(self.review)
        del(self.review_2)
        if os.path.exists("file.json"):
            os.remove("file.json")
        return super().tearDown()

    def test_reviewmodel(self):
        """Tests for verifying the review model"""
        self.assertIsInstance(self.review, BaseModel)
        self.assertIsInstance(self.review, Review)
        self.assertEqual(type(self.review).__name__, "Review")
        self.assertEqual(type(self.review_2).__name__, "Review")
        self.assertIsInstance(self.review, object)
        self.assertIsInstance(self.review_2, object)

    def test_reviewmodel_attributes(self):
        """Tests for veifying the attributes of the review model"""
        self.assertIn("id", self.review.to_dict().keys())
        self.assertIn("created_at", self.review.to_dict().keys())
        self.assertIn("updated_at", self.review.to_dict().keys())
        self.assertIn("__class__", self.review.to_dict().keys())
        self.assertNotIn("my_number", self.review.to_dict().keys())
        self.review.my_number = 45
        self.assertIn("my_number", self.review.to_dict().keys())

    def test_reviewmodel_dates(self):
        """Tests for verifying the date attributes of the review model"""
        format = "%Y-%m-%dT%H:%M:%S.%f"
        dict_date = self.review.to_dict()["updated_at"]
        updated_at = self.review.updated_at

        self.assertIsInstance(dict_date, str)
        self.assertIsInstance(updated_at, datetime)
        self.assertEqual(dict_date, updated_at.isoformat())
        self.assertEqual(updated_at, datetime.strptime(dict_date, format))

    def test_reviewmodel_dict(self):
        """Tests for verifying the to_dict method of the review model"""
        self.assertIsInstance(self.review.to_dict(), dict)
        self.assertIsInstance(self.review_2.to_dict(), dict)

    def test_reviewmodel_str(self):
        """Tests for verifying the str method of the review model"""
        class_name = type(self.review).__name__
        string_format = "[{}] ({}) {}".format(class_name, self.review.id,
                                              self.review.__dict__)
        self.assertEqual(str(self.review), string_format)

    def test_reviewmodel_save(self):
        """Tests for verifying the save method of the review model"""
        updated_at = self.review.updated_at
        self.assertEqual(updated_at, self.review.updated_at)
        self.review.save()
        self.assertLessEqual(updated_at, self.review.updated_at)


if __name__ == '__main__':
    unittest.main()
