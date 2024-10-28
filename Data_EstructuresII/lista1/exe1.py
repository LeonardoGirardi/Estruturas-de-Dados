"""Crie uma estrutura de dados para representar um PET, com nome e ano de nascimento."""

class Pet:
    def __init__(self, nome: str, ano_nasc: int):
        self.nome = nome 
        self.ano_nasc = ano_nasc

    def __str__(self):
        return f"Nome: {self.nome} Ano de Nasciemento: {self.ano_nasc}"
    
