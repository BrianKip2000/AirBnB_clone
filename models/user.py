#!/usr/bin/python3
from  models.base_model import BaseModel


class User(BaseModel):
    """inherits from BaseModel: For users in airbnb"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

