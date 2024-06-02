#!/usr/bin/python3
import json
import os


class FileStorage:
    """
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        if obj.id in FileStorage.__objects:
            print("exists")
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj
        # OR
        # type(self).__objects[obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = []
        for obj in FileStorage.__objects.values():
            new_dict.append(obj.to_dict())
        with open(FileStorage.__file_path, "w", encoding='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects if it exists"""
        if os.path.exists(FileStorage.__file_path) is True:
            try:
                with open(FileStorage.__file_path, "r") as file:
                    new_obj = json.load(file)
                    for key, val in new_obj.items():
                        obj = self.class_dict[val['__class__']](**val)
                        FileStorage.__objects[key] = obj
            except Exception:
                pass
