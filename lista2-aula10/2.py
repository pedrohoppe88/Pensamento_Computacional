nomes = []

for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

print("Lista antes da remoção:", nomes)

remover = input("Qual nome deseja remover? ")

if remover in nomes:
    nomes.remove(remover)
    print("Lista atualizada:", nomes)
else:
    print("Erro: nome não encontrado!")
