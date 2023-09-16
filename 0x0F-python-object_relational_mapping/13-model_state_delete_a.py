#!/usr/bin/python3
"""
delete from table states with names containing letter 'a'
Start link class to table in database
parameters given to script: username, password, database
"""

from sqlalchemy import create_engine, select, insert
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    deleteStates = session.query(State).filter(State.name.like(f'%a%')).all()

    if deleteStates:

        for state in deleteStates:
            session.delete(state)
        session.commit()

    session.close()
