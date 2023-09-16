#!/usr/bin/python3
"""
Defines
Class City
*****
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()


class City(Base):
    """
     Linked to MySQL table "city"
    Class City; instance of Base
   *****
    """
    __tablename__ = "cities"

    id = Column(Integer, nullable=False, primary_key=True)
    #  autoincrements
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
