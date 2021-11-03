import psycopg2
from config import config as config

con = None
try:
    con = psycopg2.connect(**config())
    cursor = con.cursor()
    '''
    SQL = "SELECT person.name, certificates.name " \
          "FROM person INNER JOIN certificates " \
          "ON person.id = certificates.person_id " \
          "WHERE certificates.name = 'GCP';"
    '''
    cert_name = 'AWS'
    person_id = 2
    SQL = "INSERT INTO certificates (name, person_id) VALUES (%s, %s);"
    record_to_insert = (cert_name, person_id)
    cursor.execute(SQL, record_to_insert)
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