import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="drivebcevent_project",
    user=".....",
    password="....",  
    host="localhost",
    port="..."
)

# Create a cursor and execute a count query
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM drivebcevents;")
print("Total Rows in drivebcevents:", cur.fetchone()[0])

# View a few rows from the table
cur.execute("SELECT * FROM drivebcevents LIMIT 5;")
rows = cur.fetchall()
for row in rows:
    print(row)

# Clean up
cur.close()
conn.close()