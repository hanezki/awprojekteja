import psycopg2
from config import config


sql_list = []


def lisaa_astiat():
    sql_list.clear()
    SQL1 = "INSERT INTO Astia (nimi, lkm, toimipaikka_id) VALUES ('Muki', 100, 1);"
    SQL2 = "INSERT INTO Astia (nimi, lkm, toimipaikka_id) VALUES ('Lasi', 80, 1);"
    SQL3 = "INSERT INTO Astia (nimi, lkm, toimipaikka_id) VALUES ('Iso lautanen', 40, 1);"
    SQL4 = "INSERT INTO Astia (nimi, lkm, toimipaikka_id) VALUES ('Pieni lautanen', 40, 1);"
    sql_list.append(SQL1)
    sql_list.append(SQL2)
    sql_list.append(SQL3)
    sql_list.append(SQL4)
    suorita_sql(sql_list)

def paivita():
    sql_list.clear()
    SQL = "UPDATE Astia SET lkm = 100 WHERE nimi = 'Lasi';"
    sql_list.append(SQL)
    suorita_sql(sql_list)


def lisaa():
    sql_list.clear()
    SQL = "INSERT INTO Astia (nimi, lkm, toimipaikka_id) VALUES ('Muki', 100, 2);"
    SQL2 = "INSERT INTO Astia (nimi, lkm, toimipaikka_id) VALUES ('Muki', 100, 3);"
    sql_list.append(SQL)
    sql_list.append(SQL2)
    suorita_sql(sql_list)

def poista():
    sql_list.clear()
    SQL = "DELETE FROM Astia WHERE nimi = 'Pieni lautanen' AND toimipaikka_id = 1;"
    sql_list.append(SQL)
    suorita_sql(sql_list)


def tulosta_astiat():

    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = "SELECT Astia.nimi, Astia.lkm, Toimipaikka.sijainti FROM Astia INNER JOIN Toimipaikka ON Astia.toimipaikka_id = Toimipaikka.id;"
        cursor.execute(SQL)
        rows = cursor.fetchall()

        for row in rows:
            nimi = row[0]
            lkm = row[1]
            toimipaikka = row[2]
            print(f"{toimipaikka}: {nimi}, {lkm}kpl")


        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()


# Tämmöne ois näppärä jos ois enemmän funktioita jotka jollain tavalla
# muokkaa tietokannan sisältöä
def suorita_sql(sql_list_to_execute):

    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()

        for sql in sql_list_to_execute:
            cursor.execute(sql)
        con.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()


if __name__ == "__main__":
    #lisaa_astiat()
    #paivita()
    #lisaa()
    #poista()
    tulosta_astiat()