arq = open("cidades.txt", 'r')

cidades = dict()

for line in arq:
    cidades[line[:40]] = line[40:]

arq.close()

cidades = sorted(cidades, key=lambda k: k[1])

arq = open("ordenado.txt", 'w')

for cidade in cidades[::-1]:
    print(f"{cidade[0]}{cidades[1]}", file=arq)

arq.close()