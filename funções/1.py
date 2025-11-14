# Função que retorna o maior número de uma lista
def maior_numero(lista):
    return max(lista)  # max retorna o maior elemento de um iterável

# Função que calcula a média de uma lista de números
def media(lista):
    return sum(lista) / len(lista)  # sum soma todos os elementos da lista / len retorna a quantidade de elementos

# Função que retorna uma lista apenas com os números pares
def numeros_pares(lista):
    pares = []  # lista vazia para armazenar os números pares
    i = 0
    while i < len(lista):  # percorre todos os elementos da lista usando índice
        if lista[i] % 2 == 0:  # verifica se o número é par
            pares.append(lista[i])  # adiciona o número par à lista 'pares'
        i += 1  # avança para o próximo elemento
    return pares

# Função que conta quantas vezes um elemento aparece na lista
def contar_elementos(lista, elemento):
    contador = 0  # inicializa o contador
    i = 0
    while i < len(lista):  # percorre todos os elementos da lista
        if lista[i] == elemento:  # verifica se o elemento atual é igual ao elemento procurado
            contador += 1  # incrementa o contador
        i += 1  # avança para o próximo elemento
    return contador  # retorna a quantidade encontrada

# Função que calcula a potência de um número
def expoente(base, exp):
    return base ** exp  # operador ** realiza a exponenciação

# Função para ler uma lista de números float do usuário
def ler_lista():
    lista = []  # lista vazia para armazenar os números
    print("Digite os números (pressione ENTER sem digitar para parar):")
    while True:  # loop infinito até o usuário pressionar ENTER vazio
        valor = input("Número: ")
        if valor == "":  # condição para sair do loop
            break
        lista.append(float(valor))  # converte para float e adiciona à lista
    return lista  # retorna a lista preenchida

# Função para ler uma lista de números inteiros do usuário
def ler_lista_inteiros():
    lista = []
    print("Digite números inteiros (pressione ENTER sem digitar para parar):")
    while True:
        valor = input("Número: ")
        if valor == "":
            break
        lista.append(int(valor))  # converte para inteiro antes de adicionar
    return lista

# Função principal que exibe o menu e executa as opções
def main():
    while True:  # loop infinito até o usuário escolher sair
        # Exibe o menu de opções
        print("\n MENU ")
        print("1 - Maior número da lista")
        print("2 - Média da lista")
        print("3 - Lista de números pares")
        print("4 - Contar elementos")
        print("5 - Calcular potência")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")  # lê a opção do usuário

        if opcao == "1":  # maior número
            lista = ler_lista()  # chama a função para ler a lista
            print("Maior número:", maior_numero(lista))

        elif opcao == "2":  # média
            lista = ler_lista()
            print("Média:", media(lista))

        elif opcao == "3":  # números pares
            lista = ler_lista_inteiros()
            print("Números pares:", numeros_pares(lista))

        elif opcao == "4":  # contar elementos
            elementos = []
            print("Digite os elementos (pressione ENTER sem digitar para parar):")
            while True:
                e = input("Elemento: ")
                if e == "":
                    break
                elementos.append(e)
            alvo = input("Elemento a contar: ")
            print("Quantidade:", contar_elementos(elementos, alvo))

        elif opcao == "5":  # potência
            base = float(input("Base: "))
            exp = float(input("Expoente: "))
            print("Resultado:", expoente(base, exp))

        elif opcao == "0":  # sair
            print("Encerrando...")
            break

        else:  # caso digite uma opção inválida
            print("Opção inválida. Tente novamente.")


main()  # chama a função principal para iniciar o programa
