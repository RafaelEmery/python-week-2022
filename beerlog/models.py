# Using sqlmodel module and SQLModel model and Field function
# SQLModel is a simple ORM . Docs: https://sqlmodel.tiangolo.com/
from sqlmodel import SQLModel, Field
# Using select function from ORM
# from sqlmodel import select
# Using typing module to set id as optional when creating an object
from typing import Optional
# Importing Pydantic library to use validator function
from pydantic import validator 
from statistics import mean
from datetime import datetime


# Inherit SQLModel class and set table as true to create a new database table
class Beer(SQLModel, table=True):
    # Defining an optional id as primary key (and without default) using Field
    id: Optional[int] = Field(primary_key=True, default=None)
    name: str
    style: str
    flavor: int
    image: int 
    cost: int
    rate: int = 0
    # Defining a default date attribute as now datetime
    date: datetime = Field(default_factory=datetime.now)

    # Method to validate ratings and raising exception
    # @validator decorator is injecting code on function and telling all attributes to validate
    @validator("flavor", "image", "cost")
    def validate_ratings(cls, v, field):   
        # 3 fields here. Example field: name='flavor' type=int required=True
        if v < 1 or v > 10:
            # Raise is like throw new.
            # TODO: what does f means on print arguments?
            raise RuntimeError(f"{field.name} must be between 1 and 10.")
        return v    # Returning value as v

    # The param always=True means that this method will always execute 
    @validator("rate", always=True)
    def calculate_rate(cls, v, values):
        # values dictionary: 
        # {'id': None, 'name': 'Brahma', 'style': 'Pilsen', 'flavor': 8, 'image': 2, 'cost': 9}
        rate = mean([values["flavor"], values["image"], values["cost"]])
        return int(rate)


# Creating an instance from model Beer
# Using python -i beerlog/models.py:
# print(select(Beer)) returns the select SQL query
# SELECT beer.id, beer.name, beer.style, beer.flavor, beer.image, beer.cost FROM beer
# Which means that beer is a table on database.
# Other query example: select(Beer).where(Beer.name == "Brahma")
# It uses SQLAlchemy and Pydentic behind the scenes
# (https://www.sqlalchemy.org/ and https://pydantic-docs.helpmanual.io/). 
# So SQLModel is an abstraction of SQLAlchemy and Pydentic, table from SQLAlchemy and a Pydent Model

# We can do a try catch with the validation error
# try:
#     first_beer = Beer(name="Brahma", style="Pilsen", flavor=8, image=2, cost=9)

#     print("\nBrahma beer:")
#     print(first_beer)
# except RuntimeError:
#     print("Validation Error!")