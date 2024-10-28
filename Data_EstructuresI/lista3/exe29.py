"""
Utilize a compreensão de listas para criar uma função que recebe um vetor
qualquer de números inteiros, filtrar_pares(vetor), e que retorna um
novo vetor contendo apenas os elementos pares do vetor original. 

"""

def filtrar_pares(vetor):

    pares = filter(lambda x: x % 2 == 0, vetor)

    return list(pares)

lista = [1,2,3,4,5,6,7,8]

print(filtrar_pares(lista))