
def maior_numero(lista):
    return max(lista)

def media(lista):
    return sum(lista) / len(lista)

def numeros_pares(lista):
    return [num for num in lista if num % 2 == 0]

def contar_elementos(lista, elemento):
    return lista.count(elemento)

def expoente(base, exp):
    return base ** exp


def main():
    while True:
        print("\n--- MENU ---")
        print("1 - Maior número da lista")
        print("2 - Média da lista")
        print("3 - Lista de números pares")
        print("4 - Contar elementos")
        print("5 - Calcular potência (expoente)")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            lista = list(map(float, input("Digite os números separados por espaço: ").split()))
            print("Maior número:", maior_numero(lista))

        elif opcao == "2":
            lista = list(map(float, input("Digite os números separados por espaço: ").split()))
            print("Média:", media(lista))

        elif opcao == "3":
            lista = list(map(int, input("Digite números inteiros separados por espaço: ").split()))
            print("Números pares:", numeros_pares(lista))

        elif opcao == "4":
            lista = input("Digite os elementos separados por espaço: ").split()
            elemento = input("Elemento a contar: ")
            print("Quantidade:", contar_elementos(lista, elemento))

        elif opcao == "5":
            base = float(input("Digite a base: "))
            exp = float(input("Digite o expoente: "))
            print("Resultado:", expoente(base, exp))

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()
