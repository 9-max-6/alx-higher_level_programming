#!/usr/bin/python3
"""
A module containing the class definition of a state and and instance
of Base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """class state that inherits from Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128))
    cities = relationship(
        "City", backref="state", cascade="delete-orphan"
        )
