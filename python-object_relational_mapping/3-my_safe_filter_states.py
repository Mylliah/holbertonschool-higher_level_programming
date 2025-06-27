#!/usr/bin/env python3
"""
Safely lists all states from the database hbtn_0e_0_usa
that match a given name (avoids SQL injection).
"""

import MySQLdb
import sys


def safe_search_state():
    """
    Connects to the database and prints matching states by name
    (exact match, safe from SQL injection).
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

    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC",
        (state_name,)
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    safe_search_state()
