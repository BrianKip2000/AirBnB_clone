#!/usr/bin/python3
import uuid
import datetime as datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test save() class"""
    def test_save_method(self):
        """Method string to test for BaseModel saving"""
        saving_class = BaseModel()
        saving_class_new = saving_class.updated_at
        saving_class.save()
        self.assertNotEqual(saving_class_new, saving_class.updated_at)
        self.assertGreater(saving_class.updated_at, saving_class_new)

    def test_to_str_method(self):
        """Unittest for to string method"""
        new_string = BaseModel()
        new_string.name = "Brian"
        new_string.my_number = 89
        self.assertEqual(new_string_dict['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()
