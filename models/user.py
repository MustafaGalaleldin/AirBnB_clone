#!/usr/bin/python3
"""class user inherits from BaseModel"""
from models.base_model import BaseModel
from models import storage


class User(BaseModel):
    """users class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """consrtructor"""
        super().__init__(*args, **kwargs)
        


