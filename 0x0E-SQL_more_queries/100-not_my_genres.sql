-- the database name will be passed as an argument of the mysql command
-- can use max two SELECT statements
-- results must be sorted in ascending order by the genre name
-- each record should display: tv_genres.name
-- tv_shows table contains only one record where title = Dexter (but the id can be different)
-- script that uses the hbtn_0d_tvshows database to lists all genres not linked to Dexter
--
--      curl [link] -s | mysql -uroot -p hbtn_0d_tvshows
--      echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
-- run this first to import a SQL dump -->
-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql

    SELECT tv_genres.name
      FROM tv_genres
     WHERE tv_genres.name NOT IN (
    SELECT tv_genres.name
      FROM tv_genres
INNER JOIN tv_show_genres
        ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
	ON tv_show_genres.show_id = tv_shows.id
     WHERE tv_shows.title = "Dexter")
  ORDER BY tv_genres.name ASC;