#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__="Cities"
    name = Column(String(128), nullable=False)
    # delete relationneship and add ondelete on ForeignKey
    state_id = Column(String(60), ForeignKey('states.id', ondelete="CASCADE"),
                        nullable=False, )
