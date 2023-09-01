# Numero : 40210465
# Nome :  Pedro Miguel da Silva Teixeira

import os

def menu():
    print("1 - Consultar atividades")
    print("2 - Melhores Tempos")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))
    return opcao


def consultarAtividades():
 
    distancia = input("Distância: ")

    ficheiro = open("atividades.txt", "r", encoding="utf-8")

    # apresentar no formato :
    #      Consulta de : 5k
    #
    #      Data       Tempo registado
    # --------------------------------
    #  2020-10-10       40,50
    #  2020-10-11       41,50
    #  2020-10-12       42,50


    print("Consulta de : ", distancia)
    print()
    print("Data       Tempo registado")
    print("--------------------------------")

    for linha in ficheiro:
        dados = linha.split(";")
        if dados[1] == distancia:
            print(dados[0], "      ", dados[2])

    ficheiro.close()

def melhoresTempos():

    distanciasValidas = ["5k", "10k", "21k"]

    distancia = input("Distância: ")

    while distancia not in distanciasValidas:
        print("Distância inválida")
        distancia = input("Distância: ")

    ficheiro = open("atividades.txt", "r", encoding="utf-8")

    print("Consulta de melhor tempo : ", distancia)

    melhorTempo = 0
    dataMelhorTempo = 0


    for linha in ficheiro:
        dados = linha.split(";")
        if dados[1] == distancia:
            if melhorTempo == 0:
                melhorTempo = dados[2]
                dataMelhorTempo = dados[0]
            elif dados[2] < melhorTempo:
                melhorTempo = dados[2]
                dataMelhorTempo = dados[0]

    print("Melhor tempo: ", melhorTempo, "Data: ", dataMelhorTempo)


def main():
    opcao = menu()
    while opcao != 0:
        if opcao == 1:
            consultarAtividades()
        elif opcao == 2:
            melhoresTempos()
        elif opcao == 0:
            print("A sair...")
            break
        else:
            print("Opção inválida")
        opcao = menu()

main()