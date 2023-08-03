import random

# # 1. Elabore um programa que leia uma frase e escreva os seus caracteres por ordem inversa.
texto = input("Indique um texto: ")

for i in range(len(texto)-1, -1, -1):
    print(texto[i], end="")

# # --------------------------------------------------------------------------------------------
# # 2. Elabore um programa que leia uma frase e determine:
# # a) O número de caracteres da frase;
# # b) O número espaços;
# # c) O número de vogais;

texto = input("Indique um texto: ")

print("Nº de caracteres: ", len(texto))

vowels = ["a", "e", "i", "o", "u"]

count = 0

for i in range(len(texto)):
    if texto[i].lower() in vowels:
        count += 1

print("Nº de vogais: ", count)
print("Nº de espaços: ", texto.count(" "))

# # --------------------------------------------------------------------------------------------
# # 3. Elabore um programa que leia uma frase e determine se é um palíndromo.


def isPalindrome(text):
    for i in range(len(text)):
        # se cada caracter for diferente lido ao contrário na string, não é palíndromo
        if text[i] != text[len(text)-1-i]:
            return False
    # se cada caracter for igual lido ao contrário na string, é palíndromo
    # => elif text[i] == text[len(text)-1-i]:
    return True


texto = input("Indique um texto: ")

if isPalindrome(texto):
    print("O texto é capicua")
else:
    print("O texto não é capicua")

# # --------------------------------------------------------------------------------------------
# # 4. Escreva a função removeSpaces que receba um texto e substitua as
# # sequências de dois ou mais espaços por um único espaço. A função
# # deve imprimir o texto resultante.


def removeSpaces(text):
    # substitui os espaços por um único espaço
    text = text.replace("  ", " ")

    # se o texto tiver mais de 2 espaços, chama a função novamente
    if "  " in text:
        removeSpaces(text)
    else:
        print("Texto: {}".format(text))


text = input("Texto: ")

removeSpaces(text)

# # --------------------------------------------------------------------------------------------
# # 5. Escreva a função shortName que deve receber um nome completo e
# # devolve uma string com o primeiro e último nome(primeiro nome
# #                                                 próprio e último apelido)


def shortName(name):
    # separa o nome por espaços
    name = name.split(" ")

    # retorna o primeiro nome e o último nome
    return "{} {}".format(name[0], name[len(name)-1])


name = input("Nome: ")

shortName_ = shortName(name)

print("{}".format(shortName_))

name = "Pedro Teixeira"

print(name.split(" ")[1])

# # --------------------------------------------------------------------------------------------

# # 6. Elabore a função standardName que deve receber um nome completo e
# # devolve uma string com o nome normalizado: inclui o primeiro e o
# # último nome e abreviaturas de todos os outros nomes intercalares.

# # example : "Pedro Miguel Silva Teixeira" -> "Pedro M. S. Teixeira


def standardName(name):
    # separa o nome por espaços
    name = name.split(" ")

    # se o nome tiver mais de 2 nomes, adiciona a abreviatura do nome
    if len(name) > 2:
        for i in range(1, len(name)-1):
            name[i] = name[i][0] + "."
       # igonrar os "de" e "da" e "do" e "das" e "dos"
        for i in range(1, len(name)-1):
            if name[i].lower() in ["de", "da", "do", "das", "dos"]:
                name[i] = name[i].lower()
                pass
    # junta o nome
    name = " ".join(name)

    return name


name = input("Nome: ")

standardName_ = standardName(name)

print("{}".format(standardName_))

# # --------------------------------------------------------------------------------------------
# # 7.Elabore a função generatePassword que funciona como um gerador de
# # passwords: a função deve receber um username, e em função desse
# # nome deve gerar uma password que é constituída da seguinte forma:
# # • Password consiste nos caracteres das posições pares do username, intercalados de um número aleatório entre 1 e 9 (inclusive).
# # • A password termina com o nº de caracteres indicados no username
# # Exemplo:
# # userName: Carlos
# # generatePassword(userName) = > Password: a3l2s76(mero exemplo)
# # Se o username incluir algum espaço a função deve devolver a mensagem
# # “username é inválido”, em alternativa à password


def generatePassword(username):
    # se o username tiver espaços, retorna mensagem de erro
    if " " in username:
        print("username é inválido")

    # se o username não tiver espaços, gera a password
    # e retorna a password
    else:
        password = ""
        for i in range(0, len(username), 2):
            # em cada caracter par, adiciona o caracter e um número aleatório entre 1 e 9
            password += username[i] + str(random.randint(1, 9))
        password += str(len(username))
        return password


username = input("Username: ")

password = generatePassword(username)

print("Password: {}".format(password))

# # --------------------------------------------------------------------------------------------
# # 8 replace any number for word


def replaceNumbers(text):
    # substitui os números por palavras
    text = text.replace("0", "zero")
    text = text.replace("1", "um")
    text = text.replace("2", "dois")
    text = text.replace("3", "três")
    text = text.replace("4", "quatro")
    text = text.replace("5", "cinco")
    text = text.replace("6", "seis")
    text = text.replace("7", "sete")
    text = text.replace("8", "oito")
    text = text.replace("9", "nove")

    return text


text = input("Texto: ")

text = replaceNumbers(text)

print("{}".format(text))

# # --------------------------------------------------------------------------------------------


def countWord(text, word):
    # conta o número de vezes que uma palavra aparece num texto
    text = text.split(" ")
    count = 0
    for i in range(len(text)):
        if text[i] == word:
            count += 1
    # onde a palavra aparece
    positions = []
    for i in range(len(text)):
        if text[i] == word:
            positions.append(i)
    print("A palavra {} ocorre {} vezes no texto. Nas posições {}".format(
        # return positions into string +1 because the first position is 1
        word, count, " ".join(str(x+1) for x in positions)))
    return count


text = input("Texto: ")
search = input("Pesquisa: ")

countWord(text, search)

# # --------------------------------------------------------------------------------------------
# # 10. . Escreva a função reverseWords que receba um texto e devolva o
# # mesmo texto, mas com as palavras por ordem inversa.


def reverseWords(text):
    # separa o texto por espaços
    text = text.split(" ")
    # inverte a ordem das palavras
    text = text[::-1]
    # junta o texto
    text = " ".join(text)
    return text


text = input("Texto: ")

text_ = reverseWords(text)

print("{}".format(text_))

# # --------------------------------------------------------------------------------------------
# # 11. Implemente a função printCharLine que receba dois argumentos:
# # um texto e o nº de caracteres que se pretende imprimir por cada
# # linha.


def printCharLine(text, n):
    # imprimir o texto em linhas de n caracteres contando os espaços
    # se o texto for menor que n caracteres, imprime o texto
    if len(text) <= n:
        print(text)
    # se o texto for maior que n caracteres, imprime o texto em linhas de n caracteres
    else:
        print(text[:n])
        printCharLine(text[n:], n)


text = input("Texto: ")

n = int(input("Nº de caracteres: "))

# printCharLine(text, n)

# --------------------------------------------------------------------------------------------
# 12. Implemente a função romanNumeral que receba um número entre 1 e
# 999 (pedido ao utilizador) e devolva o mesmo valor em numeração
# Romana


def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


def main():
    # entrada de dados
    number = int(input("Digite um número inteiro: "))
    # saída de dados
    print(int_to_roman(number))


# chamada da função principal
main()
