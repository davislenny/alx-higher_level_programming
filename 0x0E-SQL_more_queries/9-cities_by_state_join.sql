-- Lists all cities contained in the database hbtn_0d_usa
-- Display cities.id - cities.name - states.namem sorted in ascending order by cities.id
SELECT cities.id, cities.name, states.namem
FROM cities
INNER JOIN states
ON states.id = cities.state_id
ORDER BY cities.id ASC;
