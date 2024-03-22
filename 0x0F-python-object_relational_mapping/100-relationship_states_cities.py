#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa
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

    # Create State "California" with City "San Francisco"
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)
    
    session.add(california)
    session.add(san_francisco)
    session.commit()

    print(california.id)

    # Close session
    session.close()
