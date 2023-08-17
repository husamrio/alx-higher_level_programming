-- if user_0d_1 already exists, script should not fail
-- password should be set to user_0d_1_pwd
-- should have all privileges
-- creates the MySQL server user user_0d_1

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;