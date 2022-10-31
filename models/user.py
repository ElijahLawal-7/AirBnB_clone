#!/usr/bin/python3
"""The User Model Class"""
from models.base_model import BaseModel


class User(BaseModel):
    """The User Class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
