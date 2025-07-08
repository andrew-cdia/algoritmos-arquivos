import random

arq = open("mercadorias.txt", 'r', encoding="UTF-8")

itens = []

for line in arq:
    itens.append(line.split(", "))

arq.close()

mercadoria, quantidade = 1, 0

while mercadoria:
    tipo = input("Entrada/Saída: ")

    mercadoria = input("Mercadoria: ")
    quantidade = int(input("Quantidade: "))

    if tipo.lower() == "entrada":
        cond = True
        while cond:
            
            codigo = random.randint(1, 999)
            for item in itens:
                if codigo == item[0]:
                    break
            else:
                cond = False

            itens.append([codigo, mercadoria, quantidade])

    elif tipo.lower() == "saida":
        
        for item in itens:
            if item[1] == mercadoria and int(item[2]) == quantidade:
                itens.pop(item)

    else:
        break
    
arq = open("mercadorias.txt", 'w', encoding="UTF-8")

for item in itens:
    print(itens.join(", "), file=arq)

arq.close()