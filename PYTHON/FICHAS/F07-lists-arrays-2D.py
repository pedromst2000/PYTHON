# matrizes

# 1. Dada uma matriz 3x3 de inteiros, cujos valores
# são indicados pelo utilizador, elabore uma função invert que receba a matriz lida e imprima,
# assim como à sua transposta.

# inputs do user
# Linha 1, coluna 1 :
# Linha 1, coluna 2 :
# Linha 1, coluna 3 :
# Linha 2, coluna 1 :
# Linha 2, coluna 2 :
# Linha 2, coluna 3 :
# Linha 3, coluna 1 :
# Linha 3, coluna 2 :
# Linha 3, coluna 3 :

# Outpus
# Matriz lida:
# 1 2 3
# 4 5 6
# 7 8 9

# Matriz Transposta:
# 1 4 7
# 2 5 8
# 3 6 9

print()
def invert(matriz):
    print()
    print("Matriz Original:")
    for i in range(3):
        for j in range(3):
            print(matriz[i][j], end=" ")
        print()
    print()
    print()
    print("Matriz Transposta:")
    for i in range(3):
        for j in range(3):
            print(matriz[j][i], end=" ")
        print()


matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input("Linha " + str(i+1) + ", coluna " + str(j+1) + ": ")))
    matriz.append(linha)

invert(matriz)
print()

# ---------------------------------------------------------------------------------------------

# drawn a square with symbols

def square(n, symbol):
# linhas
    for i in range(n):
# colunas
        for j in range(n):
            print(symbol, end=" ")
        print()


square(5, "*")

# ---------------------------------------------------------------------------------------------
# 2. Elabore um programa com o seguinte menu inicial:


# => Inicializar matriz:
# deve pedir ao utilizador a dimensão da matriz (nº de linhas /colunas da matriz)
# e invocar uma função que preencha a matriz com valores aleatórios entre 10 e 100.
# A função deve imprimir a matriz gerada.

# => Matriz transposta: : deve invocar uma função que receba
# a matriz gerada, e imprima a sua transposta

# => Maior valor :  deve invocar uma função que
#  receba a matriz e imprima o maior valor da matriz

# => Sair: termina o programa

# inputs
# Menu
# 1. Inicializar matriz
# 2. Matriz Transposta
# 3. maior valor
# 0. Sair
# Escolha uma das opções:

# outputs
# 1. Inicializar matriz

# Dimensão da matriz: 3

# Matriz Gerada:
# 18 64 74
# 80 15 76
# 99 77 74

# 2. Matriz Transposta

# Matriz Original:
# 18 64 74
# 80 15 76
# 99 77 74

# Matriz Transposta:
# 18 80 99
# 64 15 77
# 74 76 74

# 3. maior valor
# O maior valor da matriz é 99

# programa
import random

def inicializar_matriz(n):
    matriz = []
    #linhas
    for i in range(n):
        linha = []
    #colunas
        for j in range(n):
            linha.append(random.randint(10, 100))
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz):
    # linhas
    for i in range(len(matriz)):
      # colunas
        for j in range(len(matriz)):
            print(matriz[i][j], end=" ")
        print()


# matriz transposta
def matriz_transposta(matriz):
    #linhas
    for i in range(len(matriz)):
    #colunas
        for j in range(len(matriz)):
            print(matriz[j][i], end=" ")
        print()

# # maior valor
def maior_valor(matriz):
    maior = matriz[0][0]
    #linhas
    for i in range(len(matriz)):
    #colunas
        for j in range(len(matriz)):
            if matriz[i][j] > maior:
                maior = matriz[i][j] #armazenar o maior valor
    return maior

# menu
def menu():
    print("           MENU         ")
    print("1. Inicializar matriz")
    print("2. Matriz Transposta")
    print("3. maior valor")
    print("0. Sair")
    opcao = int(input("Escolha uma das opções:"))
    return opcao

print()

def main():
    opcao = menu() # armazena o valor da opção escolhida
    while True:
        if opcao == 1:
            n = int(input("Dimensão da matriz: "))
            matriz = inicializar_matriz(n) # armaenar a matriz gerada / lista gerada
            print()
            print()
            print()
            print("Matriz Gerada:")
            # imprimir_matriz(matriz)
            print()
        elif opcao == 2:
            print()
            print()
            print("Matriz Original:")
            imprimir_matriz(matriz)
            print()
            print()
            print("Matriz Transposta:")
            matriz_transposta(matriz)
            print()
        elif opcao == 3:
            print("O maior valor da matriz é  {}".format(maior_valor(matriz)))
            print()
        elif opcao == 0:
            break
        opcao = menu()

main()

# ---------------------------------------------------------------------------------------------
# 3. Elabore um programa que permita gerir a
# ocupação de um pequeno parque de estacionamento,
# com o layout abaixo apresentado (3 filas de estacionamento, cada uma delas com
# 5 lugares).

# layout do parque de estacionamento
# 1 2 3 4 5 Fila 1
# 1 2 3 4 5 Fila 2
# 1 2 3 4 5 Fila 3

# Quando o programa se inicia, todos os lugares do parque devem estar livres.
#  O seu programa deve conter um menu com as seguintes opções:

# MENU
# 1. Entrada de veículo
# 2. Saída de carro
# 3. Estado do parque
# 0. Sair

# 1. Entrada de veículo
# deve ocupar o primeiro lugar que estiver livre, começando
# pela Fila 1 e terminando na Fila 3. Deve indicar na consola a posição do lugar a
# ocupar.
# Se todos os lugares estiverem ocupados deverá surgir a mensagem de
# “Parque completo”.

# 2. Saída de carro
# O utilizador deve indicar a posição, na fila de estacionamento, do
# carro que pretende sair(fila e lugar). Esse lugar deve passar ao estado de livre.

# 3. Estado do parque
# : esta opção deve indicar, na consola, o número de lugares
# ocupados e o número de lugares livres, no parque.

# 0. Sair
# Termina o programa.

# programa

parking = []


def enterVehicle():
    # lugares nas linhas do parque
    for i in range(len(parking)):
     #lugares nas colunas do parque
        for j in range(len(parking[i])):
            if parking[i][j] == 0:
                parking[i][j] = 1
                print("Fila: {}".format(i+1))
                print("Lugar: {}".format(j+1))
                return
    print("Parque completo")


def exitVehicle():
    fila = int(input("Fila: "))
    lugar = int(input("Lugar: "))
    if parking[fila-1][lugar-1] == 1:
        parking[fila-1][lugar-1] = 0
        print("Veículo saiu do parque")
    else:
        print("Lugar vazio")


def stateOfParking():
    ocupados = 0
    for i in range(len(parking)):
        for j in range(len(parking[i])):
            if parking[i][j] == 1:
                ocupados += 1
    print("Ocupados: {}".format(ocupados))
    print("Livres: {}".format(15-ocupados))


def menu():
    print("           MENU         ")
    print("1. Entrada de veículo")
    print("2. Saída de carro")
    print("3. Estado do parque")
    print("0. Sair")
    opcao = int(input("Escolha uma das opções:"))
    return opcao


def main():
    # no range de 3 porque são 3 filas
    for i in range(3):
        parking.append([0, 0, 0, 0, 0])
    opcao = menu() # armazena o valor da opção escolhida
    while True:
        if opcao == 1:
            enterVehicle()
        elif opcao == 2:
            exitVehicle()
        elif opcao == 3:
            stateOfParking()
        elif opcao == 0:
            break
        opcao = menu()


main()
# ---------------------------------------------------------------------------------------------
# 4. Implemente um programa que permita somar e subtrair duas matrizes (devem ter a
# mesma ordem, isto é, as duas matrizes devem ter igual número de linhas e colunas).

# => Somar duas matrizes

# 5 4          0 -2      5 2
# 0 2    +     5 -3   =  5 -1
# 1 -1         -1 0      0 -1


# => Subtrair duas matrizes

# 5 4          0 -2      5 6
# 0 2    -     5 -3   =  -5 5
# 1 -1         -1 0      2 -1

# menu
# MENU
# 1. Somar matrizes
# 2. Subtrair matrizes
# 0. Terminar
# input Opção:

# outputs
# se selecionar a opção 1 ou 2 deve pedir número de linhas e colunas das matrizes
# duas matrizes devem ter a mesma ordem, isto é, as duas matrizes devem ter igual número de linhas e colunas

# Número de linhas: 3
# Número de colunas: 2

# Matriz 1:         Matriz 2:          Matriz Resultado:
# 1 2               1  0                    2  2
# 3 0               2  2                    5  2
# 2 1               3  3                    5  4


# imprimir o segunite resultado_

# Número de linhas: 3
# Número de colunas: 2

# Matriz 1:         Matriz 2:          Matriz Resultado:
# 1 2               1  0                    0  2
# 3 0               2  2                   -1 -2
# 2 1               3  3                   -1 -2


# programa

def menu():
    print("           MENU         ")
    print("1. Somar matrizes")
    print("2. Subtrair matrizes")
    print("0. Terminar")
    opcao = int(input("Escolha uma das opções:"))
    return opcao


def createMatrix():
    linhas = int(input("Número de linhas: "))
    colunas = int(input("Número de colunas: "))
    matrix = []
    for i in range(linhas):
        matrix.append([])
        for j in range(colunas):
            matrix[i].append(int(input("Elemento [{}][{}]: ".format(i+1, j+1))))
    return matrix


def sumMatrix(matrix1, matrix2):
    matrixResult = []
    for i in range(len(matrix1)):
        matrixResult.append([])
        for j in range(len(matrix1[i])):
            matrixResult[i].append(matrix1[i][j] + matrix2[i][j])
    return matrixResult


def subMatrix(matrix1, matrix2):
    matrixResult = []
    for i in range(len(matrix1)):
        matrixResult.append([])
        for j in range(len(matrix1[i])):
            matrixResult[i].append(matrix1[i][j] - matrix2[i][j])
    return matrixResult


# imprimir as matrizes com espaços entre as matrizes na horizontal


def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()


def main():
    opcao = menu()
    while True:
        if opcao == 1:
            print("Matriz 1:")
            matrix1 = createMatrix()
            print("Matriz 2:")
            matrix2 = createMatrix()
            matrixResult = sumMatrix(matrix1, matrix2)
            print("Matriz Resultado:")
            printMatrix(matrixResult)
        elif opcao == 2:
            print("Matriz 1:")
            matrix1 = createMatrix()
            print("Matriz 2:")
            matrix2 = createMatrix()
            matrixResult = subMatrix(matrix1, matrix2)
            print("Matriz Resultado:")
            printMatrix(matrixResult)
        elif opcao == 0:
            break
        opcao = menu()


main()

# ---------------------------------------------------------------------------------------------
