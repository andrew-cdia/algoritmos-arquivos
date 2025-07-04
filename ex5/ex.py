arq = open("alfabeto.txt", 'r')

counter = dict()
caracter = arq.read(1)

while caracter:
    if caracter.isalpha() and caracter in counter:
        counter[caracter] += 1
    else:
        counter[caracter] = 1

    caracter = arq.read(1)  

print(f"Quantidades: {counter}")

arq.close()