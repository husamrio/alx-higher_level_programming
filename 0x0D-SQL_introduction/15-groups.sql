-- displays this data sorted by number in descending order
-- lists the `score` and number of occurances with each score with 'number'
-- score   number
--
-- 8   1
-- 10  2

SELECT score, COUNT(score) AS 'number' FROM second_table GROUP BY score ORDER BY number DESC;