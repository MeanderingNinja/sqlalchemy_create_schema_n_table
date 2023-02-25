# Creating a schema and a table in a Postgres Database Using SQLAlchemy

## 1. Define your model class in `model.py`. Here's an example:

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# We need to inherit Base in order to register models with SQA. Without this, SQA wouldn't know anything about our models.
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
```

In this example, we define a model class `User` that inherits from `Base`, the declarative base class provided by SQLAlchemy. The class has three columns: `id`, `username`, and `password`, each defined using `Column`.

## 2. Create an engine to connect to your database. Here's an example:

```python
from sqlalchemy import create_engine
engine = create_engine('postgresql://user:password@host:port/database')
```

In this example, we create a PostgreSQL engine using the `create_engine()` function.

## 3. Check if the schema already exists. You can construct a SQL query to check. Here's an example:
```python
# text() method of SQLAlchemy converts the string into a TextClause object that can be executed using the execute() method of a database engine.
schema_exists_query = text(f"SELECT EXISTS(SELECT SCHEMA_NAME FROM information_schema.schemata WHERE SCHEMA_NAME = '{schema_name}')")
# More expplanation needed here 20230224
result = engine.execute(schema_exists_query).fetchone()
schema_exists = result[0]

# create schema if it doesn't exist
if not schema_exists:
    print("Creating the schema...")
    create_schema_query = text(f'CREATE SCHEMA {schema_name};')
    engine.execute(create_schema_query)
else:
    print(f"The schema {schema_name} already created!")
```

## 4. Check if the table already exists. You can use the `has_table()` method of the engine's dialect object to check if the table already exists. Here's an example:

```python
from model import Base, User, SCHEMA_NAME, TABLE_NAME

# create a connection from the engine
conn = engine.connect()

if not engine.dialect.has_table(conn, table_name):
    # create the table if it doesn't exist
    Base.metadata.create_all(engine)
```

In this example, we check if the table named `users` already exists in the database using `has_table()`. If it does not exist, we can safely create it using `Base.metadata.create_all(engine)`.

## 4. Create a session to interact with the database. Here's an example:

```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
```

In this example, we create a `Session` object using the `sessionmaker()` function and bind it to the engine object we created earlier. We then create a session object by calling `Session()`.

## 5. Use the session to interact with the database. Here's an example:

```python
# create a new user
new_user = User(username='john_doe', password='secret')
session.add(new_user)
session.commit()

# query the database for all users
users = session.query(User).all()
for user in users:
    print(user.id, user.username, user.password)
```

In this example, we create a new `User` object with a username and password, add it to the session using `session.add()`, and commit the changes to the database using `session.commit()`. We then query the database for all `User` objects using `session.query(User).all()`, and print the results.

That's it! By following these steps, you can use a SQL query string and `create_all()` function along with data model to creat a schema and to create a table in a database respectively. Note that if you have made changes to the table schema (e.g., by adding or modifying columns), you will need to use a migration tool like Alembic to update the existing table schema instead of simply recreating the table.

