#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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

    # Query State objects containing letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # Delete State objects containing letter 'a'
    for state in states_with_a:
        session.delete(state)

    # Commit the changes
    session.commit()

    # Close session
    session.close()
