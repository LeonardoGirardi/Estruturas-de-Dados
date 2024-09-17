"""
Implemente um programa que recebe dois vetores numéricos ordenados e
intercala seus elementos em um novo vetor de forma ordenada. 

"""
def ordenaVetor(vetor):

    n = len(vetor)

    for i in range(n):
        for j in range(0, n-i-1):
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]

    return vetor


def intercalaVetor(vetor1, vetor2):

    ordenaVetor(vetor1)
    ordenaVetor(vetor2)

    tam_v1 = len(vetor1)
    tam_v2 = len(vetor2)

    novoVetor = []

    for i in range(min(tam_v1, tam_v2)):
        novoVetor.append(vetor1[i])
        novoVetor.append(vetor2[i])

    if tam_v1 > tam_v2:
        novoVetor.extend(vetor1[tam_v2:])
        
    if tam_v1 < tam_v2:
        novoVetor.extend(vetor2[tam_v1:])
        
    return novoVetor

arr1 = [1,9,7,3,5,11]
arr2 = [0,2,4,6,8,10,12,13,14]


print(intercalaVetor(arr2, arr1))


