-- Create table unique_id with a unique id and defaults to 1
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256));
