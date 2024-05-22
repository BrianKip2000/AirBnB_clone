#!/usr/bin/python3
"""
This module contains the tests for the FileStorage class.
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Test case for the FileStorage class.

    This test case verifies that the FileStorage class correctly saves and reloads objects.

    Methods:
        setUp(self): Sets up the test case by initializing the FileStorage object.
        tearDown(self): Tears down the test case by reloading the objects from the JSON file.
        test_all_returns_objects(self): Verifies that the `all` method 
        correctly returns all the objects in the `__objects` attribute.
        test_save_and_reload(self): Verifies that the `save` and `reload`
        methods correctly save and reload the objects in the `__objects` attribute.
    """

    def setUp(self):
        """
        Set up the test case by initializing the FileStorage object.

        Parameters:
            self (TestFileStorage): The current test case object.

        Returns:
            None
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Tears down the test case by reloading the objects from the JSON file.

        Parameters:
            self (TestFileStorage): The current test case object.

        Returns:
            None
        """
        self.storage.reload()

    def test_all_returns_objects(self):
        """
        Verifies that the `all` method correctly 
        returns all the objects in the `__objects` attribute.

        Parameters:
            self (TestCase): The current test case object.

        Returns:
            None
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        result = self.storage.all()
        self.assertEqual(result, self.storage.__objects)

    def test_save_and_reload(self):
        """
        Verifies that the `save` and `reload` methods correctly save 
        and reload the objects in the `__objects` attribute.

        This test case creates two instances of the `BaseModel` class 
        and adds them to the `FileStorage` object using the `new` method. 
        It then calls the `save` method to serialize the objects to a JSON file 
        and the `reload` method to deserialize the objects from the JSON file. 
        Finally, it calls the `all` method to retrieve all the objects and 
        compares the result with the `__objects` attribute of the `FileStorage` object. 
        The test asserts that the result is equal to the `__objects` attribute.

        Parameters:
            self (TestCase): The current test case object.

        Returns:
            None
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()
        self.storage.reload()
        result = self.storage.all()
        self.assertEqual(result, self.storage.__objects)


if __name__ == '__main__':
    unittest.main()
