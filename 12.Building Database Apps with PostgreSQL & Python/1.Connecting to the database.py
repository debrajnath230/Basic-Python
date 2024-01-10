import psycopg2
connect = psycopg2.connect(
    dbname="MPFBF",
    user="postgres",
    password="9706934428",
    host="Localhost",
    port="5432"
    )

print('Connected Successfully')