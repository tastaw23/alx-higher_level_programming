-- Task: List all genres in hbtn_0d_tvshows_rate by their rating

-- Database name will be passed as an argument

-- List all genres by their rating
SELECT tv_genres.name, COALESCE(SUM(rating), 0) AS rating_sum
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;

