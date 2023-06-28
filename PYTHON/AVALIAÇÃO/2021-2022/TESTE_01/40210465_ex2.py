# Numero : 40210465 Nome : Pedro Teixeira

import random

paises = ["Portugal", "Espanha", "Franca", "Alemanha", "Italia", "Austria", "Belgica", "Grecia", "Letonia", "Lituania"]


# o programa deve possibilitar o utilizador adivinhar o nome do país:
# = Sortear aleatoriamente um país da lista, em função da dimensão da própria lista
# = Dispor no máximo de 3 tentavias para o utilizador acertar o nome do País
# = Antes de cada tentativa deve invocar a função imprimePais, que funciona como apoio ao utilizador, a função deve
# imprimir tantos "-" qauntos os caracteres constituiem o nome do país sorteado. A cada tentiva , a função, deve 
# desvendar um novo caracter do nome do país, como surge no exemplo seguinte:

#       Adivinhe o nome do país
#
#
#        L - - - - - - -
#
# Qual o páis? Líbia
#
# Qual o páis? Liberia
#
# Qual o páis? Lituania
#
# ACERTOU !!!!!


# inicializar variaveis
pais = random.choice(paises)
tentativas = 3


def imprimePais(pais, tentativas):
    print("Adivinhe o nome do país")
    print()
    for i in range(len(pais)):
        if i > tentativas:
            print(pais[i], end = " ")
        else:
            print("-", end = " ")
    print()


def adivinhaPais(pais, tentativas):
    while tentativas > 0:
        imprimePais(pais, tentativas)
        tentativas -= 1
        resposta = input("Qual o país? ")
        if resposta == pais:
            print("ACERTOU !!!!!")
            break
    if tentativas == 0:
        print("ERROU !!!!!")


# main
adivinhaPais(pais, tentativas)






