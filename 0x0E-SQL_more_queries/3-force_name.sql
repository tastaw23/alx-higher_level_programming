-- 3-force_name.sql

-- Task Description: Create table force_name in the specified database

-- Create table force_name if it does not exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
    );

