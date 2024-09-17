"""
Crie uma estrutura para uma fila ligada simples e implemente a inserção,
remoção de elementos e a impressão dos elementos em ordem. Utilize dois
atributos para referenciar o início e final da fila. 

"""

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None 

class FilaLigada:

    def __init__(self):
        self.inicio = None
        self.final = None

    def add(self, valor):

        novo = Node(valor)

        if self.inicio == None:
            self.inicio = novo
            self.final = novo
        else:
            self.final.next = novo
            self.final = novo

    def printList(self):
        aux = self.inicio 

        while aux.next != None:
            print(aux.valor, end=" -> ")
            aux = aux.next
        print(self.final.valor)
        
    def remove(self):

        if self.inicio is None:
            print("Fila Vazia!")
            return 
        
        self.inicio = self.inicio.next 
        
        if self.inicio is None:
            self.final = None
        

fl = FilaLigada()

fl.add(1)
fl.add(2)
fl.add(3)
fl.add(4)
fl.add(5)
fl.add(6)

fl.printList()

fl.remove()

fl.printList()





