import sqlite3

con = sqlite3.connect('C:\\Users\\sezen\\PycharmProjects\\pythonProject2\\vuz_6sem\\py_vuz\\ind5\\db01.db')
cur = con.cursor()
#ПЕРВАЯ ТАБЛИЦА
cur.execute('DROP TABLE IF EXISTS musics')
cur.execute('CREATE TABLE musics (id INTEGER PRIMARY KEY, music VARCHAR(30), dat TEXT)')
var_list = [
    ("Я буду руки твои целовать", '20.11.2015'),
    ("Молния", '14.12.2016'),
    ("Stuck with U", '13.08.2017'),
    ("Песня1", '12.07.2018'),
]
sql = '''\
INSERT INTO musics(music, dat)
VALUES (?,?)
'''
cur.executemany(sql, var_list)
con.commit()
cur.execute('SELECT * FROM musics')
print(f'Первая таблица = {cur.fetchall()}')
#ВТОРАЯ ТАБЛИЦА
cur.execute('DROP TABLE IF EXISTS places')
cur.execute('CREATE TABLE places (id INTEGER PRIMARY KEY, place VARCHAR(30), col INTEGER)')
var_list = [
    ("Moscow", 2),
    ("Sochi", 1),
    ("Washington", 2)
]
sql = '''\
INSERT INTO places(place, col)
VALUES (?,?)
'''
cur.executemany(sql, var_list)
con.commit()
cur.execute('SELECT * FROM places')
print(f'Вторая таблица = {cur.fetchall()}')
#ТРЕТЬЯ ТАБЛИЦА
cur.execute('DROP TABLE IF EXISTS singers')
cur.execute('CREATE TABLE singers (id INTEGER PRIMARY KEY, name VARCHAR(30), age INTEGER, country VARCHAR(30), '
            'place_id INTEGER, music_id INTEGER, FOREIGN KEY (place_id) REFERENCES places (id), FOREIGN KEY'
            '(music_id) REFERENCES musics (id))')
var_list = [
    ("Baskov", 47, "Russia",  1, 1),
    ("Arianna Grande", 30, "USA", 3, 2),
    ("Bilan", 42, "Russia", 2, 3),
]
sql = '''\
INSERT INTO singers(name, age, country, place_id, music_id)
VALUES (?,?,?,?,?)
'''
cur.executemany(sql, var_list)
con.commit()
cur.execute('SELECT * FROM singers')
print(f'Третья таблица = {cur.fetchall()}')
con.close()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Обработка запроса </title>
</head>
<body>""")
print('<h1> База присутствует</h1>')
print('''<form action = "/index.html">
                    <input type = "submit" value = "ОК">
                </form>''')
print('</body></html>')