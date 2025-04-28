inicio =  int(input("Digite o valor inicial: "))
fim =  int(input("Digite o valor final: "))

if inicio > fim:
    print("Intervalo de valores inválido")
else:
    soma = 0
    n = inicio
    
    while n <= fim:
        if n % 2 != 0:
            soma += n
        n += 1

print(f"Soma dos ímpares neste intervalo: {soma}")
    