#!/usr/bin/python3
import sys
import unittest
sys.path.append("../..")
from models.state import State


class Test_StateModel(unittest.TestCase):
    """test the State model"""

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
    unittest.main()
