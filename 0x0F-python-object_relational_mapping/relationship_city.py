#!/usr/bin/python3
"""A file that contains the class definition of a City"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, ForeignKey
from relationship_state import Base
from sqlalchemy.orm import relationship

class City(Base):
    """
    inherits from Base (imported from model_state)
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", backref='city')
    