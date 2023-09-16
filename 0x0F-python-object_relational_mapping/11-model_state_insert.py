#!/usr/bin/python3
"""
parameters given to script: username, password, database
Start link class to table in database
update state: given id, change state name
"""
from sqlalchemy import create_engine, select, insert
import sys
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    with engine.connect() as connection:
        transaction = connection.begin()
        query = insert(State).values(name="Louisiana")
        connection.execute(query)
        query = select(State).where(State.name == "Louisiana")
        state = connection.execute(query).fetchone()
        if state:
            print(state.id)
        transaction.commit()

    engine.dispose()
