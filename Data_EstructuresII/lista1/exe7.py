"""Crie  uma  estrutura  de  dados  que  represente  uma  fila  de  pessoas  numa  agência  bancária,
contendo  o  seu  nome  e  número  da  conta.  Implemente  as  operações  d
e  Fila:  adicionar,  remover,  inicializar,  vazia (verifica se está vazia). """

class Pessoa:
    def __init__(self, nome: str, num_conta: str):
        self.nome = nome
        self.num_conta = num_conta
        self.prox = None


    def __str__(self):
        return f"Nome: {self.nome} || Conta: {self.num_conta}"

class Lista:
    def __init__(self):
        self.primeiro = None

    def inicializar(self):
        self.primeiro = None
        
    def verifica_status(self) -> str:
        if self.primeiro is None:
            return print("Lista Vazia")
        return print("A Lista contem elementos!")

    def add(self, nome, num_conta="0000"):
        novo = Pessoa(nome, num_conta)

        if self.primeiro is None:
            self.primeiro = novo
        else:
            aux = self.primeiro
            while aux.prox:
                aux = aux.prox
            aux.prox = novo

    def rem(self):
        if self.primeiro is not None:
            self.primeiro = self.primeiro.prox
        else:
            return print("Lista Vazia: Nada a Remover!")

    def imprimir(self):
        if self.primeiro is None:
            return print("Lista Vazia: Nada para Imprimir!") 
        
        aux = self.primeiro
        while aux:
            print(aux)
            aux = aux.prox
        print()
fila = Lista()

fila.add("Maria","2325")
fila.add("Jose","4565")
fila.add("Ana","1547")
fila.add("Volnei","2345")

fila.verifica_status()

fila.imprimir()

fila.rem()

fila.imprimir()

fila.inicializar()

fila.verifica_status()







    
