import mysql.connector as mysql
from mysql.connector import Error

def CreateConnection():
    connection = mysql.connect(host='localhost',
                                database='sgt_consulta_old_certo21_03_2020',
                                user='root',
                                password='')
    return connection

def GetCodItem():
    connection = CreateConnection()
    query = ("""select cod_item from itens i
     left join assuntos a on a.cod_assunto = i.cod_item
     where i.tipo_item = 'A' """)
    cursor = connection.cursor(buffered=True)
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def GetCodItemPai():
    connection = CreateConnection()
    query = ("""select cod_item_pai from itens i
     left join assuntos a on a.cod_assunto = i.cod_item
     where i.tipo_item = 'A' """)
    cursor = connection.cursor(buffered=True)
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def GetNome():
    connection = CreateConnection()
    query = ("""select nome from itens i
     left join assuntos a on a.cod_assunto = i.cod_item
     where i.tipo_item = 'A' """)
    cursor = connection.cursor(buffered=True)
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def GetDataSet(item):
    if item == "Assuntos":

        connection = CreateConnection()
        query = ("""select cod_item, cod_item_pai, nome, situacao, a.glossario from itens i
        left join assuntos a on a.cod_assunto = i.cod_item
        where i.tipo_item = 'A' 
        order by cod_item_pai""")
        cursor = connection.cursor(buffered=True)
        cursor.execute(query)
        result = cursor.fetchall()
       
        connection.commit()
        connection.close()
        return result
    else:
        connection = CreateConnection()
        query = ("""select cod_item, cod_item_pai, nome, situacao, c.glossario from itens i
        left join classes c on c.cod_classe = i.cod_item
        where i.tipo_item = 'C' 
        order by cod_item_pai""")
        cursor = connection.cursor(buffered=True)
        cursor.execute(query)
        result = cursor.fetchall()
        
        connection.commit()
        connection.close()
        return result