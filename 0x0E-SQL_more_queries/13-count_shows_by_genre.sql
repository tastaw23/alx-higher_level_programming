-- Task: List all genres from hbtn_0d_tvshows and display the number of shows linked to each

-- Database name will be passed as an argument

-- List all genres with the number of shows linked to each genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;

