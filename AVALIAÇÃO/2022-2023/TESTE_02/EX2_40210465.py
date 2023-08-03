# Numero : 40210465
# Nome : Pedro Miguel Silva Teixeira
import os

# consultarAtividades através da leitura do ficheiro atividades.txt


def consultarAtividades():
    # ler o ficheiro
    f = open("atividades.txt", "r")
    # ler o ficheiro e guardar numa lista
    lista = f.readlines()
    # fechar o ficheiro
    f.close()

    # pedir ao utilizador a distancia
    distancia = input(
        "Qual a distancia que pretende consultar? (5k, 10k ou 21k) ")

    # verificar se a distancia é valida
    if distancia == "5k" or distancia == "10k" or distancia == "21k":

        # imprime a consulta da distancia
        print("Consulta de: " + distancia.upper())
        print()
        print("Data\t\t\tTempo registado")
        print("----------------------------------------")

        # percorrer a lista
        for i in range(len(lista)):
            # separar a data, a distancia e o tempo
            data, dist, tempo = lista[i].split(";")
            # verificar se a distancia é igual à distancia que o utilizador pretende
            if distancia == dist:
                # imprimir a data e o tempo
                print(data + "\t" + tempo)

    else:
        # imprimir mensagem de erro
        print("Distancia invalida!")


# melhoresTempos através da leitura do ficheiro atividades.txt
def melhoresTempos():
    # ler o ficheiro
    f = open("atividades.txt", "r")
    # ler o ficheiro e guardar numa lista
    lista = f.readlines()
    # fechar o ficheiro
    f.close()

    # imprimir o cabeçalho
    print("Melhores tempos")
    print("----------------------------------------")

    # percorrer a lista
    for i in range(len(lista)):
        # separar a data, a distancia e o tempo
        data, dist, tempo = lista[i].split(";")
        # verificar se a distancia é igual à distancia que o utilizador pretende
        if dist == "5k" or dist == "5K":
            # guardar o tempo e a data
            tempo5k = tempo
            data5k = data
        elif dist == "10k" or dist == "10K":
            # guardar o tempo e a data
            tempo10k = tempo
            data10k = data
        elif dist == "21k" or dist == "21K":
            # guardar o tempo e a data
            tempo21k = tempo
            data21k = data

    # imprime os melhores tempos
    print("Data\t\t\tTempo registado")
    print("----------------------------------------")
    # imprimir o tempo e a data do 5k lado a lado
    print("5K: " + tempo5k + "\t\t" + data5k)
    # imprimir o tempo e a data do 10k lado a lado
    print("10K: " + tempo10k + "\t\t" + data10k)
    # imprimir o tempo e a data do 21k lado a lado
    print("21K: " + tempo21k + "\t\t" + data21k)
    print("----------------------------------------")


def main():
    # imprimir o menu
    print()
    print("MENU")
    print("1. Consultar atividades")
    print("2. Melhores tempos")
    print("0. Sair")
    print()

    # pedir ao utilizador a opção
    opcao = input("Qual a opção? ")
    print()
    # dar a possibilidade ao utilizador de selecionar outra opção
    while opcao != "0":
        # verificar se a opção é valida
        if opcao == "1":
            # chamar a função consultarAtividades
            consultarAtividades()
        elif opcao == "2":
            # chamar a função melhoresTempos
            melhoresTempos()
        else:
            # imprimir mensagem de erro
            print("Opção invalida!")

        # imprimir o menu
        print()
        print("MENU")
        print("1. Consultar atividades")
        print("2. Melhores tempos")
        print("0. Sair")
        print()

        # pedir ao utilizador a opção
        opcao = input("Qual a opção? ")
        print()


main()
