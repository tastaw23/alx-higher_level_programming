-- 3-force_name.sql

-- Task Description: Create database hbtn_0d_2 and table force_name

-- Create database hbtn_0d_2 if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create table force_name in the hbtn_0d_2 database
CREATE TABLE IF NOT EXISTS hbtn_0d_2.force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

