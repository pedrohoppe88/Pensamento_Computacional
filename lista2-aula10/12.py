palavra = input("Digite uma palavra: ").lower()

letras = list(palavra)

if letras == letras[::-1]:
    print("É um palíndromo!")
else:
    print("Não é palíndromo.")
