#!/usr/bin/python3
"""
parameters given to script: username, password, database, state name to match
Start link class to table in database
return state id given state name; SQL injection free
"""

from sqlalchemy import create_engine, select, text, bindparam
import sys
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    state_name = sys.argv[4]
    with engine.connect() as connection:
        query = select(State).where(State.name == state_name)
        states = connection.execute(query).first()
        if states:
            print(states.id)
        else:
            print("Not found")

    engine.dispose()
