-- 5. Full table description
-- Script to print the full description of the table 'first_table' in the specified database

-- Database name passed as an argument to the mysql command
USE `$1`;

-- Printing the full description of 'first_table'
SHOW CREATE TABLE first_table;

