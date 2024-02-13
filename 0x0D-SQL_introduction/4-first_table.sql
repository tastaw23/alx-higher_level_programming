-- 4. Create first_table
-- Script to create the table 'first_table' in the specified database

-- Database name passed as an argument to the mysql command
USE `$1`;

-- Creating 'first_table' if it doesn't exist
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);

