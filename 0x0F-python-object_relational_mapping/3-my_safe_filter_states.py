#!/usr/bin/python3
"""
parameters given to script: username, password, database, state to match
# http://bobby-tables.com/python
*********
return matching states; safe from MySQL injections
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

    # cursor created to exec queries using SQL; match arg given
    cursor = db.cursor()
    sql_cmd = """SELECT *
                 FROM states
                 WHERE name=%s ORDER BY id ASC"""

    cursor.execute(sql_cmd, (argv[4],))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
