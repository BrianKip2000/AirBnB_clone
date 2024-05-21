#!/usr/bin/python3
import json
import os


class FileStorage:
    """Class that stores our HBNB details"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary in objects private attr"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name.id>"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to json file"""
        obj_dict = {key: obj.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the json file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split()
                    obj_class = globals()[class_name]
                    obj = obj_class.from_dict(value)
                    self.__obj[key] = obj