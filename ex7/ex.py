arq = open("minusculas.txt", 'r')

conteudo = arq.read()

arq.close()

conteudo = conteudo.upper()

arq = open("minusculas.txt", 'w')

arq.write(conteudo)

arq.close()