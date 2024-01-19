-- This script creates a table named 'users' wwith the attribute id, email & name.
-- If the table already exists, the script will not fail.

CREATE TABLE IF NOT EXISTS users (
	-- id attribute is an integer, never null, auto increaments
	-- is the primary key
        id INT AUTO_INCREMENT PRIMARY KEY,
	-- The email attribute is a string of 255 characters.
        -- Never null, and unique.
        email VARCHAR(255) NOT NULL UNIQUE,
	-- Name attribute is a string of 255 characters.
        name VARCHAR(255)
);
