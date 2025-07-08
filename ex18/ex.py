arq = open("alunos.txt", 'a', encoding="UTF-8")

n = int(input("Número de alunos: "))

alunos = []

for i in range(n):
    matricula = int(input("Matricula: "))
    sobrenome = input("Sobrenome: ")
    ano = int(input("Ano de nascimento"))

    alunos.append([matricula, sobrenome, ano])

for aluno in alunos:
    print(aluno.join(", "), file=arq)

arq.close()