#!/usr/bin/python3
"""testing storage"""
import unittest
from models import storage
from models.engine.file_storage import FileStorage


class StorageTest(unittest.TestCase):
    """testing class"""
    def setUp(self):
        """setting"""
        self.inst = FileStorage()
        self.objs = FileStorage.__objects

    def test_all(self):
        """teat all"""
        dic = self.inst.all()
        self.assertEqual(dic, self.objs)
        self.assertEqual(type(self.inst.all()), type({}))

    def test_save(self):
        """test saving method"""
        with open(self.inst.__file_path, 'r') as f:
            a = f.read()
        self.assertEqual(type(a), type(""))


if __name__ == '__main__':
    unittest.main()
