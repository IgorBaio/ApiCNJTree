from treelib import Node, Tree
import Database
import json
from flask import Flask, jsonify
import PocArvore as poc

import re

app = Flask(__name__)

class Item(object):
    def __init__(self, codItem: int, codItemPai: int, nome: str, status: str, glossario: str):
        self.codItem = codItem
        self.codItemPai = codItemPai
        self.nome = nome
        self.status = status   
        self.glossario = glossario
    
nodeGroup=[]
def GetTree():
    tree = Tree()
    tree.create_node(0,0,data=Item(0,0,"Arvore CNJ",None,None))
    return tree
def GetDataSet(item):
    dataSetMyTree = Database.GetDataSet(item)
    return dataSetMyTree


def Main(dataSetMyTree):
    for vItem in dataSetMyTree:
        codItem = vItem[0]
        codItemPai = vItem[1]
        nome = vItem[2]
        status=vItem[3]
        glossario = vItem[4]

        if codItemPai is None:
            codItemPai = 0

        nItem = Item(codItem, codItemPai,nome,status,glossario)
        nodeGroup.append(nItem)

def MontaArvore(lista, tree = False):
    listaDeNodesAux = []
    for node in lista:
        try:
            tree.create_node(node.codItem,node.codItem,parent=node.codItemPai,data=node)
        except:
            listaDeNodesAux.append(node)
    
    if listaDeNodesAux.__len__() > 0 :
        MontaArvore(listaDeNodesAux, tree)

def getNode(cod_item, tree):
    node = tree.get_node(cod_item)
    return node

def getPath(cod_item, item):
    try:
        dataSet = GetDataSet(item)
        Main(dataSet)
        tree = GetTree()
        MontaArvore(nodeGroup, tree)
        node = getNode(cod_item, tree)
        nodeGroup.clear()
        
        return buildPathFodase(node,tree)
    except:
        return "Item não encontrado"

def isLeaf(node,tree):
    if node in tree.rsearch():
        return True
    else:
        return False

conjNodes = []
def buildPathFodase(node, tree):
    global nodePath
    conjNodes.append(node)

    if node.fpointer.__len__() == 0: 
        nodePath = node.data.nome
        buildPathFodase(getNode(node.bpointer,tree), tree)
    elif not node.bpointer == 0 and not node.identifier == 0:
        if node == conjNodes[0]:
            nodePath = node.data.nome 
        else:
            nodePath = node.data.nome + '/' + nodePath
        buildPathFodase(getNode(node.bpointer,tree),tree)
    elif not node.is_root() or node.bpointer == 0 :
        if node == conjNodes[0]:
            nodePath = node.data.nome 
        else:
            nodePath = node.data.nome + '/' + nodePath
            buildPathFodase(getNode(node.bpointer,tree),tree)
    
    conjNodes.clear()
    tree = None
    return nodePath


def SaveFile(diretorio, tree):
    sub_t = tree.subtree(0)
    sub_t.save2file(diretorio+"\\treeJsonClass4.txt", data_property="nome")
    sub_t.show(data_property="nome")


def PerguntaUsuario(item):
    try:
        codItem = int(input("Codigo do assunto a ser buscado: "))
        printPATH(codItem, item)
    except:
        print("Nao foi possivel buscar esse dado\n")
            
        
def printPATH(codItem, item):
    print("\n\n",getPath(codItem, item),"\n\n")

def jsonApiItems(codItem, item):
    path = getPath(codItem, item)
    return path

def jsonApiInsert():
    return poc.Run()


@app.route('/Assuntos=<int:id>', methods=['GET'])
def getAssuntos(id):
    conjNodes.clear()
    return jsonify(jsonApiItems(id, "Assuntos")), 200

@app.route('/Classes=<int:id>', methods=['GET'])
def getClasses(id):
    conjNodes.clear()
    return jsonify(jsonApiItems(id, "Classes")), 200

@app.route('/InsercaoArvore', methods=['GET'])
def GetInsert():
    return jsonify(jsonApiInsert()), 200

if __name__ == '__main__':
    app.run(debug=True)