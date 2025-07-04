arq = open("substituir_vogais.py", 'r')

conteudo = arq.read()

arq.close()

novo = ""

for caracter in conteudo:
    if caracter.lower() in ['a', 'e', 'i', 'o', 'u']:
        novo += '*'
    else:
        novo += caracter

arq = open("substituir_vogais.py", 'w')

arq.write(novo)

arq.close()