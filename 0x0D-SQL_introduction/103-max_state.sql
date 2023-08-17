--  The max temperature is displayed of each state (arranged by State name)

SELECT state, MAX(value) as 'max_temp' FROM temperatures GROUP BY state ORDER BY state;