#!/usr/bin/python3
import sys
import unittest
import pep8
from models.review import Review


class Test_ReviewModel(unittest.TestCase):
    """
    Test the review model class
    """

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        user_path = 'models/review.py'
        result = pepstylecode.check_files([user_path])

    def setUp(self):
        self.model = Review()
        self.model.save()

    def test_ReviewInstantiation(self):
        self.assertTrue(hasattr(self.model, "place_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "text"))
        self.assertEqual(self.model.place_id, "")
        self.assertEqual(self.model.user_id, "")
        self.assertEqual(self.model.text, "")


if __name__ == "__main__":
    sys.path.append("../..")
    unittest.main()
