#!/usr/bin/python3
"""[Documentation Class]"""
import json
import models
from models.base_model import BaseModel


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """[instance method]

        Returns:
            [dictionary]: [objects]
        """
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        for key, value in self.__objects.items():
            if not isinstance(value, dict):
                self.__objects[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as file:
                serializable_file = json.load(file)
            for key, value in serializable_file.items():
                self.__objects[key] = eval(value['__class__'])(**value)

        except FileNotFoundError:
            pass
