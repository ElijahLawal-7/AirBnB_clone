#!/usr/python3
from models.base_model import BaseModel
"""Class inherence from BaseModel"""


class Review(BaseModel):
    """Class for reviews"""
    place_id = ""
    user_id = ""
    text = ""
