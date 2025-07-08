arq = open("produtos.txt", 'r+', encoding="UTF-8")

soma = 0

for line in arq:
    preco = float(line.split(", ")[1])

    soma += preco

print(f"Total: R${soma:.02}", file=arq)

arq.close()