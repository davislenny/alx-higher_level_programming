-- Creates the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create user user_Od_2 with password user_Od_2_pwd
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Give the user readonly privilege
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
