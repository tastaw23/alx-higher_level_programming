-- 6. List all values in first_table
-- Script to list all rows of the table 'first_table' in the specified database

-- Database name passed as an argument to the mysql command
USE `$1`;

-- Listing all rows of 'first_table'
SELECT * FROM first_table;

