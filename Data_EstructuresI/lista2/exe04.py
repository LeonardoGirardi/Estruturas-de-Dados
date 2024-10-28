"""
Implemente as estruturas de Aluno, Professor, Disciplina e Turma elaboradas
na atividade 05 (IP-01).

Desenvolva um diagrama das estruturas para um sistema de gerenciamento de escola.
Considere as entidades principais: Alunos, Professores, Disciplinas e Turmas. Modele
as classes, atributos e as associações necessárias.
"""
class Aluno:
    def __init__(self, alunoID, nome, disciplinaID):
        self.alunoID = alunoID
        self.nome = nome
        self.disciplinaID = []


class Professor:
    def __init__(self, professorID, disciplinaID, nome):
        self.professorID = professorID
        self.disciplinaID = disciplinaID
        self.nome = nome


class Disciplina:
    def __init__(self, disciplinaID, nome):
        self.disciplinaID = disciplinaID
        self.nome = nome


class Turma:
    def __init__(self, disciplinaID, alunoID):
        self.disciplinaID = disciplinaID
        self.alunoID = []

