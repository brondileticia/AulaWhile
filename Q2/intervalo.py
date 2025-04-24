n1 =  int(input("Digite o valor inicial: "))
n2 =  int(input("Digite o valor final: "))
soma = 0

# if (n1 < 0) or (n2 < 0) or (n1 < n2):
#     print("Intervalo de valores inválido")
# else:
for n in range(n1, n2+1):
    if ((n % 2) != 0):
        soma += n

print(f"Soma dos ímpares neste intervalo: {soma}")
    