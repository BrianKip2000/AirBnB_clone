#!/usr/bin/python3
import uuid
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testing the class BaseModel"""
    def test_init_(self):
        #test id
        test1 = BaseModel()
        test2 = BaseModel()
        self.assertIsInstance(test1.id, str)
        self.assertNotEqual(test1.id, test2.id)

        #test created_at
        test_1 = test1.created_at
        
        test_2 = test2.created_at
        self.assertNotEqual(test_1, test_2)

        #test updated
        test_3 = test1.updated_at
        test_4 = test2.created_at
        self.assertNotEqual(test_3, test_4)

        #test kwargs
        
    def test_save(self):
        tests_save = BaseModel()
        tests_sa = tests_save.updated_at
        tests_save.save()
        tests = tests_save.updated_at
        tests_save == tests
        self.assertNotEqual(tests_sa, tests)

    def test_to_dict(self):
            """tests the to_dict method of the BaseModel"""
            test_to_dict = BaseModel()
            dictionary = test_to_dict.to_dict()
            self.assertIn('created_at', dictionary)
            self.assertIn('__class__', dictionary)
            self.assertIn('updated_at', dictionary)
            self.assertIsInstance(dictionary['created_at'], str)
            self.assertIsInstance(dictionary['updated_at'], str)
            self.assertEqual(dictionary['created_at'], test_to_dict.created_at.isoformat())
            
            
if __name__ == "__main__":
    unittest.main()
