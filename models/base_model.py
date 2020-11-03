#!/usr/bin/python3
""" Principal class"""

from uuid import uuid4
from datetime import datetime
import models


date_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Base Model class"""

    def __init__(self, *args, **kwargs):
        """Contructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, date_format)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """toString"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """updated the public instance attribute update_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert to dictionary"""
        dicc = dict(self.__dict__)
        dicc['__class__'] = self.__class__.__name__
        dicc['updated_at'] = dicc['updated_at'].isoformat()
        dicc['created_at'] = dicc['created_at'].isoformat()
        return dicc
