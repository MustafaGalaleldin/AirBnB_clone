#!/usr/bin/python3
"""state class model"""
from models.base_model import BaseModel
from models import storage


class State(BaseModel):
    """State class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(*args, **kwargs)
