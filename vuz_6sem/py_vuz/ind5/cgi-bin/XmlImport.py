import encodings
import sqlite3
import xml.dom.minidom
from xml import etree

doc = xml.dom.minidom.Document()
root = doc.createElement('table')
doc.appendChild(root)
with sqlite3.connect('C:\\Users\\sezen\\PycharmProjects\\pythonProject2\\vuz_6sem\\py_vuz\\ind5\\db01.db') as con:
    c = con.cursor()
    c.execute('select * from places')
    for row in c.fetchall():
        dic = ['id', 'place', 'col']
        row = {'id': str(row[0]), 'place': row[1], 'col': str(row[2])}
        record = doc.createElement('record')
        root.appendChild(record)
        for key, value in row.items():
            element = doc.createElement(key)
            element.appendChild(doc.createTextNode(value))
            record.appendChild(element)

    with open('C:\\Users\\sezen\\PycharmProjects\\pythonProject2\\vuz_6sem\\py_vuz\\ind5\\table.xml', 'w') as f:
        f.write(doc.toprettyxml())
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
    <html>
    <head>
    <meta charset="utf-8">
    <title>Обработка запроса </title>
    </head>
    <body>""")
print('''<form action = "/index.html">
                    <input type = "submit" value = "ОК">
                </form>''')
print('</body></html>')