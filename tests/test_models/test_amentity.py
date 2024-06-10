#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmentity(unittest.TestCase):
    """Test amentity"""
    def setUp(self):
        self.test_amentity = Amenity()

    def test_amentty(self):
        self.assertIs(self.test_amentity.name, '')

if __name__ == '__main__':
    TestAmentity().unittest()
