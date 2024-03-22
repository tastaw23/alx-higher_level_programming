#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Collect command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create connection URL
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(mysql_username, mysql_password, database_name)

    # Create engine
    engine = create_engine(db_url)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects
    states = session.query(State).order_by(State.id).all()

    # Loop through each State
    for state in states:
        print("{}: {}".format(state.id, state.name))
        
        # Loop through each City in the state
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    # Close session
    session.close()
