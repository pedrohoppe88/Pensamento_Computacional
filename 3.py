""""
 Leia dois inteiros A e B (com A ≤ B) e exiba, 
 no intervalo fechado de A até B, apenas os números que são múltiplos de 3 e não são múltiplos de 5. Informe também quantos números foram exibidos.
"""
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
contador = 0
for i in range(a, b + 1):
    if i % 3 == 0 and i % 5 != 0:
        print(i)
        contador += 1
print(f"Total de números exibidos: {contador}")
