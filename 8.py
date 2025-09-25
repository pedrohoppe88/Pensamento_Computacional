"""
O programa deve solicitar ao usuário um número inteiro positivo e verificar
se ele é um número perfeito. Um número é dito perfeito quando a soma de todos os 
seus divisores positivos, excluindo ele mesmo, é igual ao próprio número 
(por exemplo, 6 = 1 + 2 + 3). Mostre todos os divisores usados no cálculo e, ao final, diga se o número é ou não perfeito.
"""
numero = int(input("Digite um número inteiro positivo: "))
divisores = []
soma = 0
for i in range(1, numero, 1):
    if numero % i == 0:
        divisores.append(i)
        soma += i
print(f"Divisores de {numero}: {divisores}")
if soma == numero:
    print(f"{numero} é um número perfeito.")
else:
    print(f"{numero} não é um número perfeito.")