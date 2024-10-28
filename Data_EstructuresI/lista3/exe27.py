"""
Utilize a compreensão de listas para multiplicar todos os elementos de um
vetor por um número N. 

"""

lista = [1,2,3,4,5,6,7,8,9,10]
n = 2

listaMult = [int(num)*n for num in lista]

print(listaMult)
