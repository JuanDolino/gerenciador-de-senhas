import sqlite3
from registerMasterPassword import registrarSenhaMaster

def databaseInit():
    conn = sqlite3.connect("passwords.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS datauser(
        user     TEXT,
        password INT,
        service  TEXT
    )''')

    conn.execute('''CREATE TABLE IF NOT EXISTS master(
        masterpassword INT
    )''')

databaseInit()
registrarSenhaMaster()