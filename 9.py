N = int(input("Digite um número inteiro positivo: "))

a, b = 0, 1
for i in range(N):
    print(a)
    a, b = b, a + b  

print(f"O último número exibido foi: {a - b}")