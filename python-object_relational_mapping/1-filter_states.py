#!/usr/bin/env python3
"""
Lists all states with a name starting with 'N' from the database hbtn_0e_0_usa.
Uses MySQLdb to connect to MySQL and filter the results.
"""

import MySQLdb
import sys


def list_states_starting_with_N():
    """
    Connects to MySQL and prints states whose names start with 'N'.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states "
        "WHERE name LIKE BINARY 'N%' "
        "ORDER BY id ASC"
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    list_states_starting_with_N()
