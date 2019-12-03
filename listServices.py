import sqlite3
from time import sleep

def listServices():
    conn = sqlite3.connect('passwords.db')
    cur = conn.execute("SELECT * FROM datauser")

    print('='*50)
    print(f'{"SERVIÇOS":>27}')
    print('='*50)


    if len(cur.fetchall()) == 0:
        print("NADA CADASTRADO")
        conn.close()
    
    else:
        cur = conn.execute("SELECT * FROM datauser")
        for i in cur:
            print(i[2])
        input("PRESSIONE QUALQUER TECLA: ")
