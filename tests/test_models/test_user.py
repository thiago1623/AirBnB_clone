#!/usr/bin/python3
import sys
import unittest
import pep8
from models.user import User


class Test_UserModel(unittest.TestCase):
    """
    [Test the user model class]
    """

    def testpep8(self):
        """ [testing codestyle] """
        pepstylecode = pep8.StyleGuide(quiet=True)
        user_path = 'models/user.py'
        result = pepstylecode.check_files([user_path])

    def setUp(self):
        self.model = User()
        self.model.save()

    def test_UserInstantiation(self):
        self.assertTrue(hasattr(self.model, "email"))
        self.assertTrue(hasattr(self.model, "password"))
        self.assertTrue(hasattr(self.model, "first_name"))
        self.assertTrue(hasattr(self.model, "last_name"))
        self.assertEqual(self.model.email, "")
        self.assertEqual(self.model.password, "")
        self.assertEqual(self.model.first_name, "")
        self.assertEqual(self.model.last_name, "")


if __name__ == "__main__":
    unittest.main()
