import xml.dom.minidom
# Создаем XML-документ
doc = xml.dom.minidom.Document()
# Создаем корневой элемент
root = doc.createElement('table')
doc.appendChild(root)
data = [
 {'ID': '1', 'Name': 'Alice', 'Age': '25'},
 {'ID': '2', 'Name': 'Bob', 'Age': '30'},
 {'ID': '3', 'Name': 'Charlie', 'Age': '35'}
]
for row in data:
  record = doc.createElement('record')
  root.appendChild(record)

  for key, value in row.items():
    print(row, type(row))
    print(key, type(key))
    print(value, type(value))
    element = doc.createElement(key)
    element.appendChild(doc.createTextNode(value))
    record.appendChild(element)