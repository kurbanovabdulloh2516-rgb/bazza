import sqlite3 # мы ипортируем стореную в пайтон базу данных sqlite3

connect = sqlite3.connect('abdullokh.db') # 
cousor = connect.cursor()


cousor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age TEXT
)
''')



cousor.execute('INSERT INTO users (name,age) VALUES (?,?)',('MAX',3))
cousor.execute('INSERT INTO users (name,age) VALUES (?,?)',('MAX',3 ))
connect.commit()