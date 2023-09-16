#!/usr/bin/python3
"""
parameters given to script: username, password, database
return state objects containing letter 'a' from database via python
*****
"""

from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":

    # create engine for database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # check python instance in database for letter 'a'

    for state in session.query(State).filter(
            State.name.like('%a%')).order_by(State.id):
        print("{:d}: {:s}".format(state.id, state.name))

    session.close()
