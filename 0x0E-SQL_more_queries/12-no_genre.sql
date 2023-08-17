-- the database name will be passed as an argument of the mysql command
-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked
-- can use only one SELECT statement
-- results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- each record should display: tv_shows.title - tv_show_genres.genre_id
--
--      curl [link] -s | mysql -uroot -p hbtn_0d_tvshows
--      echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
-- run this first to import a SQL dump -->
-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql

   SELECT tv_shows.title, tv_show_genres.genre_id
     FROM tv_shows
LEFT JOIN tv_show_genres
       ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_show_genres.genre_id IS NULL
 ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;