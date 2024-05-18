#!/usr/bin/python3
"""state Amenity model"""
from models.base_model import BaseModel
from models import storage


class Amenity(BaseModel):
    """Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(*args, **kwargs)
