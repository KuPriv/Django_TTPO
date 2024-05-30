#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3

with sqlite3.connect('C:\\Users\\sezen\\PycharmProjects\\pythonProject2\\vuz_6sem\\py_vuz\\ind5\\db01.db') as con:
    c = con.cursor()
    c.execute('select * from places')

    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
    <html>
    <head>
    <meta charset="utf-8">
    <title>Обработка запроса </title>
    </head>
    <body>""")
    print('<h1> Города </h1>')
    s = [(str(i + 1), 'Город: ', x[1], 'Количество посещений: ', int(x[2]), '\n') for i, x in enumerate(c.fetchall())]
    for i in range(len(s)):
        print(i + 1, "Городок")
        for j in range(1, int(len(s[i])) - 1, 2):
            print('<p>', s[i][j], s[i][j + 1], '</p>')
    c.execute('select * from singers')

    print('<h1> Певцы </h1>')
    s = [(str(i + 1), 'Имя: ', x[1], 'Возраст: ', int(x[2]), 'Страна: ', str(x[3]), 'Город: ', int(x[4]), 'Музыка: ', int(x[5]),  '\n') for i, x in enumerate(c.fetchall())]
    for i in range(len(s)):
        print(i + 1, "Певец")
        for j in range(1, int(len(s[i])) - 1, 2):
            if s[i][j] == 'Город: ':
                c.execute('select place from places where id = ?', (int(s[i][j+1]), ))
                print('<p>', s[i][j], c.fetchall()[0][0], '</p>')
            elif s[i][j] == 'Музыка: ':
                c.execute('select music from musics where id = ?', (int(s[i][j+1]), ))
                print('<p>', s[i][j], c.fetchall()[0][0], '</p>')
            else:
                print('<p>', s[i][j], s[i][j + 1], '</p>')
    c.execute('select * from musics')
    print('<h1> Музыка </h1>')
    s = [(str(i + 1), 'Музыка: ', x[1], 'Когда исполнили: ', x[2], '\n') for i, x in enumerate(c.fetchall())]
    for i in range(len(s)):
        print(i + 1, "Музычка")
        for j in range(1, int(len(s[i])) - 1, 2):
            print('<p>', s[i][j], s[i][j + 1], '</p>')
    print('''<form action = "/index.html">
                    <input type = "submit" value = "ОК">
                </form>''')
    print('</body></html>')