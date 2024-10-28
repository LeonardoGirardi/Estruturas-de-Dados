"""
Implemente uma função que crie uma lista B com os elementos de uma lista
A em ordem invertida. (Adicione elemento por elemento).
"""

def inverteOrdem(vetor):
    tam = len(vetor)

    i = tam - 1
    novo_vetor = []

    while i >= 0:
        novo_vetor.append(vetor[i])
        i -= 1
    return novo_vetor

vetor = [1,2,3,4,5,6,7,8,9]

print(inverteOrdem(vetor))
