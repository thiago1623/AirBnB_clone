#!/usr/bin/python3
import sys
__import__("sys").path.append("..")


if __name__ == '__main__':
    from models import storage
    from models.base_model import BaseModel

    all_objs = storage.all()
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
