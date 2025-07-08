media = 6

alunos = []

arq = open("notas_turma.txt", 'r', encoding="UTF-8")

for line in arq:
    alunos.append(line.split(", "))

while True:
    print("1 - Definir informações")
    print("2 - Inserir alunos")
    print("3 - Exibir alunos e medias")
    print("4 - Exibir aprovados")
    print("5 - Exibir reprovados")
    print("6 - Salvar dados em disco")
    print("0 - Sair")

    tipo = int(input())

    if not tipo in range(0, 7):
        continue
    
    if tipo == 0:
        break
    
    if tipo == 1:
        media = float(input("Média: "))
    
    elif tipo == 2:
        nome = input("Nome: ")
        nota = float(input("Nota: "))

        alunos.append([nome, nota])
    
    elif tipo == 3:
        for aluno in alunos:
            print(aluno.join(", "))
        
    elif tipo == 4:
        for aluno in alunos:
            if aluno[1] >= media:
                print(aluno.join(", "))

    elif tipo == 5:
        for aluno in alunos:
            if aluno[1] < media:
                print(aluno.join(", "))

    elif tipo == 6:
        with open("notas_turma.txt", 'w', encoding="UTF-8") as arq:
            for aluno in alunos:
                print(alunos.join(", "), file=arq)
    
