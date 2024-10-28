"""Crie  uma  estrutura  de  dados  que  represente  uma  vacina  contendo  tipo,  e  o
  animal  PET  a  que  foi  aplicado (utilize a estrutura criada anteriormente)."""

class Pet:
    def __init__(self, nome: str, ano_nasc: int):
        self.nome = nome 
        self.ano_nasc = ano_nasc

    def __str__(self):
        return f"Nome: {self.nome}  || Ano de Nasciemento: {self.ano_nasc}"
    

class Vacina:
    def __init__(self, tipo: str, pet: Pet):
        self.tipo = tipo
        self.pet = pet

    def __str__(self):
        return f"""
        ______Vacinacao_____
        Pet: {self.pet.nome}              
        Tipo: {self.tipo}             `
    """
    
p1 = Pet("Bob", 2020)

vac1 = Vacina("Raiva", p1)

print(p1)

print(vac1)


        