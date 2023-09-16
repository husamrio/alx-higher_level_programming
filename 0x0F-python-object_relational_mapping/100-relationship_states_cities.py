#!/usr/bin/python3
"""
parameters given to script: username, password, database
*****
create state "California" with city attribute "San Francisco"
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

    # Initialize state "California" with city attribute "San Francisco"

    new_s = State(name="California")
    new_c = City(name="San Francisco")
    new_s.cities.append(new_c)

    session.add(new_s)
    session.add(new_c)

    session.commit()
    session.close()
