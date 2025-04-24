alunos = 0
idades = 0
alturas = 0
media_altura = 0
media_idade = 0

idade = int(input("Idade: "))
altura = float(input("Altura: "))

while idade != 0:
    idade = int(input("Idade: "))
    altura = float(input("Altura: "))
    alunos += 1
    if altura < 1.70:
        idades += idade
    elif idade > 20:
        alturas += altura
        
media_altura = alturas / alunos
media_idade = idades / alunos

print(f"A classe tem {alunos} alunos")
print(f"A idade média dos alunos com menos de 1,70m de altura é {media_idade}")
print(f"A altura média dos alunos com mais de 20 anos é {media_altura}")