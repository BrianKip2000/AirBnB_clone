#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """Class for review"""
    place_id = ''
    user_id = ''
    text = ''

