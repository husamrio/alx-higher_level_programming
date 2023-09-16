#!/usr/bin/python3
"""
parameters given to script: username, password, database, state
return cities that are in the state given (tables 'cities' 'states)
*****
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # connect to database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],  # "your_username"
                         passwd=argv[2],  # "your_password"
                         db=argv[3])  # "your_database_name"

    # cursor created to exec queries using SQL; join two tables for all info
    cursor = db.cursor()

    sql_cmd = """SELECT cities.name
                 FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 WHERE states.name LIKE %s
                 ORDER BY cities.id ASC"""

    cursor.execute(sql_cmd, (argv[4], ))

    # Style of the printing of cities of same state separated by commas
    print(', '.join(["{:s}".format(row[0]) for row in cursor.fetchall()]))

    cursor.close()
    db.close()
