arq = open("alfabeto.txt", 'r', encoding="UTF-8")

counter = dict()
caracter = arq.read(1)

while caracter:
    if caracter.isalpha() and caracter in counter:
        counter[caracter.lower()] += 1
    elif caracter.isalpha():
        counter[caracter.lower()] = 1

    caracter = arq.read(1)  

print(f"Quantidades: {counter}")

arq.close()