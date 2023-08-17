-- Records should be listed by descending score
-- Don’t list rows without a name value
-- Lists all records of the table second_table of the database hbtn_0c_0
-- The database name will be passed as an argument to the mysql command
-- Results should display the score and the name (in this order)

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;