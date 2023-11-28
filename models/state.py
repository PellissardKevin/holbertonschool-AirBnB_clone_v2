#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    # Add condition if storage is db or not
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete", backref="state",
                              passive_deletes=True)
    else:
        @property
        def cities(self):
            """Return the list of City instances with state_id
            equals to the current State.id"""
            state_cities = []
            from models import storage
            all_cities = storage.all(City)
            state_cities = [city for city in all_cities.values()
                            if city.state_id == self.id]
            return state_cities
