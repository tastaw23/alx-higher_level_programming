-- Listing the number of records with the same score, sorted by the number of records (descending)
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
