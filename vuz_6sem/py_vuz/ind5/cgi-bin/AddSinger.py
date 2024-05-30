#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import cgi
import sqlite3

form = cgi.FieldStorage()
t1 = form.getfirst("name1", "не задано")
t2 = form.getfirst("age", "не задано")
t3 = form.getfirst("country", "не задано")
t4 = form.getfirst("place", "не задано")
t5 = form.getfirst("music", "не задано")
if t1 != 'не задано' and t2 != 'не задано' and t3 != 'не задано' and t4 != 'не задано' and t5 != 'не задано':
    with sqlite3.connect('C:\\Users\\sezen\\PycharmProjects\\pythonProject2\\vuz_6sem\\py_vuz\\ind5\\db01.db') as con:
        c = con.cursor()
        c.execute('select id from places where place = ?', (t4, ))
        t4 = int(c.fetchall()[0][0])
        print(t4)
        c.execute('select id from musics where music = ?', (t5, ))
        t5 = int(c.fetchall()[0][0])
        c.execute('insert into singers (name, age, country, place_id, music_id) values (?,?,?,?,?)',
                  (t1, int(t2), t3, t4, t5))
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Обработка запроса </title>
</head>
<body>""")
print("<h1>Обработка певца уфф</h1>")
print("<p>Имя: %s</p>" % t1)
print("<p>Возраст: %s</p>" % t2)
print("<p>Страна: %s</p>" % t3)
print("<p>Город: %s</p>" % t4)
print("<p>Музыка: %s</p>" % t5)
print('''<form action = "/index.html">
                    <input type = "submit" value = "ОК">
                </form>''')
print("""</body> </html>""")