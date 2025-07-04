arq1 = open("arquivo1.txt", 'r')
arq2 = open("arquivo2.txt", 'r')

arq3 = open("arquivo3.txt", 'w')

arq3.write(arq1.read())
arq3.write(arq2.read())

arq1.close()
arq2.close()
arq3.close()