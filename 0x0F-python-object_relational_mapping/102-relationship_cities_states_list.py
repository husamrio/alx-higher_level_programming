#!/usr/bin/python3
"""
parameters given to script: username, password, database
*****
use table relationship to access and print city and state
"""

from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import Base, State


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

    # Utilize the table relationship to access and print city and state

    rows = session.query(City).order_by(City.id).all()
    for city in rows:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
