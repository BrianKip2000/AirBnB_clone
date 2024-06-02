#!/usr/bin/python3
"""File Storage"""
import json
import os


class FileStorage:
    """File Storage module"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set objects with key"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves __objects to the JSON file"""
        objs = {}
        for k, v in FileStorage.__objects.items():
            objs[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(objs, file)

    def reload(self):
        """Reloads the stored objects"""
        from models.base_model import BaseModel
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            
            # Check if the loaded data is a dictionary
            if isinstance(obj_dict, dict):
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)  # Assuming the class is already imported
                    instance = cls(**value)
                    FileStorage.__objects[key] = instance
            else:
                raise TypeError("Expected a dictionary in the JSON file, but got a list")


