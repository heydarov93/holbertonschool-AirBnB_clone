#!/usr/bin/python3
"""
This is a 'user' module that contains User class
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User that inherits from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
