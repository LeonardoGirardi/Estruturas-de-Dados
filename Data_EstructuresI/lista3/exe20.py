"""
Escreva uma função para ordenar uma lista de strings em ordem alfabética
crescente.
""" 

def ordenaStrings(strings):

    n = len(strings)

    for i in range(n):
        for j in range(0, n-i-1):
            if strings[j] > strings[j + 1]:
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
    
    return strings

#teste

nomes = ["Ana", "Claudio", "Marta", "Felipe", "Anacleto", "John"]

print(ordenaStrings(nomes))

