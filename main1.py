import sqlite3 as sql

boglanish = sql.connect("susys.db")

malumot = boglanish.cursor()

malumot.execute('''
CREATE TABLE IF NOT EXISTS Pupils(
    ism TEXT,
    familiya TEXT,
    yosh INTEGER
)
''')
#koment