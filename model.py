from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

SCHEMA_NAME = "my_schema"
TABLE_NAME = "users"

# Import the base class our models inherit from
# Without this, SQLAlchemy wouldn't know anything about our models.
# When you define models in SQLAlchemy, the Base object automatically 
# generates a metadata object that reflects the structure of your models.
Base = declarative_base()

class User(Base):
    __tablename__ = TABLE_NAME
    __table_args__ = {'schema': SCHEMA_NAME} # specify the schema name

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

