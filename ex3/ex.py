arq = open("vogais_consoantes.txt", 'r')

vogais = 0
consoantes = 0
letra = arq.read(1)

while letra:
    if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
        vogais += 1
    elif letra.isalpha():
        consoantes += 1
    letra = arq.read(1) 

print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")

arq.close()