#!/usr/bin/python3
"""
This script takes in an argument and 
displays all values in the states
where 'name' matches the argument
from the database 'hbtn_0e_0_usa'
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """

    db = MySQLdb.connect(host="localhost",user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = '{:s}'"
                .format(sys.argv[4])+"ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()