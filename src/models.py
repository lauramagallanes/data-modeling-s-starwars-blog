import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)

class Planeta(Base):
    __tablename__ = 'planetas'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)

class Personaje(Base):
    __tablename__ = 'personajes'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)

class Vehiculo(Base):
    __tablename__ = 'vehiculos'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    manufacturer = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    max_atmospheric_speed = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)

class Favorito(Base):
    __tablename__ = 'favoritos'
    
    id = Column(Integer, primary_key=True)
    usuarios_id = Column(Integer, ForeignKey("usuarios.id"))
    usuarios = relationship(Usuario)
    planetas_id = Column(Integer, ForeignKey("planetas.id"))
    planetas = relationship(Planeta)
    personajes_id = Column(Integer, ForeignKey("personajes.id"))
    personajes = relationship(Personaje)
    vehiculos_id = Column(Integer, ForeignKey("vehiculos.id"))
    vehiculos = relationship(Vehiculo)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')