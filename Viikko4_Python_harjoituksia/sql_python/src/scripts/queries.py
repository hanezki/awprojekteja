import psycopg2
from config import config

con = None
try:
    con = psycopg2.connect(**config())
    cursor = con.cursor()

    SQL = "CREATE TABLE dogs (id SERIAL PRIMARY KEY,name varchar(255) NOT NULL,breed varchar(255) NOT NULL);"
    cursor.execute(SQL)
    con.commit()

    cursor.execute("SELECT * FROM certificates")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if con is not None:
        con.close()