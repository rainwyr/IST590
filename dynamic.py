import mysql.connector as MySQL
import os
conn = MySQL.connect(
    host='localhost',
    database='bank',
    user='root',
    password=os.environ.get('mysql_local_password'))
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS friends;')
cur.execute('CREATE TABLE friends (name VARCHAR(30), hobby VARCHAR(30));')
cur.execute('INSERT INTO friends VALUES (%s, %s);', ['Rain', 'Aerial Silks'])
cur.execute('INSERT INTO friends VALUES (%s, %s);', ['Vinny', 'Karate'])
cur.execute('SELECT * FROM friends')
result = cur.fetchall()
cur.execute('DROP TABLE friends;')
cur.close()
print "Friends & Hobbies"
print result
