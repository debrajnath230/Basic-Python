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
    
    name=input('Enter Name: ')
    id=input('Enter id: ')
    age=input('Enter Age: ')
    
    query='''insert into employees (Name, id , Age) values(%s,%s,%s);'''
    cursor.execute(query,(name,id,age))
    
    print('Data Added Successfully')

    conn.commit()
    conn.close()

data()
