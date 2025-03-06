#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Module to test BaseModel class
    """
    def test_save(self):
        """
        Tests the save method
        """
        testModel = BaseModel()
        old_updated = testModel.updated_at

        testModel.save()

        self.assertNotEqual(old_updated, testModel.updated_at)
        self.assertIsInstance(testModel.updated_at, datetime)
    
    def test_to_dict(self):
        """Tests if the to dictionary method works well"""
        testModel = BaseModel()
        testModel.name = "Home Work"
        testModel.number = 10
        testModel.save()

        newDict = testModel.to_dict()

        self.assertIsInstance(newDict, dict)

    def test_str(self):
        """Tests whether str output will be printed"""
        testModel = BaseModel()

        out_printed = f"[{testModel.__class__.__name__}] ({testModel.id}) <{testModel.__dict__}>"

        self.assertEqual(str(testModel), out_printed) 

if __name__ == '__main__':
    unittest.main()

