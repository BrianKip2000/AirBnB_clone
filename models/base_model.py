#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base class for the entire HBNB project"""
    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dict containing all keys/values of __dict__"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.created_at.isoformat()

        return obj_dict
