import sqlite3 as sql 

boglanish = sql.connect("yangi.db")

malumot = boglanish.cursor()

malumot.execute('''
CREATE TABLE IF NOT EXISTS Talaba(
    ism TEXT,
    familiya TEXT,
    yosh INTEGER,
    kurs INTEGER,
    guruhi TEXT
)''')

malumot.execute('''
CREATE TABLE IF NOT EXISTS Programmes(
    ism TEXT,
    familiya TEXT,
    yosh INTEGER,
    yonalishi TEXT,
    darajasi TEXT
)''')

malumot.execute('''
CREATE TABLE IF NOT EXISTS Bekorchilar(
    ism TEXT,
    familiya TEXT,
    yosh INTEGER,
    uxlashi INTEGER
)''')

malumot.execute('''
CREATE TABLE IF NOT EXISTS Uchuvchilar(
    ism TEXT,
    familiya TEXT,
    yosh INTEGER,
    samalyot nomi TEXT,
    tajribasi INTEGER
)''')

malumot.execute('''
CREATE TABLE IF NOT EXISTS Quruvchilar(
    ism TEXT,
    familiya TEXT,
    yosh INTEGER,
    soni INTEGER
)''')

malumot.execute('''
CREATE TABLE IF NOT EXISTS Hakkerlar(
    ism TEXT,
    familiya TEXT,
    yosh INTEGER,
    nomi TEXT
)''')

malumot.execute('''
CREATE TABLE IF NOT EXISTS Gulchilar(
    dokoni TEXT 
    gullari TEXT
    gullari soni INTEGER
)
''')