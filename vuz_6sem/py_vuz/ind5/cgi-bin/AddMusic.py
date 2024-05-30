#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import cgi
import sqlite3

form = cgi.FieldStorage()
t1 = form.getfirst("music", "не задано")
t2 = form.getfirst("dat", "не задано")
print(t1)
if t1 != 'не задано' and t2 != 'не задано':
    print(1)
    with sqlite3.connect('C:\\Users\\sezen\\PycharmProjects\\pythonProject2\\vuz_6sem\\py_vuz\\ind5\\db01.db') as con:
        c = con.cursor()
        c.execute('insert into musics (music, dat) values (?,?)',
                  (t1, t2))

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Обработка запроса </title>
</head>
<body>""")
print("<h1>Обработка певца уфф</h1>")
print("<p>Музыка: %s</p>" % t1)
print("<p>Когда исполнили: %s</p>" % t2)
print('''<form action = "/index.html">
                    <input type = "submit" value = "ОК">
                </form>''')
print("""</body> </html>""")