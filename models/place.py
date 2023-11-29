#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from sqlalchemy import *
from amenity import Amenity

metadata = MetaData()

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__= "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0) 
    number_bathrooms = Column(Integer, nullable=False, default=0) 
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    user = relationship('User', back_populates='places')
    city = relationship('City', back_populates='places')

    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary="place_amenity", back_populates="place_amenities", viewonly=False)

    amenity_ids = []

    @property
    def amenities(self):
        """Getter attribute"""
        return self.amenity_ids

    @amenities.setter
    def amenities(self, amenity):
        """Setter attribute"""
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity.id)
