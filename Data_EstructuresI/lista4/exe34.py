
"""
Implemente um programa que receba duas filas to tipo encadeadas e
concatene-as em uma nova estrutura de fila. 

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Fila:
    def __init__(self):
        self.inicio = None 

    def add(self, val):
        novo = Node(val)\
        
        if self.inicio == None:
            self.inicio = novo
        else: 
            aux = self.inicio
            while aux.next:
                aux = aux.next
            aux.next = novo
    
    def printFila(self):
        aux = self.inicio 
        while aux:
            print(aux.val, end=" -> ")
            aux = aux.next
        print()

    def concatena(self, f2):
    
        f3 = Fila()

        aux = self.inicio

        while aux:
            f3.add(aux.val)
            aux = aux.next

        aux = f2.inicio 

        while aux:
            f3.add(aux.val)
            aux = aux.next

        return f3.printFila()

    
f1 = Fila()
f2 = Fila()

f1.add(1)
f1.add(2)
f1.add(3)
f1.add(4)
f1.add(5)
f2.add(1)
f2.add(2)
f2.add(3)
f2.add(4)
f2.add(5)
f1.concatena(f2)