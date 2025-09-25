"""
Solicite um número inteiro N e exiba os N primeiros múltiplos de 9, mostrando também a soma desses múltiplos ao final.
"""
numero = int(input("Digite um número inteiro positivo: "))
soma = 0
for i in range(1, numero + 1):
    multiplo = i * 9
    print(multiplo)
    soma = soma + multiplo
print(f"A soma dos {numero} primeiros múltiplos de 9 é: {soma}")