import sqlite3

conn = sqlite3.connect('db.sqlite')

cursor = conn.cursor()
cursor.execute('insert into url (u) values (\'www.baidu.com\')')
conn.commit()
cursor.close()
cursor = conn.cursor()
cursor.execute('select * from URL')
values = cursor.fetchall()
print values
cursor.close()

