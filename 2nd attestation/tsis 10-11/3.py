import psycopg2
import csv

hostname = 'localhost'
database = 'nefor'
username = 'postgres'
password = ' 2546'
port_id = '5432'

conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = password,
            port = port_id)

cur = conn.cursor()


#1) DESING THE TABLE FOR PHONEBOOK
#cur.execute("DROP TABLE PhoneBook")
cur.execute("""CREATE TABLE IF NOT EXISTS PhoneBook(
    id SERIAL PRIMARY KEY
    ,name TEXT NOT NULL
    ,phone TEXT NOT NULL
    ,surname TEXT NOT NULL
)""")
#conn.commit()
# 2)TWO WAYS OF    INSERTIN DATA 1.BY ENTERING

'''
CREATE OR REPLACE FUNCTION find_records(startN TEXT)
RETURNS SETOF PhoneBook AS $$
BEGIN
	RETURN QUERY SELECT * FROM PhoneBook WHERE name LIKE "n%";
END;
$$ LANGUAGE plpgsql;
'''





def add_data(name , phone, surname):
    cur.execute("""INSERT INTO PhoneBook(name , phone, surname)
                VALUES (%s, %s, %s)""", (name , phone, surname))
    conn.commit()
# 2.BY UPLOADINNG DATA FROM CSV FILE
def upload_csv(filename):
    with conn.cursor() as cursor:
        with open (filename + '.csv') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                
                cur.execute("""INSERT INTO PhoneBook(name , phone, surname)
                        VALUES  (%s, %s, %s)
                        """ , (row[0] , row[1], row[2]))
    conn.commit()

#3) UPDATING DATA IN THE TABLE
def update(name):
    newname = input("Enter a new name: ")
    newphone = input("Enter a new phone number: ")
    newsur = input("Enter a new surname: ")
    cur.execute("SELECT * FROM PhoneBook WHERE name = %s",(name,))
    res = cur.fetchall()
    for record in res:
        cur.execute("UPDATE PhoneBook SET name = %s WHERE name = %s", (newname, record[1]))
        cur.execute("UPDATE PhoneBook SET phone = %s WHERE phone = %s", (newphone, record[2]))
        cur.execute("UPDATE PhoneBook SET surname = %s WHERE surname = %s", (newsur, record[3]))
    conn.commit()
    
    print("hello bitch")

#4) QUERING DATA FROM TABLES
def querying_data():
    with conn.cursor() as cursor:
        print('BY ASC ENTER "asc" and BY DESC ENTER "desc" or by N ')
        choice = input()
        if choice.lower() == 'asc':
            cur.execute("SELECT * FROM PhoneBook ORDER BY name ASC" )
            rows = cur.fetchall() 
            for row in rows: 
                print(row)
        elif choice.lower() == 'desc':
            cur.execute("SELECT * FROM PhoneBook ORDER BY name DESC")
            rows = cur.fetchall()
            print(rows)
        elif choice.lower() == "n":
            cur.callproc('find_records', ['name'])
            rows = cur.fetchall()
            print(rows)
    conn.commit()

#5) DELETE DATA FROM TABLES
def delete(name):
    cur.execute("""DELETE FROM PhoneBooK WHERE name = %s """ , (name, ))
    conn.commit()

run = True
while run:
    print(' ')
    print(" ")
    print(" ")
    print('PHONEBOOK. WHAT YOU WANT?:')
    print(" ")
    print('1. ADD ENTRY')
    print('2. UPLOAD CSV FILE')
    print('3. UPDATE CONTACTS')
    print('4. QUERY THE DATA')
    print('5. DELETE THE DATA')
    print('6. QUIT')
    choice = input()

    if choice == '1':
        name = input("Enter name: ")
        phone = input('Enter phone: ')
        surname = input("Enter surname: ")
        add_data(name, phone, surname)
    elif choice == '2':
        filename = input('Enter csv filename: ')
        upload_csv(filename)
    elif choice == '3':
        name = input("Enter a name: ")
        update(name)
    elif choice == '4':
        querying_data()    
    elif choice == '5':
        surname = input('Enter name to delete: ')
        delete(surname)
    elif choice == '6':
        run = False
        conn.close()
        cur.close()
    else:
        print('Wrong value')
            
