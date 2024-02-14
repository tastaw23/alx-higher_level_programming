-- Task: Create the hbtn_0d_usa database and the states table if they don't exist

-- Check if the hbtn_0d_usa database exists, create it if not
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
