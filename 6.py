soma = 0
contador = 0

while True:
    n = int(input("Digite um número inteiro (negativo para sair): "))
    if n < 0:
        break
    soma += n
    contador += 1

if contador > 0:
    media = soma / contador
    print(f"A média dos números positivos é: {media}")
else:
    print("Nenhum número positivo foi digitado.")