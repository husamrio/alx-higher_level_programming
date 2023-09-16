#!/usr/bin/python3
"""
parameters given to script: username, password, database
return states starting with 'N'
***
"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    # Link to database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],  # "your_username"
                         passwd=argv[2],  # "your_password"
                         db=argv[3])  # "your_database_name"

    # cursor created to exec queries using SQL; filter names starting with 'N'
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    for row in cursor.fetchall():
        if row[1][0] == 'N':
            print(row)

    cursor.close()
    db.close()
