"""
Crie uma simulação de um sistema de atendimento de banco com a estrutura
de fila criada anteriormente, onde novos clientes são adicionados e atendidos
sequencialmente ao removê-los da fila. 

"""

class Node:
    def __init__(self, client):
        self.client = client
        self.next = None

class FilaClient:
    def __init__(self):
        self.inicio = None 

    def add(self, client):

        novo = Node(client)

        if self.inicio == None:
            self.inicio = novo
        else:
            aux = self.inicio
            while aux.next:
                aux = aux.next
            aux.next = novo 

    def remove(self):
        if self.inicio == None:
            return print("Fila Vazia!")
        self.inicio = self.inicio.next

    def printFila(self):
        aux = self.inicio 
        print("Fila de Atendimento")
        while aux != None:
            print(aux.client, end=" -> ")
            aux = aux.next
        print()

############ SIMULACAO ##############

fl = FilaClient()

def addClient():
    fl.add(str(input("Insira um Nome: "))) 

def attendClient():
    fl.remove()

def listClient():
    fl.printFila()

def simula():

    print("--------- Menu de Gerenciamento ---------\n")
    opt = int(input("[1] Adicionar Clientes\n[2] Atender Clientes\n[3] Listar Clientes\n[4] Sair do Sistema\n"))
    
    if opt == 1:
        addClient()
    
    if opt == 2:
        attendClient()

    if opt == 3:
        listClient()

    if opt == 4:
        return print("Operacao Finalizada!")

    simula()

# Teste

simula()    




