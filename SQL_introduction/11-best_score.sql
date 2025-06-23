-- script that lists all records with a specific score in a table
SELECT score, name 
FROM second_table 
WHERE score >= 10 
ORDER BY score DESC;