CREATE DATABASE Keittio;

CREATE TABLE Astia(
    id SERIAL,
    nimi varchar(255) NOT NULL,
    lkm int
);

-- vaihe 2 juttuja

CREATE TABLE Toimipaikka(
    id SERIAL PRIMARY KEY,
    nimi varchar(255) NOT NULL,
    sijainti varchar(255) NOT NULL,
    aloitusvuosi int NOT NULL
);

INSERT INTO Toimipaikka (nimi, sijainti, aloitusvuosi)
VALUES ('Academy Finland', 'Espoo', 2017),
       ('Academy Sweden', 'Kista', 2015),
       ('Academy Germany', 'Munchen', 2018);

ALTER TABLE Astia ADD toimipaikka_id int;

ALTER TABLE Astia ADD FOREIGN KEY (toimipaikka_id) REFERENCES Toimipaikka(id);

