#!/usr/bin/python3
"""Review class model"""
from models.base_model import BaseModel
from models import storage


class Review(BaseModel):
    """Review class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(*args, **kwargs)
