import sqlite3

# Connect or create DB file
conn = sqlite3.connect('mydatabase.db')

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')

# Insert data
cursor.execute('''
INSERT INTO users (name, email) VALUES (?, ?)
''', ('Ramesh', 'ramesh@example.com'))

# Commit changes
conn.commit()

# Query data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close connection
conn.close()
