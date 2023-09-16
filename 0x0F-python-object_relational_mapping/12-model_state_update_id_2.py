#!/usr/bin/python3
"""
parameters given to script: username, password, database
Start link class to table in database
update state: given id, change state name
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
    updateState = session.query(State).filter_by(id=2).first()

    if updateState:
        updateState.name = 'New Mexico'
        session.commit()
    session.close()
