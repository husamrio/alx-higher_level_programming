--  data in table Updated;  Bob's changed score to 10
--
-- score   name
-- 10  John
-- 10  Bob
-- 3   Alex
-- 8   George

UPDATE second_table SET `score` = 10 WHERE `name` = 'Bob';