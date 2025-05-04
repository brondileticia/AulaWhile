x = float(input("Digite x: "))

soma = 1.0
termo = 1.0
numerador = 1.0
denominador = 1.0
n = 1

while termo >= 0.0001 or termo <= -0.0001:
    numerador *= x         # x^n
    denominador *= n       # n!
    termo = numerador / denominador
    soma += termo
    n += 1

print(f"e elevado a {x:.1f} = {soma:.4f}")
