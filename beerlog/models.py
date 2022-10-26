# Using sqlmodel module and SQLModel model and Field function
# SQLModel is a simple ORM . Docs: https://sqlmodel.tiangolo.com/
from sqlmodel import SQLModel, Field
# Using select function from ORM
# from sqlmodel import select
# Using typing module to set id as optional when creating an object
from typing import Optional
# Importing Pydantic library to use validator function
from pydantic import validator 


# Inherit SQLModel class and set table as true to create a new database table
class Beer(SQLModel, table=True):
    # Defining an optional id as primary key (and without default) using Field
    id: Optional[int] = Field(primary_key=True, default=None)
    name: str
    style: str
    flavor: int
    image: int 
    cost: int

    # Method to validate ratings and raising exception
    # @validator decorator is injecting code on function and telling all attributes to validate
    @validator("flavor", "image", "cost")
    def validate_ratings(cls, v, field):    
        if v < 1 or v > 10:
            # Raise is like throw new. TODO: what does f means?
            raise RuntimeError(f"{field.name} must be between 1 and 10.")
        return v    # Returning value as v


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
try:
    first_beer = Beer(name="Brahma", style="Pilsen", flavor=8, image=2, cost=9)
except RuntimeError:
    print("Validation Error!")