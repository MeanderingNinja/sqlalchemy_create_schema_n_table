from sqlalchemy import create_engine, text
from model import Base, User, SCHEMA_NAME, TABLE_NAME
from sqlalchemy.orm import sessionmaker


def create_schema_if_not_exist(engine, schema_name):
    schema_exists_query = text(f"SELECT EXISTS(SELECT SCHEMA_NAME FROM information_schema.schemata WHERE SCHEMA_NAME = '{schema_name}')")
    result = engine.execute(schema_exists_query).fetchone()
    schema_exists = result[0]

    # create schema if it doesn't exist
    if not schema_exists:
        print("Creating the schema...")
        create_schema_query = text(f'CREATE SCHEMA {schema_name};')
        engine.execute(create_schema_query)
    else:        print(f"The schema {schema_name} already created!")

def create_table_if_not_exist(engine, table_name):
    # create a connection from the engine
    conn = engine.connect()
    if not engine.dialect.has_table(conn, TABLE_NAME):
        # create the table if it doesn't exist
        print("Creating users table")
        Base.metadata.create_all(engine)
    else:
        print("Table already created!")

def add_table_object_and_check(engine, object):

    # create a Session factory bound to the engine
    Session = sessionmaker(bind=engine)

    with Session() as session:
        session.add(new_user)
        session.commit()
        # query the database for all users
        users = session.query(User).all()
        for user in users:
            print(user.id, user.username, user.password)


engine = create_engine('postgresql://pa-test:pa-test@192.168.1.157:5432/pa-test') 
create_schema_if_not_exist(engine, SCHEMA_NAME)
create_table_if_not_exist(engine, TABLE_NAME)

# create a new user
new_user = User(username='john_doe', password='secret')

add_table_object_and_check(engine, new_user)











