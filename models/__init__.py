#!/usr/bin/python3
''' init documentation'''
from models.engine import file_storage
from models.base_model import BaseModel

storage = file_storage.FileStorage()
storage.reload()
