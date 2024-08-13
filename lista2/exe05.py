"""
Desenvolva uma estrutura para uma tarefa simples (apenas uma descrição
da atividade). Depois crie um vetor adicionando novas instâncias de tarefas à
essa lista.
"""
class Comprar:
    def __init__(self, item, preco):
        self.item = item
        self.preco = preco

compra1 = Comprar('Carro', '60000')
compra2 = Comprar('Moto', '20000')
compra3 = Comprar('Macbook', '12000')

compras = [compra1, compra2, compra3]

"""
Implemente um método que imprima o vetor de tarefas criado na atividade
anterior com um número de contador. Exemplo:
1. Limpar a casa
2. Estudar estruturas de dados
3. Fazer um bolo
"""
for i in compras:
    print("Comprar: ", i.item, i.preco)



