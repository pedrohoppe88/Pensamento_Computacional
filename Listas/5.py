"""

5. Peça ao usuário para digitar duas sequências de 5 números e armazene em duas 
listas distintas. Após, faça um programa que junte essas duas listas em uma só.
"""

lista1 = []
lista2 = []

for i in range(5):
    num1 = int(input(f"Digite o {i+1}º número da primeira lista: "))
    lista1.append(num1)

for i in range(5):
    num2 = int(input(f"Digite o {i+1}º número da segunda lista: "))
    lista2.append(num2)
lista_combinada = []
lista_combinada = lista1 + lista2

print("A lista combinada é:", lista_combinada)
