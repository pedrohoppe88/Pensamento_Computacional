segredo = random.randint(1, 20)
tentativas = []

palpite = 0

while palpite != segredo:
    palpite = int(input("Digite um número entre 1 e 20: "))
    tentativas.append(palpite)

    if palpite < segredo:
        print("Muito baixo!")
    elif palpite > segredo:
        print("Muito alto!")

print("Parabéns! Você acertou!")
print("Tentativas feitas:", len(tentativas))
print("Números digitados:", tentativas)
