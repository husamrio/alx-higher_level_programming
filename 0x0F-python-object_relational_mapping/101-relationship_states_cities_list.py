#!/usr/bin/python3
"""
parameters given to script: username, password, database
use table relationship to access and print city and state
*****
"""

from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":

    # Create engine for database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # utilise the table relationship to access and print city and state

    rows = session.query(State).order_by(State.id).all()
    for state in rows:

        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()
