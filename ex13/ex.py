import datetime

arq = open("nascimentos.txt", 'r', encoding="UTF-8")

arq2 = open("idades.txt", 'w', encoding="UTF-8")

for line in arq:
    conteudo = line.split(",")

    idade = conteudo[1].split()

    hoje = datetime.date.today()

    age = int(idade[2]) - hoje.year

    if int(idade[1]) < hoje.month:
        age -= 1
    elif int(idade[0]) < hoje.day:
        age -= 1

    arq2.write(f"{conteudo[0]}, {age}") 

arq.close()
arq2.close()