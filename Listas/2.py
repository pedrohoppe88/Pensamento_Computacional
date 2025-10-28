"""
2. Crie uma lista chamada temperaturas com os valores [30, 22, 25, 28, 31, 27, 29]. Aumente todas as temperaturas menores que 25 em 5 graus.
"""

lista_temperaturas = [30, 22, 25, 28, 31, 27, 29]
for i in range(len(lista_temperaturas)):
    if lista_temperaturas[i] < 25:
        lista_temperaturas[i] += 5 
    
print(lista_temperaturas)

