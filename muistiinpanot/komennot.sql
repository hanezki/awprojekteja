-- create a database
CREATE DATABASE databasen_nimi;

-- valitse käytettävä database
USE databasen_nimi;

-- create a table
CREATE TABLE PERSON (
    Id SERIAL,
    NAME varchar(255) NOT NULL,
    AGE int NOT NULL,
    STUDENT bool
);

-- insert into table
INSERT INTO PERSON (Name, Age, Student)
VALUES ('jorma', 45, True);

-- select from table
SELECT * FROM PERSON;

-- order by something
SELECT * FROM person ORDER BY name DESC;

-- select average
SELECT AVG(age)
FROM person
