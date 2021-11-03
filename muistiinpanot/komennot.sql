-- create a database
CREATE DATABASE databasen_nimi;

-- use a database
-- \c databasen_nimi

-- check what databases there are
-- \l

-- check what tables there are
-- \d

-- create a table
CREATE TABLE certificates (
id SERIAL,
name varchar(255) NOT NULL,
person_id int,
constraint fk_person FOREIGN KEY(person_id) REFERENCES person(id)
);

CREATE TABLE person (
    id SERIAL PRIMARY KEY,
    name varchar(255) NOT NULL,
    age int NOT NULL,
    student bool
);

DROP TABLE person;

-- insert into table
INSERT INTO certificates (name, person_id)
VALUES ('GCP', 1);

INSERT INTO person (name, age, student)
VALUES ('Hannu', 24, True);

-- select from table
SELECT * FROM certificates;

-- order by something
SELECT * FROM person ORDER BY name DESC;

-- select from 2 tables with inner join
SELECT person.name, certificates.name FROM person
INNER JOIN certificates ON person.id = certificates.person_id
WHERE certificates.name = 'GCP';

-- select average
SELECT AVG(age) FROM person;

-- select count
SELECT COUNT(*) FROM person;

-- update table
UPDATE person SET name = 'esa', age = '24'
WHERE Id = 2;


-- delete from table
DELETE FROM person WHERE id = 1;

-- find all with condition
SELECT * FROM city WHERE country_code = 'FIN';

-- laske yhteen
SELECT SUM(population) FROM city WHERE country_code = 'USA';

-- listaa jollain conditionilla
SELECT name FROM city WHERE population BETWEEN 1000000 AND 2000000 LIMIT 15;

-- näytä maa jolla korkein life expectancy
-- noinspection SqlShouldBeInGroupBy

SELECT lifeexpectancy, name
FROM country
WHERE lifeexpectancy IS NOT NULL
GROUP BY name, lifeexpectancy
ORDER BY lifeexpectancy DESC
LIMIT 1;



