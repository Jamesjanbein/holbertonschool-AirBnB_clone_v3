#!/usr/bin/python3
"""
Review Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class Review(BaseModel, Base):
    """Review class handles all application reviews"""
    if storage_type == "db":
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ''
        user_id = ''
        text = ''

    if storage_type != "db":
        @property
        def place_id(self):
            """
            sets place_id
            :return: place_id
            """
            return self.place_id

        @place_id.setter
        def place_id(self, place_id):
            """
            sets place_id
            :param place_id: place id review belongs to
            """
            self.place_id = place_id
