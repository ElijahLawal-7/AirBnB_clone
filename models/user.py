#!/usr/python3
from models.base_model import BaseModel
"""Class inherence from BaseModel"""


class User(BaseModel):
    """Class for users"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
