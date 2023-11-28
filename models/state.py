#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from city import City

class State(BaseModel):
    """ State class """
    __tablename__="States"
    name = Column(String(128), nullable=False)
    cities_relation = relationship('City', back_populates='state', cascade='all, delete-orphan')

    @property
    def cities(self):
        """Return the list of City instances with state_id equals to the current State.id"""
        from models import storage
        all_cities = storage.all(City)
        state_cities = [city for city in all_cities.values() if city.state_id == self.id]

        return state_cities