"""
Escreva uma função que recebe duas listas e retorna uma terceira lista
contendo a união dos elementos únicos das duas listas. 
"""

def elementosUnicos(lista1, lista2):

    lista = lista1 + lista2

    n = len(lista)

    elementos_unicos = []
    conjunto = set()

    for elemento in lista:
        if elemento not in conjunto:
            elementos_unicos.append(elemento)
            conjunto.add(elemento)

    return elementos_unicos


lista1 = [1,2,3,3,4,5,6]
lista2 = [0,9,9,7,6]

print(elementosUnicos(lista1, lista2))

