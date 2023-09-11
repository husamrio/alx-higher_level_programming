--  the top 3 of cities displays temperature during August and July ordered by temperature (descending)

SELECT city, AVG(value) as 'avg_temp' FROM temperatures WHERE `month`=7 OR `month`=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;