-- Task: List all cities of California without using JOIN

-- Database name will be passed as an argument

-- List all cities of California using the state_id for 'California'
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id
  AND states.name = 'California'
ORDER BY cities.id ASC;

