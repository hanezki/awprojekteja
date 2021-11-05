import psycopg2
from config import config as config
import PIL.Image as Image


con = None
try:
    con = psycopg2.connect(**config())
    cursor = con.cursor()

    SQL = "SELECT file_data FROM files WHERE orig_filename = 'kitten.png';"
    cursor.execute(SQL)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if con is not None:
        con.close()