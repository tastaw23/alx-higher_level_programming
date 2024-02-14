-- Task: List all shows from hbtn_0d_tvshows_rate by their rating

-- Database name will be passed as an argument

-- List all shows by their rating
SELECT tv_shows.title, COALESCE(SUM(rating), 0) AS rating_sum
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;

