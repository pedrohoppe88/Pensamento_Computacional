while True:
    Nfatorial = int(input("Digite o número fatorial (negativo para sair): "))
    
    if Nfatorial < 0:
        break
    rastro = []
    fatorial = 1  # inicializa
    for i in range(Nfatorial, 0, -1):
        fatorial *= i
        rastro.append(str(i))
    
    print(f"O fatorial de {Nfatorial} é: {fatorial}")
    print(f"O rastro: {rastro}")