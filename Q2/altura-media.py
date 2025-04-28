alunos = 0
idades = 0
alturas = 0
aluno_altura = 0
aluno_idade = 0

while True:
    idade = int(input("Idade: "))
    if idade == 0:
        break
    altura = float(input("Altura: "))
    alunos += 1
    
    if altura < 1.70:
        idades += idade
        aluno_idade += 1
        
    elif idade > 20:
        alturas += altura
        aluno_altura += 1
        
if aluno_altura > 0:
    media_altura = alturas / aluno_altura
else: 
    media_altura = 0
    
if aluno_idade > 0:
    media_idade = idades / aluno_idade
else:
    media_idade = 0

print(f"A classe tem {alunos} alunos")
print(f"A idade média dos alunos com menos de 1,70m de altura é {media_idade}")
print(f"A altura média dos alunos com mais de 20 anos é {media_altura}")