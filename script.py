import MySQLdb
import csv

# Connect to MySQL database
conn = MySQLdb.connect(
    host="localhost",
    user="user",
    passwd="password",
    db="revou"
)

# Create a cursor object
cursor = conn.cursor()

# Function to load data from CSV and insert into the database
def load_data_from_csv(filename, table):
    with open(filename, 'r') as file:
        csv_data = csv.reader(file)
        next(csv_data)  # Skip the header row
        for row in csv_data:
            cursor.execute(f"INSERT INTO {table} VALUES ({','.join(['%s']*len(row))})", row)
        conn.commit()

# Load data from CSV files and insert into the database
load_data_from_csv('./seeds/authors.csv', 'authors')
load_data_from_csv('./seeds/publishers.csv', 'publishers')
load_data_from_csv('./seeds/books.csv', 'books')
load_data_from_csv('./seeds/sales.csv', 'sales')

# Close the cursor and database connection
cursor.close()
conn.close()
