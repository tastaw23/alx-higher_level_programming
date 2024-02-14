-- 4-never_empty.sql

-- Task Description: Create table id_not_null in the specified database

-- Create table id_not_null if it does not exist
CREATE TABLE IF NOT EXISTS hbtn_0d_2.id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

