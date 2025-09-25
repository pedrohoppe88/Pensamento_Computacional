"""
Solicite ao usuário um número inteiro positivo e mostre a sequência de números decrescentes de N até 1.
"""

n = int(input("Digite um número inteiro positivo: "))

if n <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:

    for i in range(n, 0, -1):
        print(i)
    