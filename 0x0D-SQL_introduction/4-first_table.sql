-- create table; should not fail if is in existance already

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));