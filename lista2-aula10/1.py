itens = []

for i in range(5):
    item = input(f"Digite o {i+1}º item: ")
    itens.append(item)

print("Lista atual:", itens)

indice = int(input("Digite o índice do item que deseja remover: "))

if 0 <= indice < len(itens):
    removido = itens.pop(indice)
    print("Item removido:", removido)
    print("Lista atualizada:", itens)
else:
    print("Índice inválido!")
