"""Crie  um  programa  que  implemente  as  funções  de  uma  Fila  (FIFO) 
 utilizando  a  estrutura  de  dados  criada anteriormente. Operações: adicionar e remover. """

class Node:
    def __init__(self, val: int):
        self.val = val
        self.prox = None 

class Lista:
    def __init__(self):
        self.primeiro = None

    def add(self, val):
        novo = Node(val)

        if self.primeiro is None:
            self.primeiro = novo
        else:
            aux = self.primeiro
            while aux.prox:
                aux = aux.prox
            aux.prox = novo

    def rem(self):
        if self.primeiro is not None:
            self.primeiro = self.primeiro.prox 
        else:
            print("Lista Vazia!")

    def imprimir(self):
        aux = self.primeiro
        while aux:
            print(aux.val, end=" -> ")
            aux = aux.prox
        print()

l1 = Lista()

l1.add(1)
l1.add(2)
l1.add(3)
l1.add(4)
l1.add(5)
l1.add(6)

l1.imprimir()

l1.rem()

l1.imprimir()