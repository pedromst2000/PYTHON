# implementar um pequeno jogo em que o objetivo é de conseguir obter, numa jogada, dois números
# seguidos

# o jogo deve gerar em cada jogada 5 números aleatórios entre 1 e 30, não repetidos

# se na sequência de 5 números se encontrarem dois consecutivos, o jogo termina
# mostrando o número de jogadas efetuadas para conseguir a sequeência

# exemplo , á segunda jogada conseguiu-se obter os números 28 e 29 que são consecutivos

# 14     24     18    20     9
# 28      2     29    10     15
#
#
#
# Conseguiu obter uma sequência de dois núumeros em 2 jogadas !

# Caso a sequência de 5 números aleatórios não contenha dois consecutivos, então o jogo deve continuar, surgindo a
# mensagem “prima enter para gerar nova jogada

import random

print()
numeros = []

# gerar numeros aleatorios
def gerar_numeros():
    for i in range(5):
        # se o numero gerado ja existir, gerar outro
        while True:
            numero = random.randint(1, 30)
            if numero not in numeros:
                numeros.append(numero)
                break
            else:
                continue

# verificar numeros consecutivos
def verificar_numeros(numeros):
    for i in range(len(numeros) - 1):
        if numeros[i] + 1 == numeros[i + 1]:
            return True
    return False

# imprimir numeros
def imprimir_numeros(numeros):
    for i in range(len(numeros)):
        print(numeros[i], end=" ")
    print()


def main():
    jogadas = 0
    while True:
        print()
        gerar_numeros()
        print()
        imprimir_numeros(numeros)
        print()
        jogadas += 1
        if verificar_numeros(numeros):
            print()
            print(f"\nConseguiu obter uma sequência de dois números em {jogadas} jogadas !")
            print()
            break
        else:
            print()
            numeros.clear()
            input("Prima enter para gerar nova jogada")
            print()
            continue
main()