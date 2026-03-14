import sqlite3
db_path="data/database/nhs_ae.db"
conn=sqlite3.connect(db_path)
print("Database created successfully")
conn.close()