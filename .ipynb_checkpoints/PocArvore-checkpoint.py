import mysql.connector
from mysql.connector import Error

dumpEstrutura =""
dumpDados =""
log = []

directory = raw_input("\n\nDigite seu repositorio onde estao os dumps: ")

def ExecuteDumpEstrura():
    dumpEstrutura = raw_input("\n\nNome do arquivo de estrutura com extensao: ")
    dumpEstrutura = directory+"\\"+dumpEstrutura
    arquivo = open(dumpEstrutura)
    dumpEstrutura = arquivo.read()
    ExecuteQuery(dumpEstrutura)

def ExecuteDumpDados():
    dumpDados = raw_input("\n\nNome do arquivo de dados com extensao: ")
    dumpDados = directory+"\\"+dumpDados
    arquivo = open(dumpDados)
    dumpDados = arquivo.read()
    ExecuteQuery(dumpDados)

def ExecuteQuery(query):
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='')
    cursor = connection.cursor()
    query = query.split(";")
    for cmd in query:
        try:
            cursor.execute(cmd)
        except Error as e:
                print(cmd,"\n")
                log.append(e)
        finally:
            connection.commit()
    connection.close()

# def CreateDataBase():
#     sqlcmd = "CREATE DATABASE `FooPistolaData`"
#     connection = mysql.connector.connect(host='localhost',
#                                          user='root',
#                                          password='')
#     cursor = connection.cursor()
#     try:
#         cursor.execute(sqlcmd)
#     except Error as e:
#             print('Deu merda aqui', e)
#     finally:
#         connection.commit()
#         connection.close()


try:
    #CreateDataBase()
    ExecuteDumpEstrura()
    ExecuteDumpDados()
    file = open(directory+"\\log.txt", "w+")
    file.write(log)
        

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    
        print("\n\nMySQL connection is closed")






