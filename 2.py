"""
Dado um inteiro positivo N, liste todos os divisores de N, do 1 até N, e conte quantos divisores foram encontrados. No fim, mostre a contagem total.
"""

n = int(input("Digite um número inteiro positivo: "))
i = 0
contador = 0

for i in range(1, n + 1):
    if n % i == 0:
        print(i)
        contador += 1
print(f"Total de divisores encontrados: {contador}")