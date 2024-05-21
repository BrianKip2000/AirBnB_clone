#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests the BaseModel class"""

    def test_instantiation(self):
        """Tests instantiation of BaseModel class"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_save(self):
        """Tests save method of BaseModel class"""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict(self):
        """Tests to_dict method of BaseModel class"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict['updated_at'], my_model.updated_at.isoformat())
        self.assertEqual(my_model_dict['name'], my_model.name)
        self.assertEqual(my_model_dict['my_number'], my_model.my_number)
        self.assertEqual(my_model_dict['id'], my_model.id)

    def test_str(self):
        """Tests __str__ method of BaseModel class"""
        my_model = BaseModel()
        expected_str = f"[{my_model.__class__.__name__}] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(str(my_model), expected_str)

if __name__ == '__main__':
    unittest.main()
