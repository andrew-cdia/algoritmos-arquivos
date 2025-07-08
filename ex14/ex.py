arq = open("classificacao.txt", 'r', encoding="UTF-8")

pessoas = dict()

for line in arq:
    line_split = line.split(", ")

    pessoas[line_split[0].strip()] = line_split[1].strip()

arq.close()

arq = open("classificacao2.txt", 'w', encoding="UTF-8")

for pessoa, idade in pessoas.items():
    if int(idade) == 18:
        print(f"{pessoa}, entrando na maioridade",file=arq)
    elif int(idade) > 18:
        print(f"{pessoa}, maior de idade",file=arq)
    else:
        print(f"{pessoa}, menor de idade",file=arq)        

arq.close()