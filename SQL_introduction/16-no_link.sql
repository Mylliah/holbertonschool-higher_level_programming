-- script that lists all records of a table with specifics constraints
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;