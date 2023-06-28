# implementar programa que determina o número de palavras contidas numa string e as que surgem mais que uma vez

# => input string
# => implementar função que determina o número de palavras contidas numa string


inputString = input("Insira uma string:")

# função que devolve o número de palavras contidas numa string que surge mais que uma vez
def countWords(inputString):
    # separar a string em palavras
    words = inputString.split()
    # criar um dicionário com as palavras e o número de vezes que aparecem
    wordsDict = {}
    for word in words:
        if word in wordsDict:
            wordsDict[word] += 1
        else:
            wordsDict[word] = 1
    # determinar o número de palavras que surgem mais que uma vez
    count = 0
    for word in wordsDict:
        if wordsDict[word] > 1:
            count += 1
    return count

print()
print("Número de palavras que surgem mais que uma vez:", countWords(inputString))