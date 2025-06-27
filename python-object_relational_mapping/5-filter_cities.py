#!/usr/bin/env python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa,
safe from SQL injection.
"""

import MySQLdb
import sys


def list_cities_of_state():
    """
    Connects to the DB and lists all cities of the state given in argument.
    Results are displayed as a single comma-separated line.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    """
    cur.execute(query, (state_name,))

    cities = [row[0] for row in cur.fetchall()]

    print(", ".join(cities))

    cur.close()
    db.close()


if __name__ == "__main__":
    list_cities_of_state()
