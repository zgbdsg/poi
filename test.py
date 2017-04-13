import sqlite3

conn = sqlite3.connect('db.sqlite')

cursor = conn.cursor()
cursor.execute('select * from URL')
values = cursor.fetchall()
print len(values)
cursor.close()

