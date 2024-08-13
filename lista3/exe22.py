"""
Implemente uma função que recebe uma lista de números e retorna duas
listas separadas, uma contendo os números positivos e outra contendo os
números negativos. 

"""

def partelista(lista):

    n = len(lista)

    positivos = []
    negativos = []
 

    for i in range(n):
        if lista[i] >= 0:
            positivos.append(lista[i])
        else:
            negativos.append(lista[i])

    return negativos, positivos
        

lista = [-1, 4, 2, -2, -3, 0, 9]

print(partelista(lista))