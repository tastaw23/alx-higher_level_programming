#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa
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

    # Query State object with id=2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Change the name of the State object to "New Mexico"
    state_to_update.name = "New Mexico"

    # Commit the change
    session.commit()

    # Close session
    session.close()
