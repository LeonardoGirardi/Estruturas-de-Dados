"""
Implemente uma função que recebe duas listas ordenadas e retorna uma
terceira lista contendo todos os elementos das duas listas originais já em
ordem. 
"""

def ordenaListas(lista1, lista2):

    lista = lista1 + lista2

    n = len(lista)

    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


lista1 = [1,3,5,7,8,9,9,0,8,4,3,5,6]
lista2 = [0,9,1,5,6,8,9,0,1,2]

print(ordenaListas(lista1, lista2))

