"""Crie  uma  estrutura  de  dados  que  represente  uma  lista  encadeada  de  datas  utilizando  
a  estrutura  criada no exercício 03. Implemente um programa com as operações de fila para a lista de datas. """

class Data: 
    def __init__(self, dia: int, mes: int, ano:int):
        self.dia = dia 
        self.mes = mes
        self.ano = ano 
        self.prox = None 

    def __str__(self):
        return f"Data: {self.dia}/{self.mes}/{self.ano}"
    
class Lista:
    def __init__(self):
        self.primeiro = None

    def add(self, dia, mes, ano):
        novo = Data(dia, mes, ano)
        
        if self.primeiro is None:
            self.primeiro = novo
        else:
            aux = self.primeiro
            while aux.prox:
                aux = aux.prox
            aux.prox = novo 

    def remove(self):
        if self.primeiro is not None:
            self.primeiro = self.primeiro.prox
            return
        print("Lista Vazia: Nada para remover")

    def imprimir(self):
        aux = self.primeiro
        while aux:
            print(aux)
            aux = aux.prox
        print()


dt = Lista()

dt.add(10,12,2020)
dt.add(10,11,2020)
dt.add(10,10,2020)
dt.add(10,9,2020)

dt.imprimir()

dt.remove()

dt.imprimir()