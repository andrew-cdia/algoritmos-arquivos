arq = open("notas.txt", 'r', encoding="UTF-8")

alunos = dict()

for line in arq:
    line_split = line.split(", ")

    alunos[line_split[0].strip()] = line_split[1].split()

melhor_aluno = max(alunos.items(), key=lambda k: k[1])

print(f"Melhor aluno: {melhor_aluno[0]}, Nota: {melhor_aluno[1]}")

arq.close()