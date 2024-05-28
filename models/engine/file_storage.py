#!/usr/bin/python3
import json
import models


class FileStorage:
    """Class that stores our HBNB details"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary in objects private attr"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name.id>"""
        if obj:
            self.__objects["{} {}".format(str(type(obj).__name__), obj.id)] = obj

    def save(self):
        """Serializes __objects to json file"""
        dict = {}
        for id, objs in self.__objects.items():
            dict[id] = objs.to_dict()
        with open(self.__file_path, mode='w', encoding='útf-8') as file:
            json.dump(dict, file)

    def reload(self):
        """Deserializes the json file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                obj = json.load(file)
            for key, value in obj.items():
                name = models.allclasses[value["__class__"]](**value)
                self.__objects[key] = name
        except Exception:
            pass
