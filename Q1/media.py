menor = 501
maior = 0
soma = 0
contador = 0

while contador < 5:
    numero = int(input("Digite um número: "))
    soma += numero
    contador += 1
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero

media = soma / 5

print("Menor número:", menor)
print("Maior número:", maior)
print("Média:", media)
