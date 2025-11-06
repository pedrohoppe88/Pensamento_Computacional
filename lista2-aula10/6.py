nums = []

for i in range(5):
    n = float(input(f"Digite o {i+1}º número: "))
    nums.append(n)

soma = sum(nums)
media = soma / len(nums)

print("Soma:", soma)
print("Média:", media)
