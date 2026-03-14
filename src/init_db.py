import sqlite3

db_path = r"data\database\nhs_ae.db"

conn=sqlite3.connect(db_path)

with open(r"sql\create_tables.sql","r") as f:
    conn.executescript(f.read())

print("Tables created")

conn.close()

