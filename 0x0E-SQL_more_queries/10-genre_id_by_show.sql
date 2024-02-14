-- Task: List all shows in hbtn_0d_tvshows that have at least one genre linked

-- Database name will be passed as an argument

-- List all shows with at least one linked genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

