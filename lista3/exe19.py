"""
Crie uma função que encontre a moda e a mediana de um vetor de
elementos numéricos.
- Moda é o elemento mais recorrente no conjunto (mais se repete);
- Mediana é o valor que ocupa a posição central dos elementos quando
ordenados.
"""
def modaMediana(vetor):

    ordenado = ordenaVetor(vetor)

    # mediana
 
    n = len(ordenado)

    if n % 2 == 1:
        mediana = ordenado[n // 2]
    else:
        mediana = (ordenado[n // 2 - 1] + ordenado[n // 2]) / 2

    #moda 

    frequencias = {}
    for numero in ordenado:
        if numero in frequencias:
            frequencias[numero] += 1
        else:
            frequencias[numero] = 1

    print(frequencias)        

    return mediana

def ordenaVetor(arr):

    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]

    return arr



vetor = [0,6,9,1,5,8,7,8,7,9,8]

print(modaMediana(vetor))
