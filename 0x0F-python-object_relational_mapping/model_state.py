#!/usr/bin/python3
"""Defines the State class"""

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Instance of the declarative base
Base = declarative_base()

# State class definition
class State(Base):
    """Class representing a state"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return "<State(id='%s', name='%s')>" % (self.id, self.name)
