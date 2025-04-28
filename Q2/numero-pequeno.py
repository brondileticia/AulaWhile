numero = float(input("Digite um número pequeno, menor do que 1: "))

soma = 0
termo = 1
contador = 0

while True:
    parcela = 1 / (termo ** 2)
    if parcela < numero:
        break
    soma += parcela
    contador += 1
    termo += 1

print(f"Foram somados {contador} termos")
print(f"Soma = {soma:.5f}")
