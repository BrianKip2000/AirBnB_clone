#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """Base Class for AirBnB project"""

    def __init__(self, *args, **kwargs):
        """Initialize class with public attributes"""
        if kwargs:
            for key, value in kwargs.items():
                    if key in [ "updated_at" ,"created_at"]:
                        setattr(self, key, datetime.fromisoformat(str(value)))
                    elif key != "__class__":
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        prints out the class name, its id, and the dictionary at which
        it was stored
        """
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """
        Saves the created id at the updated time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Adds class, created_at and updated_at to the dictionary
        returns a dictionary with all of above
        Utilizes isoformat()
        """
        return {
            "id": self.id,
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            **self.__dict__,
            }
