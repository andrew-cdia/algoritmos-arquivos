arq = open("palavras.txt", 'r', encoding="UTF-8")

palavra = input()

texto = arq.read()

quantidade = texto.count(palavra.strip())

print(f"Quantidade: {quantidade}")

arq.close()