#!/usr/bin/python3
"""Test city"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test city model"""
    def setUp(self):
      self.test_cit = City()

    def test_city(self):
        self.assertIs(self.test_cit.state_id, "")
        self.assertIs(self.test_cit.name, "")

if __name__ == '__main__':
    TestCity().unittest()
