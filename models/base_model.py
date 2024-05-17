#!/usr/bin/python3
""" the class model """
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """ the basemodel """
    def __init__(self, *args, **kwargs):
        """ constructor """
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k == "updated_at" or k == "created_at":
                    setattr(self, k, datetime.fromisoformat(kwargs[k]))
                else:
                    setattr(self, k, kwargs[k])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        storage.new(self)

    def __str__(self):
        """ print:[<class name>] (<self.id>) <self.__dict__> """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the updated_at with the current datetime """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all k/v of __dict__ instance """
        ret_dict = {'__class__': self.__class__.__name__}
        for k, v in self.__dict__.items():
            if type(v) is datetime:
                ret_dict[k] = v.isoformat()
            else:
                ret_dict[k] = v
        return ret_dict
