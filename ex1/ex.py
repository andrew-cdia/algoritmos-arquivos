arq = open("linhas.txt", 'r', encoding="UTF-8")

linhas = 0

for line in arq:
    linhas += 1

print(f"Linhas: {linhas}")

arq.close()