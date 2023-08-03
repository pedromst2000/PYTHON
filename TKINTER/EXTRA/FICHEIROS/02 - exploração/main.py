
file = open("countries.txt", "r", encoding="utf-8")

# avançar progressivamente para próxima linha do ficheiro com ciclo while quando na opção se pretende avançar para a próxima linha S


print(file.readline())
countLines = 1

while True:
    

    op = input("Deseja avançar para a próxima linha? (S/N) ")
    if op == "S" or op == "s":
        countLines += 1
        print(file.readline())
        print("Linha: ", countLines)
        if countLines == 5:
            # recompor o ficheiro para a primeira linha
            file.seek(0)
            countLines = 0
            
    else:
        break


