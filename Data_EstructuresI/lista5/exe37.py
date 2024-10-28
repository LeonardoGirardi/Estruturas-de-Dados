"""
Crie uma estrutura para uma pilha ligada simples e implemente a inserção,
remoção de elementos, um método para verificar se a pilha está vazia e a
impressão dos elementos em ordem. Utilize apenas um atributo para
referenciar o topo da pilha. 
"""

class Node: 
    def __init__(self, val):
        self.val = val
        self.prev = None

class Pilha:
    def __init__(self):
        self.primeiro = None

    def add(self,val):
        novo = Node(val)

        if self.primeiro is None:
            self.primeiro = novo
        else:
            novo.prev = self.primeiro
            self.primeiro = novo

    def checagem(self):
        if self.primeiro is None:
            print("Lista Vazia") 
        else:               
            print("A Lista contem elementos")                

    def remove(self):

        if self.primeiro is None:
            print("Lista Vazia")                
        else:
            self.primeiro = self.primeiro.prev
    
    def printP(self):

        if self.primeiro is None:
            print("Lista Vazia!")

        aux = self.primeiro 

        while aux:
            print(aux.val, end=" -> ")
            aux = aux.prev
        print()
            

pl = Pilha()
pl.add(1)
pl.add(2)
pl.add(3)
pl.add(4)

pl.printP()

pl.remove()

pl.printP()

pl.checagem()
