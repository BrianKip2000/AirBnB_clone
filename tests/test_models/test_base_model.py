#!/usr/bin/python3
import uuid
import datetime as datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test save() class"""
    def test_save_method(self):
        saving_class = BaseModel()
        saving_class_new = saving_class.updated_at
        saving_class.save()
        self.assertNotEqual(saving_class_new, saving_class.updated_at)
        self.assertGreater(saving_class.updated_at, saving_class_new)
