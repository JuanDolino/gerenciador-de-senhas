import sqlite3
from clearDisplay import clear

def registerMasterPassword():
    clear()
    conn = sqlite3.connect('passwords.db')
    cur = conn.execute("SELECT * FROM master")

    if len(cur.fetchall()) == 0:
        masterPassword = 123456

        conn.execute(f"INSERT INTO master VALUES('{masterPassword}')")
        conn.commit()

        try:
            question = str(input("A senha master padrão é 123456, deseja alterar isso ? [S/N]\n"))
            if question in 'Ss':
                masterPassword = input("Digite a nova senha master: ")
                conn.execute(f"UPDATE master SET masterpassword='{masterPassword}' WHERE masterpassword='123456'")
                conn.commit()
            print("SUCESSO ! SENHA CADASTRADA")

        except:
            print("ERRO!")
    conn.close()