# import sqlite3 # мы ипортируем стореную в пайтон базу данных sqlite3

# connect = sqlite3.connect('asa.db') # 
# cousor = connect.cursor()


# cousor.execute('''
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     age TEXT
# )
# ''')



# cousor.execute('INSERT INTO users (name,age) VALUES (?,?)',('MAX',3))
# cousor.execute('INSERT INTO users (name,age) VALUES (?,?)',('MAX',3 ))

# cousor.execute("UPDATE users SET name=?, age=? WHERE id=?",('super mario',100,2))

# cousor.execute("DELETE FROM users WHERE id=?", (4,))

# connect.commit()