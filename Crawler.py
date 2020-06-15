import urllib3
from bs4 import BeautifulSoup

import re

def formataURL(action):
    url = "https://www.cnj.jus.br/sgt/"+action
    return url

def GetTexto(soup):
    for tags in soup(['html', 'body']):
        tags.decompose()
    return ' '.join(soup.stripped_strings)

def GetUrlOfDumps(soup):
    dumps = []
    links = soup.find_all('input')
    for link in links:
       atributo = (str(link.get("value")))
       if re.search("\d{1,2}\_dump_estrutura\.sql", atributo) or re.search("\d{1,2}\_dump_dados\.sql", atributo):
           atributo = formataURL(atributo)
           
           dumps.append(atributo)
    return dumps

def getSoup(pagData):
    soup = BeautifulSoup(pagData, "lxml")  
    return soup
    
#def GetDataOfDumps(soup)
    

def crawl(pagina):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    http = urllib3.PoolManager()
    try:
        dados_pagina = http.request('GET', pagina)
    except:
        print("Erro ao abrir a página"+pagina)
    return dados_pagina.data
    
        
# pagData = crawl('https://www.cnj.jus.br/sgt/versoes.php')
# soups = getSoup(pagData)
# linkOfDumps = GetUrlOfDumps(soups)
# dataDump = []
# for dump in linkOfDumps:
#     data = crawl(dump)
#     dataSoup = getSoup(data)
#     #print (dataSoup.contents)
#     dataDump.append(dataSoup.contents)
