-- create user user_0d_1 set password to 'user_0d_1_pwd'
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privileges on MySQL server
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
