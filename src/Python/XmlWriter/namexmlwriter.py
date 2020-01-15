import sqlite3
import io
import XmlWriter




con = sqlite3.connect('1.sq3')

print("1.sq3 connected")

cur = con.cursor()
cur.execute("select * from employees");
print(cur.fetchall())


XmlWriter.printwriterhello()
f = open("myfile.txt", "w", encoding="utf-8")


namexml = XmlWriter.XmlWriter()
namexml.SetFile(f)
print("Hi")
namexml.OpenElement('CITY').Attr('NAME', 'LONDON').Attr('LANG', '15').Attr('LNG', str(45)).CloseElement()


f.close()
