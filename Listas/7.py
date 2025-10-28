"""
7. Peça ao usuário para digitar uma sequência de 10 números. Em seguida, crie duas listas a partir desta sequência:
uma contendo os números pares e outra contendo os números ímpares.
"""

numeros = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
        
print("Números pares:", pares)
print("Números ímpares:", impares)

