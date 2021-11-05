import psycopg2
from config import config


sql_list = []


def lisaa_astiat():
    SQL1 = "INSERT INTO Astia (nimi, lkm) VALUES ('Muki', 100);"
    SQL2 = "INSERT INTO Astia (nimi, lkm) VALUES ('Lasi', 80);"
    SQL3 = "INSERT INTO Astia (nimi, lkm) VALUES ('Iso lautanen', 40);"
    SQL4 = "INSERT INTO Astia (nimi, lkm) VALUES ('Pieni lautanen', 40);"
    sql_list.append(SQL1)
    sql_list.append(SQL2)
    sql_list.append(SQL3)
    sql_list.append(SQL4)
    suorita_sql(sql_list)


def tulosta_astiat():

    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        SQL = "SELECT * FROM Astia"
        cursor.execute(SQL)
        rows = cursor.fetchall()
        for row in rows:
            nimi = row[1]
            lkm = row[2]
            print(f"{nimi}, {lkm}kpl")
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
    tulosta_astiat()