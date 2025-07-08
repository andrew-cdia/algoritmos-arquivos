arq = open("substituir_vogais.txt", 'r', encoding="UTF-8")

conteudo = arq.read()

arq.close()

novo = ""

for caracter in conteudo:
    if caracter.lower() in ['a', 'e', 'i', 'o', 'u']:
        novo += '*'
    else:
        novo += caracter

arq = open("substituir_vogais2.txt", 'w', encoding="UTF-8")

arq.write(novo)

arq.close()