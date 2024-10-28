"""  Crie uma estrutura de dados para representar uma data com dia, mês e ano. """

class Data: 
    def __init__(self, dia: int, mes: int, ano:int):
        self.dia = dia 
        self.mes = mes
        self.ano = ano 

    def __str__(self):
        return f"Data: {self.dia}/{self.mes}/{self.ano}"
    
           