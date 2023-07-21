import random

# listas para armazenar os valores
lista1 = []
lista2 = []

# gerar aleatoriamente os valores das listas
for i in range(10):
    lista1.append(random.randint(0, 100))
    lista2.append(random.randint(0, 100))


# verificar se existem elementos repetidos
def verificar_repetidos(lista1, lista2):
    repetidos = []
    for i in lista1:
        if i in lista2:
            repetidos.append(i)
    return repetidos

# para imprimir as listas


def imprimir_listas(lista1, lista2):
    print("Lista 1: ", end="")
    for i in range(len(lista1)):
        # para nao imprimir a virgula no ultimo elemento
        if i == len(lista1) - 1:
            print(lista1[i])
        else:
            # para imprimir a virgula entre os elementos
            print(lista1[i], end=", ")

    print()
    print("Lista 2: ", end="")
    for i in range(len(lista2)):
        if i == len(lista2) - 1:
            print(lista2[i])
        else:
            print(lista2[i], end=", ")
    print()


# para imprimir os elementos repetidos das listas
def imprimir_repetidos(repetidos):
    print("Existem {} elementos da lista 1 que se repetem na lista 2: ".format(
        len(repetidos)), end="")
    for i in range(len(repetidos)):
        # para nao imprimir a virgula no ultimo elemento
        if i == len(repetidos) - 1:
            print(repetidos[i])
        else:
            # para imprimir a virgula entre os elementos
            print(repetidos[i], end=", ")
    print()


# callback das funcoes
imprimir_listas(lista1, lista2)
imprimir_repetidos(verificar_repetidos(lista1, lista2))
