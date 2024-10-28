"""Implemente um método de ordenação para a lista de datas do exercício 09."""

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

    def ordenar(self):
        aux = True
        while aux:
            aux = False
            atual = self.primeiro
            while atual.prox:
                if (atual.ano, atual.mes, atual.dia) < (atual.prox.ano, atual.prox.mes, atual.prox.dia):
                    atual.dia, atual.mes, atual.ano, atual.prox.dia, atual.prox.mes, atual.prox.ano = \
                    atual.prox.dia, atual.prox.mes, atual.prox.ano, atual.dia, atual.mes, atual.ano
                    aux = True
                atual = atual.prox

    def imprimir(self):
        aux = self.primeiro
        while aux:
            print(aux)
            aux = aux.prox
        print()

    


dt = Lista()

dt.add(10,12,2020)
dt.add(10,11,2021)
dt.add(10,10,2025)
dt.add(10,9,2019)

dt.imprimir()

dt.ordenar()

dt.imprimir()