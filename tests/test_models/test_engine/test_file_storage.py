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

    def test_new_work(self):
        """test new mth"""
        old = len(self.inst.all())
        new1_inst = BaseModel()
        storage.new(new1_inst)
        new = len(self.inst.all())
        self.assertNotEqual(old, new)

    def test_new(self):
        """ww"""
        aa = BaseModel()
        bb = User()
        cc = Place()
        dd = Review()
        ee = State()
        ff = City()
        gg = Amenity()
        storage.new(aa)
        storage.new(bb)
        storage.new(cc)
        storage.new(dd)
        storage.new(ee)
        storage.new(ff)
        storage.new(gg)
        storage.save()
        storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + aa.id, objs)
        self.assertIn("User." + bb.id, objs)
        self.assertIn("State." + ee.id, objs)
        self.assertIn("Place." + cc.id, objs)
        self.assertIn("City." + ff.id, objs)
        self.assertIn("Amenity." + gg.id, objs)
        self.assertIn("Review." + dd.id, objs)

    def test_save(self):
        """test saving method"""
        with open('file.json', 'r') as f:
            a = f.read()
        self.assertEqual(type(a), type(""))
        with self.assertRaises(TypeError):
            storage.save(None)
        aa = BaseModel()
        bb = User()
        cc = Place()
        dd = Review()
        ee = State()
        ff = City()
        gg = Amenity()
        storage.new(aa)
        storage.new(bb)
        storage.new(cc)
        storage.new(dd)
        storage.new(ee)
        storage.new(ff)
        storage.new(gg)
        storage.save()
        storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + aa.id, objs)
        self.assertIn("User." + bb.id, objs)
        self.assertIn("State." + ee.id, objs)
        self.assertIn("Place." + cc.id, objs)
        self.assertIn("City." + ff.id, objs)
        self.assertIn("Amenity." + gg.id, objs)
        self.assertIn("Review." + dd.id, objs)

    def test_reload(self):
        """test reload"""
        with self.assertRaises(TypeError):
            storage.reload(None)
        aa = BaseModel()
        bb = User()
        cc = Place()
        dd = Review()
        ee = State()
        ff = City()
        gg = Amenity()
        storage.new(aa)
        storage.new(bb)
        storage.new(cc)
        storage.new(dd)
        storage.new(ee)
        storage.new(ff)
        storage.new(gg)
        storage.save()
        storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + aa.id, objs)
        self.assertIn("User." + bb.id, objs)
        self.assertIn("State." + ee.id, objs)
        self.assertIn("Place." + cc.id, objs)
        self.assertIn("City." + ff.id, objs)
        self.assertIn("Amenity." + gg.id, objs)
        self.assertIn("Review." + dd.id, objs)


if __name__ == '__main__':
    unittest.main()
