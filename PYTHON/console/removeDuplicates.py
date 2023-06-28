userText = input("Texto: ")

userTextList = userText.split(" ")

resultText = []

duplicates = []

for word in userTextList:
    if word not in resultText:
        resultText.append(word)
    if word not in duplicates:
        duplicates.append(word)

if len(duplicates) == 1 :
    print(f"Resultado: {' '.join(resultText)} \nFoi removida {len(duplicates)} palavra difrente")
else:
    print(f"Resultado: {' '.join(resultText)} \nForam removidas {len(duplicates)} palavras difrentes")






