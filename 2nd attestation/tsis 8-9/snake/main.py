
import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='nefor',
    user='postgres',
    password='2546',
    port_id = '5432'
)
cur = conn.cursor()

cur.execute("CREATE TABLE phonebook (id serial primary key, name text not null, surname text not null, mobile text)")
cur.close()
conn.close()

