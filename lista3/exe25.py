"""
5 Escreva uma função para ordenar uma lista de números em ordem
decrescente. (utilize for ) 

"""

def ordenaLista(lista):

    n = len(lista)

    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

lista = [1,2,3,4,5,6,7,8,9]

print(ordenaLista(lista))