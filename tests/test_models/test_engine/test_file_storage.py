import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        self.storage.reload()

    def test_all_returns_objects(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        result = self.storage.all()
        self.assertEqual(result, self.storage.__objects)

    def test_save_and_reload(self):
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
