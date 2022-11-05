from sqlmodel import create_engine
# The settings object is defined at config.py
# Uses Dynaconf lib to manage general config
from beerlog.config import settings
from beerlog import models 

# Creating a sqlite connection
engine = create_engine(settings.database.url)

# This method basically returns the SQL DDL (data def language)
# It creates all tables from the models defined
models.SQLModel.metadata.create_all(engine)

# Executing python beerlog/database.py a beerlog.db file is created