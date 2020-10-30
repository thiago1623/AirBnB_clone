#!/usr/bin/python3
''' Principal class'''
import uuid
from datetime import datetime


class BaseModel:
    """ Generate random ID"""

    def __init__(self):
        """Contructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = datetime.now()

    def __str__(self):
        """toString"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updated the public instance attribute update_at"""
        self.update_at = datetime.now()

    def to_dict(self):
        """Convert to dictionary"""
        dicc = dict(self.__dict__)
        dicc['__class__'] = self.__class__.__name__
        dicc['updated_at'] = dicc['updated_at'].isoformat()
        dicc['created_at'] = dicc['created_at'].isoformat()
        return dicc

    """Date time"""
    # moon_time = "2017-06-14T22:31:03.285259"
    # dtae = datetime.strptime(moon_time, "%Y-%m-%dT%H:%M:%S.%f")
    # print(dtae)
    # print(type(dtae))
