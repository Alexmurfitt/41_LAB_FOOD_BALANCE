from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Child(Base):
    __tablename__ = 'children'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Float)
    sex = Column(String)
    weight = Column(Float)
    height = Column(Float)

class NutritionalRequirement(Base):
    __tablename__ = 'nutritional_requirements'
    id = Column(Integer, primary_key=True)
    nutrient = Column(String)
    unit = Column(String)
    value = Column(Float)

class Food(Base):
    __tablename__ = 'foods'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    group = Column(String)
    kcal = Column(Float)
    protein = Column(Float)
    fat = Column(Float)
    carbs = Column(Float)
    fiber = Column(Float)
    iron = Column(Float)
    calcium = Column(Float)
    vitamin_c = Column(Float)
    vitamin_d = Column(Float)
    # Añadir más nutrientes clave...

class MealRecord(Base):
    __tablename__ = 'meal_records'
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey('children.id'))
    date = Column(Date)
    meal_type = Column(String)  # desayuno, merienda, almuerzo, cena
    food_id = Column(Integer, ForeignKey('foods.id'))
    quantity_g = Column(Float)
