-- Task: List all genres not linked to the show Dexter from hbtn_0d_tvshows

-- Database name will be passed as an argument

-- List all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN (
    SELECT tv_show_genres.genre_id
    FROM tv_show_genres
    JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
) AS DexterGenres ON tv_genres.id = DexterGenres.genre_id
WHERE DexterGenres.genre_id IS NULL
ORDER BY tv_genres.name ASC;

