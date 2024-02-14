-- Task: List all shows in hbtn_0d_tvshows with associated genre_id or NULL

-- Database name will be passed as an argument

-- List all shows with associated genre_id or NULL
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

