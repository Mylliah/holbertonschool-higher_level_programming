#!/usr/bin/env python3
"""
Lists all states from the database hbtn_0e_0_usa.
Connects to a MySQL server using MySQLdb and fetches all rows
from the 'states' table sorted by ascending id.
"""

import MySQLdb
import sys


def list_states():
    """
    Connects to the database using credentials from command-line arguments
    and lists all states in ascending order by id.
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
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    list_states()
