-- the database name will be passed as an argument of the mysql command
-- Each record should display: cities.id - cities.name - states.name
-- results must be sorted in ascending order by cities.id
-- lists all the cities in the database hbtn_0d_usa
-- can use only one SELECT statement

  SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states
   WHERE cities.state_id = states.id
ORDER BY cities.id ASC;