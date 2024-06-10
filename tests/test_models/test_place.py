#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """unittest for place"""
    def setUp(self):
        self.tst_place = Place()

    def test_place(self):
        self.assertIs(type(self.tst_place.city_id), str)
        self.assertIs(type(self.tst_place.user_id), str)
        self.assertIs(type(self.tst_place.name), str)
        self.assertIs(type(self.tst_place.description), str)
        self.assertIs(type(self.tst_place.number_rooms), int)
        self.assertIs(type(self.tst_place.number_bathrooms), int)
        self.assertIs(type(self.tst_place.max_guest), int)
        self.assertIs(type(self.tst_place.price_by_night), int)
        self.assertIs(type(self.tst_place.latitude), float)
        self.assertIs(type(self.tst_place.longitude), float)
        self.assertIs(type(self.tst_place.amentity_ids), list)

if __name__ == '__main__':
    TestPlace().unittest()
