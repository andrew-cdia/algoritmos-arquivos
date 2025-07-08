arq1 = open("arquivo1.txt", 'r', encoding="UTF-8")
arq2 = open("arquivo2.txt", 'r', encoding="UTF-8")

arq3 = open("arquivo3.txt", 'w', encoding="UTF-8")

arq3.write(str(arq1.read()))
arq3.write(str(arq2.read()))

arq1.close()
arq2.close()
arq3.close()