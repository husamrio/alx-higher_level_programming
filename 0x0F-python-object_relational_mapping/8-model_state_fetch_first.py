#!/usr/bin/python3
"""
parameters given to script: username, password, database
return first state object from database via python
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

    # check first python instance in database
    first_instance = session.query(State).order_by(State.id).first()

    if first_instance:
        print("{:d}: {:s}".format(first_instance.id, first_instance.name))

    else:
        print("Nothing")

    session.close()
