arq = open("analise.txt", 'r')

linhas, palavras, caracter = 0, 0, 0

for line in arq:
    
    for carac in line:
        if carac in [" ", ".", ","]:
            palavras += 1
        caracter +=1
    
    linhas += 1

print(f"Linhas: {linhas}, Palavras: {palavras}, Caracteres: {caracter}")

arq.close()