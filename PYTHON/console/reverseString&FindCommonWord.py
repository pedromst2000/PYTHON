def result(sentence):
    splitTextList = sentence.split()
    splitTextList.reverse()

    counter = 0
    num = splitTextList[0]
     
    for i in splitTextList:
        currFrequency = splitTextList.count(i)
        if(currFrequency > counter):
            counter = currFrequency
            num = i
    
    print("Resultado:" + " " + " ".join(splitTextList))
    print(f"Palavra que surge mais vezes: {num} com um total de {counter} vezes." )
    


userSentence = input("Write the sentence: ")

result(userSentence)

