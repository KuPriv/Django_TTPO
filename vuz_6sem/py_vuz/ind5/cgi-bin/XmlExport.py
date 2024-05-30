import sqlite3
import xml.dom.minidom

with sqlite3.connect('C:\\Users\\sezen\\PycharmProjects\\pythonProject2\\vuz_6sem\\py_vuz\\ind5\\db01.db') as con:
    c = con.cursor()
    xml_file = 'C:\\Users\\sezen\\PycharmProjects\\pythonProject2\\vuz_6sem\\py_vuz\\ind5\\table.xml'
    print(xml_file)
    doc = xml.dom.minidom.parse(xml_file)
    places = doc.getElementsByTagName('record')
    for place in places:
        place_id = place.getAttribute('id')
        plac = place.getElementsByTagName('place')[0].childNodes[0].data
        col = place.getElementsByTagName('col')[0].childNodes[0].data
        print(place_id, plac, col)
    c.execute('INSERT INTO places(place, col) values(?,?)', (plac, int(col)))
    con.commit()
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