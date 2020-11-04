#!/usr/bin/python3
import sys
import unittest
import pep8
from models.state import State


class Test_StateModel(unittest.TestCase):
    """test the State model"""

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        user_path = 'models/state.py'
        result = pepstylecode.check_files([user_path])

    def setUp(self):
        self.model_test = State()
        self.model_test.save()

    def test_StateInstantiation(self):
        """testing"""
        self.assertIsInstance(self.model_test, State)
        self.assertTrue(hasattr(self.model_test, "state_id"))
        self.assertTrue(hasattr(self.model_test, "name"))
        self.assertEqual(self.model_test.state_id, "")
        self.assertEqual(self.model_test.name, "")

if __name__ == '__main__':
    sys.path.append("../..")
    unittest.main()
