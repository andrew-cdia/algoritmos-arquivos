arq = open("cadastro.py", 'a', encoding="UTF-8")

nome, telefone = None, 1

while telefone != 0:
    nome = input("Nome: ")
    telefone = input("Telefone: ")

    print(f"{nome.strip()}, {telefone.strip()}", file=arq)

arq.close()