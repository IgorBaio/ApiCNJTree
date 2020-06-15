import mysql.connector
from mysql.connector import Error
import Crawler


import re

dumpEstrutura =""
dumpDados =""
log = []


def GetDumpsOfCrawler():
    pagData = Crawler.crawl('https://www.cnj.jus.br/sgt/versoes.php')
    soups = Crawler.getSoup(pagData)
    linkOfDumps = Crawler.GetUrlOfDumps(soups)
    dataDump = []
    for dump in linkOfDumps:
        data = Crawler.crawl(dump)
        dataSoup = Crawler.getSoup(data)
        if re.search("\d{1,2}\_dump_estrutura\.sql", dump):
            ExecuteQueryEstrutura(dataSoup.text)
        else:
            ExecuteQueryDados(dataSoup.text)



directory = "C:\\Users\\U6104968.TEN\\Downloads\\AtualizaCnj21-03-2020" #input("\n\nDigite seu repositorio onde estao os dumps: ")

# def ExecuteDumpEstrura():
#     dumpEstrutura = "FooPistola.sql" #input("\n\nNome do arquivo de estrutura com extensao: ")
#     dumpEstrutura = directory+"\\"+dumpEstrutura
#     arquivo = open(dumpEstrutura)
#     dumpEstrutura = arquivo.read()
#     ExecuteQueryEstrutura(dumpEstrutura)

# def ExecuteDumpDados():
#     dumpDados = "FooPistolaDados5.sql" #input("\n\nNome do arquivo de dados com extensao: ")
#     dumpDados = directory+"\\"+dumpDados
#     arquivo = open(dumpDados, encoding="utf8")
#     dumpDados = arquivo.read()
#     ExecuteQueryDados(dumpDados)

def ExecuteQueryEstrutura(query):
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='')
    cursor = connection.cursor(buffered=True)
    query = FormataQuery(query, "E")
    i=0
    for cmd in query:
        try:
            cursor.execute(cmd)
            print(i)
            i+=1
        except Error as e:
            log.append(e)
        finally:
            connection.commit()
    connection.close()

def ExecuteQueryDados(query):
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='')
    cursor = connection.cursor(buffered=True)
    query = FormataQuery(query, "D")
    i=0
    for cmd in query:
        try:
            cursor.execute(cmd)
            print(i)
            i+=1
        except Error as e:
            log.append(e)
        finally:
            connection.commit()
    connection.close()

def FormataQuery(query, indicadorQuery):
    if indicadorQuery == "D":
        commands = []
        query = re.split("(?<=['|L]\));\n[IN]", query)
        for queryAux in query:
            if not re.search("(?<=['|L]\));\s\\n[IN]", queryAux) is None :
                queryAux = re.split("(?<=['|L]\));\s\\n[IN]", queryAux)
                count = 0
                while count < queryAux.__len__():
                    commands.append(queryAux[count])
                    count += 1
            elif not re.search("(?<=[0-1]);\s\\n[IN]", queryAux) is None :
                queryAux = re.split("(?<=[0-1]);\s\\n", queryAux)

                if (queryAux[0].startswith("NSERT")) and not (queryAux[1].startswith("NSERT")):
                    unionOfQuery = queryAux[0] + queryAux[1]
                    unionOfQuery = re.sub("NSERT", "INSERT", unionOfQuery)
                    commands.append(unionOfQuery)
                
                count = 0
                while count < queryAux.__len__():
                    if not re.search(";\s\\n[SET]", queryAux[count]) is None :
                        newQueryAux = re.split(";\s\\n[SET]", queryAux[count])
                        print()
                        
                        for newQuery in newQueryAux:
                            print()
                            if not re.search("ET", newQuery) is None:
                                newCommand = re.sub("ET", "SET", newQuery) 
                                if newCommand.__len__() > 0 :
                                    commands.append(newCommand)
                            else:
                                commands.append(newQuery)
                    else:
                        commands.append(queryAux[count])
                    count += 1
                
            else:
                if not re.search("NSERT", queryAux) is None:
                    queryAux = re.sub("NSERT", "INSERT", queryAux)
                # if not (queryAux.startswith("NSERT")):
                #     q = queryAux[count - 1] + queryAux[count]
                #     print
                #     commands.append(q)
                commands.append(queryAux)
        return commands
    else:
        commands = []
        query = re.split(";\n", query)
        for queryAux in query:
            if not re.search(";\s\\n", queryAux) is None :
                queryAux = re.split(";\s\\n", queryAux)
                count = 0
                while count < queryAux.__len__():
                    commands.append(queryAux[count])
                    count += 1
            else:
                commands.append(queryAux)
        return commands


#  def createdatabase():
#     sqlcmd = "create database `foopistoladata`"
#     connection = mysql.connector.connect(host='localhost',
#                                         user='root',
#                                         password='')
#     cursor = connection.cursor()
#     try:
#         cursor.execute(sqlcmd)
#     except error as e:
#             print('deu merda aqui', e)
#     finally:
#         connection.commit()
#         connection.close()

def Run():
    try:
        #CreateDataBase()
        # ExecuteDumpEstrura()
        # ExecuteDumpDados()
        GetDumpsOfCrawler()
        file = open(directory+"\\log.txt", "w+")
        file.write(str(log))
        file2 = open(directory+"\\log2.txt", "w+")
        for dado in log:
            file2.write(str(dado))    
            

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        
            print("\n\nMySQL connection is closed")
# Run()