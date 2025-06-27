#!/usr/bin/python3
"""
Defines the State class for SQLAlchemy ORM mapping.
Represents a row in the 'states' MySQL table.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    State class mapped to the 'states' table in MySQL.
    Attributes:
        id (int): Primary key, auto-incremented, not null
        name (str): Max 128 characters, not null
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
