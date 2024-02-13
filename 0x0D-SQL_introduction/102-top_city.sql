-- Displaying the top 3 cities' temperatures during July and August ordered by temperature (descending)
-- List top 3 cities
-- Execute: cat 102-top_city.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp 
DESC LIMIT 3;
