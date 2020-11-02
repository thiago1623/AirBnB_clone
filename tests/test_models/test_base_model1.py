#!/usr/bin/python3
import sys
import unittest
sys.path.append("../..")
from datetime import datetime
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """
    Test the base model class
    """

    def setUp(self):
        self.name_class = BaseModel()

        test_args = {'created_at': datetime.now(),
                     'updated_at': datetime.now(),
                     'id': 'dc429c3c-eb20-478d-bd53-3b5c34fbff82',
                     'name': 'model1'}
        self.edge_case = BaseModel(test_args)
        self.edge_case.save()

    def test_instantiation(self):
        self.assertIsInstance(self.name_class, BaseModel)
        self.assertTrue(hasattr(self.name_class, "created_at"))
        self.assertTrue(hasattr(self.name_class, "id"))
        self.assertTrue(hasattr(self.name_class, "updated_at"))

    def test_reinstantiation(self):
        self.assertIsInstance(self.edge_case, BaseModel)
        self.assertNotEqual(self.edge_case.id,
                         'dc429c3c-eb20-478d-bd53-3b5c34fbff82')
        self.assertNotEqual(self.edge_case.created_at,
                         datetime.now())

    def test_save(self):
        self.assertTrue(hasattr(self.name_class, "updated_at"))
        self.name_class.save()
        self.assertTrue(hasattr(self.name_class, "updated_at"))
        old_time = self.edge_case.updated_at
        self.edge_case.save()
        self.assertNotEqual(old_time, self.edge_case.updated_at)

    def test_to_json(self):
        json_file = self.edge_case.to_dict()
        self.assertNotEqual(self.edge_case.__dict__, json_file)
        self.assertNotIsInstance(json_file["created_at"], datetime)
        self.assertNotIsInstance(json_file["updated_at"], datetime)
        self.assertNotEqual(json_file["created_at"], datetime.now())
        self.assertTrue(hasattr(json_file, "__class__"))
        self.assertEqual(json_file["__class__"], "BaseModel")

if __name__ == "__main__":
    unittest.main()
