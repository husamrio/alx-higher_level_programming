--      curl [link] -s | mysql -uroot -p hbtn_0d_tvshows
--      echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
-- run this first to import a SQL dump -->
-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
--
-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
-- results must be sorted in ascending order by the show title and genre name
-- each record should display: tv_shows.title - tv_genres.name
-- the database name will be passed as an argument of the mysql command
-- can use only one SELECT statement
-- if a show doesn’t have a genre, display NULL in the genre column

    SELECT tv_shows.title, tv_genres.name
      FROM tv_shows
 LEFT JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
 LEFT JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
  ORDER BY tv_shows.title, tv_genres.name ASC;