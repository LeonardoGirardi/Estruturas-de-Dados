"""
Crie  um  programa  que  implemente  as  funções  de  uma  Pilha  (LIFO)
 utilizando  a  estrutura  de  dados  criada anteriormente. Operações: empilhar, desempilhar.
"""

class Node:
    def __init__(self, val: int):
        self.val = val
        self.prev = None

class Lista:
    def __init__(self):
        self.topo = None

    def empilhar(self, val):
        novo = Node(val)

        if self.topo is None:
            self.topo = novo
        else:
            novo.prev = self.topo
            self.topo = novo

    def desempilhar(self):
        if self.topo is not None:
            self.topo = self.topo.prev
        else:
            print("Pilha Vazia!")


    def imprimir(self):
        aux = self.topo
        while aux:
            print(aux.val, end=" -> ")
            aux = aux.prev
        print()



l1 = Lista()

l1.empilhar(1)
l1.empilhar(2)
l1.empilhar(3)
l1.empilhar(4)
l1.empilhar(5)
l1.empilhar(6)

l1.imprimir()

l1.desempilhar()

l1.imprimir()
