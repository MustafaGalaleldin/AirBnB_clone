#!/usr/bin/python3
"""state City model"""
from models.base_model import BaseModel
from models import storage


class City(BaseModel):
    """City class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(*args, **kwargs)
