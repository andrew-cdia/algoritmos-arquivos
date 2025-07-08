arq = open("minusculas.txt", 'r', encoding="UTF-8")

conteudo = arq.read()

arq.close()

conteudo = conteudo.upper()

arq = open("maiusculas.txt", 'w', encoding="UTF-8")

arq.write(conteudo)

arq.close()