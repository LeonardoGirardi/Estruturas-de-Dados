"""
Implemente uma função que cria uma nova pilha fazendo uma cópia da pilha
e elementos. 
"""

class Node:
    def __init__(self, val):
        self.val = val 
        self.prev = None


class Pilha:
    def __init__(self):
        self.primeiro = None

    def inserir(self, val):
        novo = Node(val)

        if self.primeiro is None:
            self.primeiro = novo 
        else:
            novo.prev = self.primeiro
            self.primeiro = novo 

    def imprimir(self):
        aux = self.primeiro

        while aux:
            print(aux.val, end="->")
            aux = aux.prev
        print()


    
def copia(pilha):
    novo = Pilha()
    novo = pilha
    return novo



pl = Pilha()

pl.inserir(1)
pl.inserir(2)
pl.inserir(3)
pl.inserir(4)

pl.imprimir()

copia(pl)




