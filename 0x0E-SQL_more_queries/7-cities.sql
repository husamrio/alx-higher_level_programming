-- description of table data:
-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
--      state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states
-- should not fail if either exists
--      id INT unique, auto generated, can’t be null and is a primary key
--      name VARCHAR(256), can't be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
       id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
);