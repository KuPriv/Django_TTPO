#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import sqlite3


f = cgi.FieldStorage()
t1 = f.getfirst('place', 'не задано')
t2 = f.getfirst('col', 'не задано')
if t1 != 'не задано' and t2 != 'не задано':
    with sqlite3.connect('C:\\Users\\sezen\\PycharmProjects\\pythonProject2\\vuz_6sem\\py_vuz\\ind5\\db01.db') as con:
        c = con.cursor()
        c.execute('insert into places (place, col) values (?, ?)', (t1, int(t2)))

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Обработка запроса </title>
</head>
<body>""")
print("<h1>Обработка города уфф</h1>")
print("<p>Город: %s</p>" % t1)
print("<p>Количество: %s</p>" % t2)
print('''<form action = "/index.html">
                    <input type = "submit" value = "ОК">
                </form>''')
print("""</body> </html>""")
