import psycopg2
import csv
from psycopg2 import sql

# Database connection parameters
db_params = {
    'dbname': 'guru99',
    'user': 'postgres',
    'password': '9706934428',
    'host': 'localhost',  # Note: Use lowercase 'localhost'
    'port': '5432'
}

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(**db_params)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Specify the table name
table_name = 'electronics_gadgets'

# Construct a SQL query to select all columns from the table
query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))

# Execute the query
cursor.execute(query)

# Fetch all rows from the result set
rows = cursor.fetchall()

# Output fetched data to a CSV file
csv_filename = 'C://Users//nath.debraj//Desktop//Python_training_tutordude//electronics_gadgets_data.csv'
with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write the header (column names) to the CSV file
    csv_writer.writerow([desc[0] for desc in cursor.description])

    # Write the data to the CSV file
    csv_writer.writerows(rows)

print(f'Data has been exported to {csv_filename}')

# Close the cursor and connection
cursor.close()
conn.close()
