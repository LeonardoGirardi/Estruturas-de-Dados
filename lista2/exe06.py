"""
Crie uma função soma_vetores(vetor1, vetor2) que recebe dois vetores
como argumentos e retorna um novo vetor que é a soma dos dois.
(use vetor criado em código estático)
"""
def soma_vetores(vetor1, vetor2):

    soma_vetores = []

    for i in range(len(vetor1)):
        soma_vetores.append(vetor1[i] + vetor2[i])

    return soma_vetores

vetor1 = [1,2,4,5,6,7,8]
vetor2 = [1,2,4,5,6,7,8]

soma = soma_vetores(vetor1, vetor2)

print(soma)

"""
Crie uma função buscar_elemento(vetor, elemento) que retorna o índice da
primeira ocorrência do elemento no vetor. Se o elemento não estiver
presente, retorne -1.
(use for para iterar sobre o vetor. Use vetor criado em código estático)
"""
def buscar_elemento(vetor, elemento):
    for i in range(len(vetor)):
        if vetor[i] == elemento:
            return i
    return -1

elemento = 12

indice = buscar_elemento(soma, elemento)

print(indice)
"""
Implemente uma função remover_duplicatas(vetor) que remove todas as
duplicatas do vetor, mantendo a ordem original dos elementos.
(use vetor criado em código estático)
"""
def remover_duplicatas(vetor):
    elementos_unicos = []
    conjunto = set()

    for elemento in vetor:
        if elemento not in conjunto:
            elementos_unicos.append(elemento)
            conjunto.add(elemento)

    return elementos_unicos

vetor = [3, 6, 8, 2, 5, 7, 9, 1, 4, 2, 5, 8]

elementos_unicos = remover_duplicatas(vetor)

print(vetor)
print(elementos_unicos)
"""
Implemente uma função vetor_para_conjunto(vetor) que remove todas as
duplicatas do vetor, convertendo-o para um tipo de conjunto ( set).
(use vetor criado em código estático)
"""









