
import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='nefor',
    user='postgres',
    password='2546',
    port ='5432'
)
cur = conn.cursor()

cur.execute("CREATE TABLE phonebook (id SERIAL PRIMARY KEY , name TEXT NOT NULL, surname TEXT, mobile TEXT)")


conn.commit()