"""
Utilize a compreensão de listas para criar uma função
elevar_quadrado(vetor) que retorna um novo vetor com cada elemento
elevado ao quadrado, utilizando compreensão de listas. 

"""

def elevar_quadrado(vetor):

    elevado = [int(num)**2 for num in vetor]

    return elevado

lista = [1,2,3,4,5,6,7,8,9,10]

print(elevar_quadrado(lista))