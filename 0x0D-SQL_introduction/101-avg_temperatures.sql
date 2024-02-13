-- Database name passed as an argument to the mysql command
USE hbtn_0c_0;

-- Displaying the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
