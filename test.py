import sqlite3

connection = sqlite3.connect("datas.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM events WHERE band='Tiger'")
print(cursor.fetchall())

cursor.execute("SELECT band, date FROM events WHERE band='Tiger'")
print(cursor.fetchall())

cursor.execute("INSERT INTO events VALUES('AR Rahman', 'Chennai', '2024.1.23')")
connection.commit()