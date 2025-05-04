aurora = 0
natrix = 0
percy = 0
nulos = 0
total = 0

while True:
    voto = int(input("Candidato escolhido: "))

    if voto < 0:
        break

    elif voto == 1:
        aurora += 1
    elif voto == 2:
        natrix += 1
    elif voto == 3:
        percy += 1
    else:
        nulos += 1

    total += 1

if total == 0:
    print("Eleições não realizadas.")
else:
    perc_aurora = (aurora / total) * 100
    perc_natrix = (natrix / total) * 100
    perc_percy = (percy / total) * 100
    perc_nulos = (nulos / total) * 100

    print(f"Aurora - {perc_aurora:.1f}% dos votos - {aurora} voto(s)")
    print(f"Natrix - {perc_natrix:.1f}% dos votos - {natrix} voto(s)")
    print(f"Percy - {perc_percy:.1f}% dos votos - {percy} voto(s)")
    print(f"Votos nulos - {perc_nulos:.1f}% - {nulos} voto(s)")
    print(f"Votos computados: {total}")
