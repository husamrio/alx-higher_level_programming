#!/usr/bin/python3
"""
parameters given to script: username, password, database, state to match
return matching states
*****
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # Link to database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],  # "your_username"
                         passwd=argv[2],   # "your_password"
                         db=argv[3])  # "your_database_name"

    # cursor created to exec queries using SQL; match arg given
    cursor = db.cursor()

    sql_cmd = """SELECT *
                 FROM states
                 WHERE name LIKE '{:s}' ORDER BY id ASC""".format(argv[4])

    cursor.execute(sql_cmd)

    for row in cursor.fetchall():

        if row[1] == argv[4]:
            print(row)

    cursor.close()
    db.close()
