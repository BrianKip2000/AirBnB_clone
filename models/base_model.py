#!/usr/bin/python3
import uuid
from datetime import datetime
#from models import storage


class BaseModel:
    """Base class for entire project"""
    def __init__(self, *args, **kwargs):
        """Class initialization"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """Returns a printed dictionary in string format"""
        return (f"[{__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Returns updated at with current date and time"""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the class"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
