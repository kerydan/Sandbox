import sqlite3
import io
import XmlWriter




con = sqlite3.connect('1.sq3')

print("1.sq3 connected")

cur = con.cursor()
cur.execute("select * from employees");
print(cur.fetchall())


XmlWriter.printwriterhello()

namexml = XmlWriter.XmlWriter()
namexml.OpenElement('CITY').Attr('NAME', 'LONDON').Attr('LANG', '15').Attr('LNG', str(45)).CloseElement()


f = open("myfile.txt", "w", encoding="utf-8")

f.write("bla bla")
f.close()
