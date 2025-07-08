arq = open("exemplo.txt", "r", encoding="UTF-8")

letra = arq.read(1)
vogais = 0

while letra:
    if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
        vogais += 1
    letra = arq.read(1)
    
print(f"Vogais: {vogais}")
    
arq.close()