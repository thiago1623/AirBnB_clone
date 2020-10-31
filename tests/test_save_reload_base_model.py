#!/usr/bin/python3
"""TEST"""
import sys
__import__("sys").path.append("..")
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.engine.file_storage import FileStorage.all

all_objs = FileStorage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)
print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
my_model.save()
print(my_model)
