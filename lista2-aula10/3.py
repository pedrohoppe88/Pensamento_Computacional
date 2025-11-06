numeros = []

for i in range(5):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

print("Lista original:", numeros)

novo = int(input("Digite um novo número para inserir: "))
indice = int(input("Digite o índice onde deseja inserir: "))

if 0 <= indice <= len(numeros):
    numeros.insert(indice, novo)
    print("Lista atualizada:", numeros)
else:
    print("Erro: índice inválido!")
