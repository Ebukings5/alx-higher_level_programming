#!/usr/bin/python3
"""Lists states from database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__name__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM 
            cities INNER JOIN states ON states.id=cities.states.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
