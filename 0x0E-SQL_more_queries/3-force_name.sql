-- database name will be passed as an argument of the mysql command
-- creates the table force_name
-- if table exists, script should not fail
-- data in table: id INT, name VARCHAR(256) can’t be null

CREATE TABLE IF NOT EXISTS force_name (
       id INT,
       name VARCHAR(256) NOT NULL
);