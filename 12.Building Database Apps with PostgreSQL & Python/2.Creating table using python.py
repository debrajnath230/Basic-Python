import psycopg2
connect = psycopg2.connect(
    dbname="MPFBF",
    user="postgres",
    password="9706934428",
    host="Localhost",
    port="5432")

cursor=connect.cursor()
cursor.execute('''create table employees(Name Text , id  int , Age int);''')
print('Table Created Successfully')

connect.commit()
connect.close()

