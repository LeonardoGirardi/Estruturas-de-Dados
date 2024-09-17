"""
Crie um programa que receba uma pilha com a estrutura criada
anteriormente e crie uma nova pilha em ordem inversa utilizando os métodos
de empilhar e desempilhar.
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

    def desempilhar(self):
        if self.primeiro is None:
            print("Lista Vazia")
            return None
        else:
            valorRemovido = self.primeiro.val
            self.primeiro = self.primeiro.prev
            return valorRemovido
        
    def imprimir(self):
        aux = self.primeiro

        while aux:
            print(aux.val, end=" -> ")
            aux = aux.prev
        print()

    def inverter(self):
        novo = Pilha()
        aux = self.primeiro
        while aux:
            valor = self.desempilhar()
            novo.empilhar(valor)
            aux = aux.prev
        
        return novo.imprimir()
        

    
pl = Pilha()

pl.empilhar(1)
pl.empilhar(2)
pl.empilhar(3)
pl.empilhar(4)

pl.imprimir()

pl.inverter()


