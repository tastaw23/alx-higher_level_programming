#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Collect command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Prepare SQL query to retrieve cities of the given state
    query = """SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
               FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id ASC"""

    # Execute the query with state_name as parameter
    cursor.execute(query, (state_name,))

    # Fetch the result
    result = cursor.fetchone()[0]

    # Print result or "Not found" if no cities found for the state
    if result:
        print(result)
    else:
        print("Not found")

    # Close cursor and database connection
    cursor.close()
    db.close()
