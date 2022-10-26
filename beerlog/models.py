# Importing a dataclass function of dataclasses module to start modeling data
# The dataclass function allow us to define objects as dataclasses
# It's an easy way to persist data on Python 3
# More info: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass

# Defining a "simple" Beer model
# The dataclass function is the function that transform Beer into a dataclass
# It implements all special methods and uses the Decorator Pattern
@dataclass
class Beer:
    name: str
    style: str
    flavor: int
    image: int 
    cost: int

# Creating an instance from model Beer
first_beer = Beer(name="Brahma", style="Pilsen", flavor=8, image=2, cost=9)

# using python -i models.py:

# dir(first_beer), we'll have the list 
# ['__annotations__', '__class__', '__dataclass_fields__', '__dataclass_params__', '__delattr__', 
# '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
#  '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
#  '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
# '__weakref__', 'cost', 'flavor', 'image', 'name', 'style']
# The dunder attributes represents the dataclass attributes

# By object.attribute_name we can have the value (ex.: first_beer.name)
