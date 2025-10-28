numeros = []

qtd = int(input("Quantos números você vai digitar? "))

for i in range(qtd):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
    
    maior = numeros[0]
    menor = numeros[0]
    
    for n in numeros:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
