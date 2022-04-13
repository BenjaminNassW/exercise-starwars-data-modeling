import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250))
    gender = Column(String(250))
    homeworld = Column(String(250))
    user = relationship(User)


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    location_name = Column(String(250), ForeignKey(
        'character.homeworld'))
    terrain = Column(String(250))
    population = Column(Integer())
    character = relationship(Character)
    user = relationship(User)


class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    starship_name = Column(String(250))
    crew = Column(Integer())
    model = Column(String(250))
    user = relationship(User)


class Fav_C(Base):
    __tablename__ = 'fav_c'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), ForeignKey('user.name'))
    character_name = Column(
        String(250), ForeignKey('character.character_name'))
    user = relationship(User)
    character = relationship(Character)


class Fav_L(Base):
    __tablename__ = 'fav_l'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), ForeignKey('user.name'))
    character_name = Column(
        String(250), ForeignKey('location.location_name'))
    user = relationship(User)
    location = relationship(Location)


class Fav_S(Base):
    __tablename__ = 'fav_s'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), ForeignKey('user.name'))
    character_name = Column(
        String(250), ForeignKey('starship.starship_name'))
    user = relationship(User)
    starship = relationship(Starship)

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
