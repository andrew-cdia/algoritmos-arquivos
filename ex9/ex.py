arq = open("cidades.txt", 'r', encoding="UTF-8")

cidades = dict()

for line in arq:
    cidades[line[:40]] = line[40:]

arq.close()

cidades = sorted(cidades.items(), key=lambda k: k[1])

arq = open("ordenado.txt", 'w', encoding="UTF-8")

for cidade in cidades:
    print(f"{cidade[0]}{cidade[1]}", file=arq)

arq.close()