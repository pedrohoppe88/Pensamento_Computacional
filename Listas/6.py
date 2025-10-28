"""
6. Peça ao usuário para digitar duas sequências de 5 números e armazene-as 
em duas listas distintas. Em seguida, faça um programa que procure os elementos comuns entre elas e os junte em uma terceira lista.
"""
lista1 = []
lista2 = []

for i in range(5):
    num1 = int(input(f"Digite o {i+1}º número da primeira lista: "))
    lista1.append(num1)
for i in range(5):
    num2 = int(input(f"Digite o {i+1}º número da segunda lista: "))
    lista2.append(num2)
    
lista_comum = []

for elemento in lista1:
    if elemento in lista2 and elemento not in lista_comum:
        lista_comum.append(elemento) 
print("Os elementos comuns entre as duas listas são:", lista_comum)
