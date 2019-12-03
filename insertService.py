import sqlite3
from time import sleep

def insertService():
    try:
        conn = sqlite3.connect("passwords.db")

        user = input("USUÁRIO: ")
        password = input("SENHA: ")
        service = input("SERVIÇO: ")

        conn.execute(f"INSERT INTO datauser VALUES('{user}', '{password}', '{service}')")
        conn.commit()
        print("SUCESSO!")
        sleep(3)

    except:
        print("ERRO!")

    conn.close()
