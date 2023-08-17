-- list of all records with the [score >= 10] in descending order
--
-- score   name
-- 10  John
-- 14  Bob

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;