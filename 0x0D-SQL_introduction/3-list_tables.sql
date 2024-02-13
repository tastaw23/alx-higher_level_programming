-- 3. List tables of a database
-- Script to list all tables of a specified database

-- Database name passed as an argument to the mysql command
USE `$1`;

-- Displaying all tables in the specified database
SHOW TABLES;

