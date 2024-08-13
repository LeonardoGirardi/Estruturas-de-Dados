"""
Crie uma função filtrar_elementos_unicos(vetor) que retorna um
novo vetor contendo apenas os elementos únicos do vetor original, utilizando
compreensão de listas.

"""
from functools import reduce 

def filtrar_elementos_unicos(vetor):

    elementosUnicos = []
    
    [elementosUnicos.append(num) for num in vetor if num not in elementosUnicos]

    return elementosUnicos
    

lista = [1,2,2,3,4,5,6,6,7,8,9,0,0]

print(filtrar_elementos_unicos(lista))