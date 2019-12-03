import sqlite3

def registrarSenhaMaster():
    masterPassword = 123456

    conn = sqlite3.connect("passwords.db")

    conn.execute(f"INSERT INTO master VALUES('{masterPassword}')")
    conn.commit()

    cur = conn.execute("SELECT * FROM master")

    if len(cur.fetchall()) == 1:
        try:
            question = str(input("A senha master padrão é 123456, deseja alterar isso ? [S/N]\n"))
            if question in 'Ss':
                masterPassword = input("Digite a nova senha master: ")
                conn.execute(f"UPDATE master WHERE masterpassword='123456' SET masterpassword='{masterPassword}'")
                conn.commit()
            print("SUCESSO!")

        except:
            print("ERRO!")
    conn.close()