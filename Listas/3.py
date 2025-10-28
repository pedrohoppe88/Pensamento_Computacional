"""
3. Peça ao usuário para digitar as idades de várias pessoas, até o usuário digitar o valor 0.
Após, calcule a média das idades e apresente na tela.
"""

def calcular_media_idades(idadedes):
    if len(idadedes) == 0:
        return 0
    return sum(idadedes) / len(idadedes) # o sumn retorna a soma de todos os elementos da lista

def main():
    idades = []
    while True:
        idade = int(input("Digite a idade (ou 0 para sair): "))
        if idade == 0:
            break
        idades.append(idade)
    media = calcular_media_idades(idades)
    print(f"A média das idades é: {media:.2f}")     
