#!/usr/bin/python3
""" testing """
import unittest
from models.base_model import BaseModel


class Base_test(unittest.TestCase):
    """ testing base model """
    def setUp(self):
        """set"""
        self.inst = BaseModel()

    def test_str(self):
        """return string"""
        self.assertEqual(type(self.inst.__str__()), type(""))

    def test_to_dict(self):
        """test saving method"""
        self.assertEqual(type(self.inst.to_dict()), type({}))


if __name__ == '__main__':
    unittest.main()
