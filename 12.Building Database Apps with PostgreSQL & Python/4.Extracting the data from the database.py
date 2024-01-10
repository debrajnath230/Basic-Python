import psycopg2

def table():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="9706934428",
        host="localhost",
        port="5432")

    cursor = conn.cursor()
    cursor.execute('''create table employees(Name Text , id  int , Age int);''')
    print('Table Created Successfully')

    conn.commit()
    conn.close()

def data():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="9706934428",
        host="localhost",
        port="5432")

    cursor = conn.cursor()
    cursor.execute('''insert into employees (Name, id , Age) values('Debraj',01,20);''')
    print('Data Added Successfully')

    conn.commit()
    conn.close()

def extract():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="9706934428",
        host="localhost",
        port="5432")

    cursor = conn.cursor()
    cursor.execute('''select * from employees;''')
    show= cursor.fetchone()
    print(show)
    print(show[1])
    
    conn.commit()
    conn.close()

extract()
