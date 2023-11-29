#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    name = Column(String(128), nullable=False)

    place_amenities = relationship("Place", secondary="place_amenity", back_populates="amenities")