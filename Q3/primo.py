n = int(input("Digite um número: "))

if n < 2:
    print(f"O número {n} não é primo")
else:
    primo = True
    divisor = 2
    while divisor < n:
        if n % divisor == 0:
            primo = False
            break
        divisor += 1

    if primo:
        print(f"O número {n} é primo")
    else:
        print(f"O número {n} não é primo")
