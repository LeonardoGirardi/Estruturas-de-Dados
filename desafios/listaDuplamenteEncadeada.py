class Node:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.proximo = None
        self.anterior = None


class ListaDuplaEncadeada:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, nome, idade):
        novo = Node(nome, idade)

        if self.head == None:
            self.head = novo
            self.tail = novo

        else:
            self.tail.proximo = novo
            novo.anterior = self.tail
            self.tail = novo

    def imprimir(self):
        atual = self.head
        while atual != None:
            print(atual.nome, atual.idade)
            atual = atual.proximo

    def imprimirR(self):
        atual = self.tail
        while atual != None:
            print("Nome: ", atual.nome, " Idade: " , atual.idade)
            atual = atual.anterior



ls = ListaDuplaEncadeada()

ls.add("Pessoa1", 12)
ls.add("Pessoa2", 23)
ls.add("Pessoa3", 43)

ls.imprimir()
ls.imprimirR()



