"""
Crie uma função que conta quantas vezes um determinado elemento aparece em uma lista
"""

def conta(arr, n):
    i = 0
    soma = 0

    for i in arr:
        if i == n:
            soma += 1
    return soma


arr = [1,2,2,4,5,6,7,8,8,0]

n = 2

print(conta(arr, n))




