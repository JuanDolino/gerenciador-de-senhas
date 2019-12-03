import sqlite3
from time import sleep
from clearDisplay import clear

def recoverPassword():
    clear()
    conn = sqlite3.connect('passwords.db')
    cur = conn.execute("SELECT * FROM datauser")

    service = input("Qual serviço que você deseja recuperar a senha: ").lower()

    for i in cur:
        if i[2] == service:
            print("="*25)

            print(f"Usuário: {i[0]}")
            print(f"Senha: {i[1]}")
            print(f"Serviço: {service}")

    print("="*25)

    input("\nPressione qualquer tecla para continuar... ")
    