#!/usr/bin/python3
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """test review"""
    def setUp(self):
        self.review = Review()

    def test_review(self):
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(type(self.review.text), str)

