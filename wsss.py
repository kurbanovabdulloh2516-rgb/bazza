import sqlite3

connect = sqlite3.connect('kurbanov.db')
cousor = connect.cursor()


cousor.execute('''
CREATE TABLE IF NOT EXISTS abdullokh (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    age INTEGER,
    number TEXT,
    class TEXT,
    email TEXT,
    parents_phone TEXT,
    school TEXT
)
''')

cousor.execute('INSERT INTO abdullokh (name,surname,age,number,class,email,parents_phone,school) VALUES (?,?,?,?,?,?,?,?)',('AYBEK','TOKTOSUNOV', 12, '0555123456', '8B', 'AYBER14@gmail.com', '0555123987', 'SEMA'))
cousor.execute('INSERT INTO abdullokh (name,surname,age,number,class,email,parents_phone,school) VALUES (?,?,?,?,?,?,?,?)',('Alina', 'Mambetova', 15, '0700654321', '9A', 'alina.m15@gmail.com', '0502987123', 'SEMA'))
cousor.execute('INSERT INTO abdullokh (name,surname,age,number,class,email,parents_phone,school) VALUES (?,?,?,?,?,?,?,?)',('Nursultan','Esenbaev', 13, '0703987654', '7C','nursultan13@bk.ru', '0202654789', 'SEMA'))
cousor.execute('INSERT INTO abdullokh (name,surname,age,number,class,email,parents_phone,school) VALUES (?,?,?,?,?,?,?,?)',('Begimai', 'Kubatova', 14, '0777445566', '8A', 'begimai.k14@gmail.com', '0888112233', 'SEMA'))
cousor.execute('INSERT INTO abdullokh (name,surname,age,number,class,email,parents_phone,school) VALUES (?,?,?,?,?,?,?,?)',('Ermek', ' Sadykov', 16, '0666998877', '10B', 'ermek16@list.ru', '0550332211', 'SEMA'))
cousor.execute('INSERT INTO abdullokh (name,surname,age,number,class,email,parents_phone,school) VALUES (?,?,?,?,?,?,?,?)',(' Dinara', 'Toktobolotova', 15, '0501778899', '9B', 'dinara15@mail.ru', '0999888777', 'SEMA' ))
cousor.execute('INSERT INTO abdullokh (name,surname,age,number,class,email,parents_phone,school) VALUES (?,?,?,?,?,?,?,?)',(' Azat', 'Zhunusov', 16, '0553112233', '7A', 'azat13@gmail.com', '0706108859', 'SEMA'))
cousor.execute('INSERT INTO abdullokh (name,surname,age,number,class,email,parents_phone,school) VALUES (?,?,?,?,?,?,?,?)',(' Aigul', 'Sultanbekova', 16, '0702667788', '10A', 'aigul16@bk.ru', '0999111222', 'SEMA'))
connect.commit()