caracter = input()

if len(caracter) > 1: exit()

arq = open("caracteres.txt", 'r')
letra = arq.read(1)

ocorrencias = 0
while letra:
    if letra == caracter:
        ocorrencias += 1
    letra = arq.read(1)

print(f"Ocorrências de {caracter}: {ocorrencias}")

arq.close()