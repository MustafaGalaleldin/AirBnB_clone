#!/usr/bin/python3
"""testing storage"""
import unittest
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class StorageTest(unittest.TestCase):
    """testing class"""
    def setUp(self):
        """setting"""
        self.inst = FileStorage()

    def test_all(self):
        """teat all"""
        dic = self.inst.all()
        self.assertEqual(type(dic), dict)

    def test_new(self):
        """test new mth"""
        old = len(self.inst.all())
        new1_inst = BaseModel()
        storage.new(new1_inst)
        new = len(self.inst.all())
        self.assertNotEqual(old, new)

    def test_save(self):
        """test saving method"""
        with open('file.json', 'r') as f:
            a = f.read()
        self.assertEqual(type(a), type(""))
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload(self):
        """test reload"""
        with self.assertRaises(TypeError):
            storage.reload(None)


if __name__ == '__main__':
    unittest.main()
