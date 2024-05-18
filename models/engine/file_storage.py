#!/usr/bin/python3
""" storage module """
import json


class FileStorage:
    """
    serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        obj_dic = {}
        for k, v in self.__objects.items():
            obj_dic[k] = v.to_dict()
        with open(self.__file_path, "w") as f:
            f.write(json.dumps(obj_dic))

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file exists
        otherwise, do nothing. If the file does not exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r') as f:
                demo__objects = json.loads(f.read())

            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review

            for k, v in demo__objects.items():
                cls_name, cls_id = k.split('.')
                temp_obj = eval(cls_name)(**v)
                self.__objects[k] = temp_obj
        except Exception:
            pass
