-- 3-force_name.sql

-- Task Description: Create database hbtn_0d_2 and table force_name

-- Create database hbtn_0d_2 if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Use the database hbtn_0d_2
USE hbtn_0d_2;

-- Create table force_name if it does not exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

