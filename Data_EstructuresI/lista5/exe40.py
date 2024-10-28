"""
Crie um programa para combinar duas pilhas em uma. 
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None

class Pilha:
    def __init__(self):
        self.primeiro = None

    def empilhar(self, val):
        novo = Node(val)

        if self.primeiro is None:
            self.primeiro = novo 
        else:
            novo.prev = self.primeiro
            self.primeiro = novo

    def imprimir(self):
        aux = self.primeiro
        
        while aux: 
            print(aux.val ,end=" -> ")
            aux = aux.prev
        print()

    def combinar(self, pilha):
        novaPilha = Pilha()

        aux = self.primeiro

        while aux:
            novaPilha.empilhar(aux.val)
            aux = aux.prev
        
        aux2 = pilha.primeiro

        while aux2:
            novaPilha.empilhar(aux2.val)
            aux2 = aux2.prev

        return novaPilha.imprimir()


pl = Pilha()
pl2 = Pilha()

pl.empilhar(1)
pl.empilhar(2)
pl.empilhar(3)
pl.empilhar(4)

pl2.empilhar(1)
pl2.empilhar(2)
pl2.empilhar(3)
pl2.empilhar(4)

pl.combinar(pl2)