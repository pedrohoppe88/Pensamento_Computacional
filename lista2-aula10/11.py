fila = []

while True:
    print("\n1 - Adicionar pessoa")
    print("2 - Atender pessoa")
    print("3 - Sair")
    opc = input("Escolha: ")

    if opc == "1":
        nome = input("Nome da pessoa: ")
        fila.append(nome)
    elif opc == "2":
        if fila:
            atendido = fila.pop(0)
            print("Atendendo:", atendido)
        else:
            print("Fila vazia!")
    elif opc == "3":
        break
