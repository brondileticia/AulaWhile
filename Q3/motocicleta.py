preco = float(input("Valor do bem: "))
inicial = float(input("Poupança inicial: "))
rendimento = float(input("Juros mensais: "))
deposito = float(input("Poupança mensal: "))

saldo = inicial
meses = 0

while saldo < preco:
    saldo += saldo * (rendimento / 100)  # rendimento mensal
    saldo += deposito                    # novo deposito
    meses += 1

print(f"Foram necessários {meses} meses")
