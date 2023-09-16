#!/usr/bin/python3
"""
parameters given to script: username, password, database
return all table values (table 'states')
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

    # cursor to be created to exec queries using SQL
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
