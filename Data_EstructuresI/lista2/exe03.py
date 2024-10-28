"""
Implemente as estruturas de Produto, Cliente e Pedido elaboradas na
atividade 04 (IP-01).

Imagine que você está desenvolvendo um sistema para uma loja online. Crie um
diagrama para representar as principais entidades do sistema. Considere que o sistema
deve lidar com Produtos, Clientes e Pedidos. Cada produto possui um nome, preço e
quantidade em estoque. Cada cliente é identificado por um número único e possui um
histórico de pedidos. Cada pedido é associado a um único cliente e contém vários
produtos.
"""

class Produtos:
    def __init__(self, nomeProduto, preco, estoque):
        self.nomeProduto = nomeProduto
        self.preco = preco
        self.estoque = estoque



class Clientes:
    def __init__(self, id):
        self.id = id
        self.pedidos = []


class Pedidos:
    def __init__(self, id, cliente):
        self.id = id
        self.produtos = []



