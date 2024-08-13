"""
Implemente uma função receba um vetor numérico e um número N e retorne
a soma dos elementos divisíveis por N.
"""

def retorna_Soma(arr, n):

    i = 0
  "  soma = 0

    for i in arr:
        if i % n == 0:
            soma += i
    return soma

arr = [1,2,3,4,5,6,7,8,9,]

n = 2

print(retorna_Soma(arr, n))
