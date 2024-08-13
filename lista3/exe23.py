"""
Crie uma função que recebe uma lista e dois índices, e troca os elementos
nas posições correspondentes. 
"""

def trocaElementos(lista, i, j):
 
    c = lista[i]
    lista[i] = lista[j]
    lista[j] = c
    
    return lista


lista = [1,2,3,4,5,6,7,8,]

print(lista)

print(trocaElementos(lista, 0, 7))

