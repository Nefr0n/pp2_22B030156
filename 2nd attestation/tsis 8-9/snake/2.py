import psycopg2 , csv
from config import host,database,user,password

conn = psycopg2.connect(
    hostname = 'localhost',
    database = 'nefor',
    username = 'postgres',
    password = '2546',
    port_id = '5432'
)
conn.autocommit = True
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS phoneBook(
    id SERIAL PRIMARY KEY
    ,name VARCHAR(50)
    ,mobile VARCHAR(20)
)""")


def add_data(name , mobile):
    cur.execute("""INSERT INTO phoneBook(name , mobile)
                VALUES (%s , %s)""", (name , mobile)
                )

def delete(name):
    with conn.cursor() as cursor:
        cur.execute("""DELETE FROM phoneBooK WHERE name ILIKE %s
                """ , (name))
    
def update(name , mobile):
    with conn.cursor() as cursor:
        cur.execute("""SELECT FROM phoneBook WHERE name = %s OR mobile = %s
                    """ , (name , mobile))
    user = cur.fetchone()
    if user == None:
        cur.execute("""INSERT INTO phoneBook (name , mobile) 
                    VALUES (%s , %s )
                    """ , (name , mobile))
    else:
        cur.execute("""UPDATE phoneBook 
                    SET mobile = %s WHERE name = %s""" ,(mobile , name))
        
def querying_data():
    with conn.cursor() as cursor:
        print('BY ASC ENTER "asc" and BY DESC ENTER "desc" ')
        choice = input()
        if choice == 'asc':
            cur.execute("SELECT * FROM phoneBook ORDER BY name ASC" )
            rows = cur.fetchall() 
            for row in rows: 
                print(row)
        elif choice == 'desc':
            cur.execute("SELECT * FROM phoneBook ORDER BY name DESC")
            rows = cur.fetchall()
            print(rows)
        
def upload_csv(filename):
    with conn.cursor() as cursor:
        with open (filename , 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                name = row[0]
                mobile = row[1]
                cur.execute("""INSERT INTO phoneBook(name , mobile)
                        VALUES  (%s , %s )
                        """ , (name , mobile))
            
while True:
    print('PHONEBOOK PROGRAM')
    print('1. Add Entry')
    print('2. Querying data')
    print('3. Update Entry')
    print('4. Upload csv File')
    print('5. Delete Entry')
    print('6. Quit')
    choice = input('Enter your choice (1-6): ')
    
    if choice == '1':
        name = input("Enter name: ")
        mobile = input('Enter mobile: ')
        add_data(name , mobile)
    elif choice == '2':
        querying_data()
    elif choice == '3':
        name = input('Enter name: ')
        mobile = input('Enter mobile: ')
        update(name , mobile)
    elif choice == '4':
        filename = input('Enter csv filename: ')
        upload_csv(filename)
    elif choice == '5':
        name = input('Enter name to delete: ')
        delete(name)
    elif choice == '6':
        break
    else:
        print('Invalid choice.')
        
    
conn.close()