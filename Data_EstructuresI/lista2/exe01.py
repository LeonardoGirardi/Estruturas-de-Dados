"""
Implemente as estruturas de dados das atividades 01 e 02 (IP-01).

Desenhe uma estrutura de dados para representar um PET, com nome e ano de
nascimento.

Crie uma estrutura de dados que represente uma vacina contendo tipo, dosagem, e o
animal PET a que foi aplicado (utilize a estrutura criada anteriormente).

"""

class Pet:

    def __init__(self, name, species, birthdate):

        self.name = name
        self.species = species
        self.birthdate = birthdate

    def printPet(self):

        print(self.name, self.species, self.birthdate)


class Vacina(Pet):
    def __init__(self, name, species, birthdate, tipo, dosagem):

        super().__init__(name, species, birthdate)
        self.tipo = tipo
        self.dosagem = dosagem

    def printVacina(self):
        print("Vacina:", self.tipo, "- Dosagem:", self.dosagem)


pet1 = Pet('Bob','Cachorro','10/05/19')
pet2 = Pet('Con','Cachorro','20/05/19')

pet1 = Vacina('Bob', 'Cachorro', '10/05/19', 'Antirrábica', '10 ml')
pet2 = Vacina('Con', 'Cachorro', '20/05/19', 'Polivalente', '15 ml')

pet1.printPet()
pet1.printVacina()
