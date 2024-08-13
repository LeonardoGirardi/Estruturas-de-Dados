"""
Você irá desenvolver um sistema de biblioteca e precisa criar um diagrama das estruturas
para representar as principais entidades do sistema. Considere que o sistema deve
gerenciar Livros, Usuários e Empréstimos. Cada livro possui um título, autor e número
de exemplares disponíveis. Cada usuário é identificado por um número de registro e
possui um nome. Um usuário pode fazer múltiplos empréstimos, e cada empréstimo está
associado a um único livro e um único usuário. Modele as estruturas e as associações
necessárias.
"""

class Usuarios:

    def __init__(self, num_registro, nome):
        self.num_registro = num_registro
        self.nome = nome

class Livros:

    def __init__(self, titulo, autor, num_exemplares):
        self.titulo = titulo
        self.autor = autor
        self.num_exemplares = num_exemplares

class Emprestimo:
    def __init__(self, livro, usuario, data_emprestimo):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = data_emprestimo



