import sqlite3

print("Hello from pysqlite.py")
con = sqlite3.connect('1.sq3')

print("1.sq3 connected")

cur = con.cursor()
cur.execute("select * from employees");
print(cur.fetchall())
