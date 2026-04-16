import mysql.connector
conexao = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    database='crudpython'
)
sql = conexao.cursor()

def sqlcreate():
    commandcreate = f'INSERT INTO usuarios (sqlname, sqlage, sqlcity) VALUES ("{dtname}", "{dtage}", "{dtcity}")'
    sql.execute(commandcreate)
    conexao.commit()

def sqlconsult():
    commandconsult = f'SELECT * FROM usuarios'
    sql.execute(commandconsult)

    resultado = sql.fetchall()

    print("\nTabelas")
    for linha in resultado:
        print(linha)

def congrats():
    print("Congratulations, the data was added with successfuly")

def options():
    return int(input("\n===== This is a database system :) ======\n\nWhich option you gonna to open\n 1.Create database | 2.Consult | 0.Finish\n"))

option = options()

while option != 0:

    if option == 1:
        dtname = input("This is the Name collumn, please enter a new name\n")
        dtage = input("This is the Age collumn, please enter a new age\n")
        dtcity = input("This is the City collumn, please enter a new name\n")
        
        sqlcreate()
        congrats()
        option = options()

    elif option == 2:
        sqlconsult()
        option = options()

    else:
        break