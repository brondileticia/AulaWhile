n = int(input("Digite um limite: "))
soma = 0
i = 1

while i <= n:
    print(f'Somando {i} a {soma}.')
    soma += i
    i += 1
print(f"A soma de 1 a {n} é {soma}.")
