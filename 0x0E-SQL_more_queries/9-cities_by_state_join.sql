-- Task: List all cities in the database hbtn_0d_usa with associated state names

-- Database name will be passed as an argument

-- List all cities with associated state names
SELECT cities.id, cities.name, (SELECT states.name FROM states WHERE states.id = cities.state_id) AS state_name
FROM cities
ORDER BY cities.id ASC;
