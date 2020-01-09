import sqlite3
import XmlWriter

def printhello():
    print('Hello from printhello')



print("Hello from pysqlite.py")
con = sqlite3.connect('1.sq3')

print("1.sq3 connected")

cur = con.cursor()
cur.execute("select * from employees");
print(cur.fetchall())
printhello()
XmlWriter.printwriterhello()

namexml = XmlWriter.XmlWriter()
namexml.print()
namexml.OpenElement('CITY').CloseElement()
