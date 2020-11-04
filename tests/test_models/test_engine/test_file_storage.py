#!/usr/bin/python3
"""File Storage unittest"""

import unittest
import pep8
import models
import re
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """[unittest]"""

    def testpep8(self):
        """ [testing codestyle] """
        pepstylecode = pep8.StyleGuide(quiet=True)
        user_path = 'models/engine/file_storage.py'
        result = pepstylecode.check_files([user_path])

    def test_createAttr_noArgs(self):
        """[create Instance User]"""
        my_model = User()
        my_model.first_name = "FirstName"
        my_model.last_name = "LastName"
        my_model.email = "email@test.com"
        self.storage = FileStorage()

    def test_all(self):
        """[Test all File Storage Functions]"""
        storage = FileStorage()
        my_model = storage.all()
        self.assertIsNotNone(my_model)
        self.assertEqual(type(my_model), dict)
        self.assertIs(my_model, storage._FileStorage__objects)

    def teardown(cls):
        """ Deletes instance after test """
        del cls.user

    def tearDown(self):
        """ Deletes file after test """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_new(self):
        """[Test new file storage functions]"""
        storage = FileStorage()
        my_model = storage.all()
        user = User()
        user.id = 12345
        user.name = "Name"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(my_model[key])
