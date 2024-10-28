"""  Crie  uma  estrutura  de  dados  de  uma  fila  circular  que  representa  processos 
     em  um  computador  e  implemente também a operação de rotação
   (mover o primeiro elemento para o final). """

class Node:
    def __init__(self, processo: int):
        self.processo = processo
        self.prox = None

    def __str__(self):
        return f"Processo: {self.processo}"

class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
    
    def add(self, processo):

        novo = Node(processo)

        if self.primeiro is None:
            self.primeiro = novo
            self.ultimo = novo
            self.ultimo.prox = self.primeiro 
        else:
            self.ultimo.prox = novo
            self.ultimo = novo
            self.ultimo.prox = self.primeiro

    def rotacionar(self):
        if self.primeiro is not None and self.primeiro != self.ultimo:
            self.ultimo = self.primeiro
            self.primeiro = self.primeiro.prox

    def imprimir(self):
        aux = self.primeiro  
        while True:
            print(aux)
            aux = aux.prox
            if aux == self.primeiro:
                break
        print()

f = Fila()

f.add(1)
f.add(2)
f.add(3)
f.add(4)
f.add(5)

f.imprimir()

f.rotacionar()

f.imprimir()

f.rotacionar()

f.imprimir()
