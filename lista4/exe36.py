"""
Implemente um programa que recebe duas filas e intercala seus elementos
em uma nova fila encadeada. 
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class FilaLigada:
    def __init__(self):
        self.inicio = None

    def add(self, val):
        novo = Node(val)

        if self.inicio is None:
            self.inicio = novo
        else:
            aux = self.inicio
            while aux.next:
                aux = aux.next
            aux.next = novo  

    def imprimir(self):
        
        aux = self.inicio
        while aux:
            print(aux.val, end=" -> ")
            aux = aux.next
        print()

    def intercalar(self, fila):
        nova_lista = FilaLigada()
        aux = self.inicio 
        aux2 = fila.inicio

        i = 0

        while i != 1:
            if aux is not None:
                nova_lista.add(aux.val)
                aux = aux.next
       
            if aux2 is not None:
                nova_lista.add(aux2.val)
                aux2 = aux2.next
      
            if aux is None and aux2 is None:
                i = 1 

        return nova_lista.imprimir()
    

fl1 = FilaLigada()
fl2 = FilaLigada()

fl1.add(1)
fl1.add(3)
fl1.add(5)
fl1.add(7)
fl1.add(9)

fl1.imprimir()


fl2.add(2)
fl2.add(4)
fl2.add(6)
fl2.add(8)
fl2.add(10)
fl2.add(11)
fl2.add(12)
fl2.add(13)


fl2.imprimir()

fl1.intercalar(fl2)




        
    





    