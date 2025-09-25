"""
O programa deve ler uma idade digitada pelo usuário e só aceitar valores entre 0 e 120. 
Enquanto a entrada for inválida, peça novamente e conte quantas tentativas foram necessárias até receber um valor válido. 
Ao final, exiba a idade confirmada e o total de tentativas.
"""
i = 0
contador = 0;

while True:
    idade = int(input("Digiteb a sua idade de 0 a 120: "))
    if idade >= 0 and idade <= 120:
        contador += 1
        print(f"Idade confirmada: {idade}")
        print(f"Total de tentativas: {contador}")
        break