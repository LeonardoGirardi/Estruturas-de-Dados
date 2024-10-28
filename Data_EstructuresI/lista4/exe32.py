"""
Crie uma estrutura para uma fila ligada simples e implemente a inserção,
remoção de elementos e a impressão dos elementos em ordem. Utilize
apenas um atributo para referenciar o início da fila

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Fila:
    def __init__(self):
        self.inicio = None

    def add(self, val):

        novo = Node(val)

        if self.inicio == None:
            self.inicio = novo
        else:
            aux = self.inicio
            while aux.next:
                aux = aux.next
            aux.next = novo




    def remove(self):
        if self.inicio == None:
            print("Lista Vazia")
        self.inicio = self.inicio.next

    def printFila(self):
        aux = self.inicio
        while aux != None:
            print(aux.val, end=" -> ")
            aux = aux.next
        print()


fila = Fila()

fila.add(1)
fila.add(2)
fila.add(3)
fila.add(4)

fila.printFila()

fila.remove()

fila.printFila()


