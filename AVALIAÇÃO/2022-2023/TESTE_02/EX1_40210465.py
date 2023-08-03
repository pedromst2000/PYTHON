# Numero : 40210465
# Nome : Pedro Miguel Silva Teixeira

import random
import os

# função para preencher o tabuleiro com números aleatórios
def preencheTabuleiro(linha, coluna, tabuleiro):
    # verifica se o número é repetido
    # se for repete o ciclo até ser diferente
    for i in range(linha):
        for j in range(coluna):
            while True:
                num = random.randint(1, 30)
                if num not in tabuleiro[i]:
                    tabuleiro[i][j] = num
                    break
                if num in tabuleiro[i]:
                    continue
    return tabuleiro


# inicialmente o tabuleiro apresenta o seguinte formato:
#               Tabuleiro De Jogo
# ----------------------------------------
# 0                 0                 0
# 0                 0                 0
# 0                 0                 0
# -----------------------------------------

# para imprimir o formato inicial do tabuleiro
def tabuleiroInicial():
    # criação do tabuleiro
    tabuleiro = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(0)
        tabuleiro.append(linha)

    # apresentação do tabuleiro
    print()
    print()
    print()
    # imprimir centrado o titulo
    print("            Tabuleiro De Jogo")
    print("----------------------------------------")
    for i in range(3):
        for j in range(3):
            print(tabuleiro[i][j], end="                 ")
        print()
    print("-----------------------------------------")
    print()
    return tabuleiro

#  atualiza o estado do tabuleiro após cada jogada (após desvendar uma célula (linha, coluna))

def imprimirTabuleiro(linha, coluna):
    # criação do tabuleiro
    tabuleiro = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(0)
        tabuleiro.append(linha)

    # apresentação do tabuleiro
    print()
    print()
    print()
    # imprimir centrado o titulo
    print("            Tabuleiro De Jogo")
    print("----------------------------------------")
    for i in range(3):
        for j in range(3):
            if i == linha and j == coluna:
                print("*", end="                 ")
            else:
                print(tabuleiro[i][j], end="                 ")
        print()
    print("-----------------------------------------")

    return tabuleiro

# validar coordenadas introduzidas pelo utilizador


def validarCoordenadas(linha, coluna):
    # verifica se as coordenadas estão dentro dos limites do tabuleiro entre 1 e 3
    if linha < 1 or linha > 3 or coluna < 1 or coluna > 3:
        return False
    else:
        return True


# validar se a célula já foi desvendada
def validarCelula(linha, coluna):
    # verifica se a célula já foi desvendada
    if linha == 0 or coluna == 0:
        return False
    else:
        return True

# função que devolve a soma do total de pontos visiveis no tabuleiro, após cada jogada
def somarTabuleiro(tabuleiro):
    soma = 0
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] != 0:
                soma = soma + tabuleiro[i][j]
    print("Total de pontos visiveis no tabuleiro: ", soma)
    return soma

def main():
    # inicialmente o tabuleiro apresenta o seguinte formato:
    #               Tabuleiro De Jogo
    # ----------------------------------------
    # 0                 0                 0
    # 0                 0                 0
    # 0                 0                 0
    # -----------------------------------------
    tabuleiro = tabuleiroInicial()

    # preenche o tabuleiro com números aleatórios
    tabuleiro = preencheTabuleiro(3, 3, tabuleiro)

    # inicializa o total de pontos visiveis no tabuleiro
    soma = 0

    # inicializa o número de jogadas
    jogadas = 0

    # inicializa o estado do jogo
    estado = True

    # ciclo para jogar
    while estado:
        # pede ao utilizador as coordenadas da célula que pretende desvendar
        linha = int(input("Introduza a linha: "))
        coluna = int(input("Introduza a coluna: "))

        # validar coordenadas introduzidas pelo utilizador
        if validarCoordenadas(linha, coluna) == False:
            print("Coordenadas inválidas!")
            continue

        # validar se a célula já foi desvendada
        if validarCelula(linha, coluna) == False:
            print("Célula já desvendada!")
            continue
        if validarCelula(linha, coluna) == True:

            # atualiza o estado do tabuleiro após cada jogada (após desvendar uma célula (linha, coluna))
            tabuleiro = imprimirTabuleiro(linha, coluna)

            # atualiza o total de pontos visiveis no tabuleiro
            soma = somarTabuleiro(tabuleiro)

            print(f'Pontos visiveis: {soma}')
            # atualiza o número de jogadas
        jogadas = jogadas + 1

        # o jogo termina quando o utilizador conseguir atinigr pelo menos 100 pontos nas células que tornou visiveis e dá a possibilidade de jogar novamente 'Press any key to continue . . .'
        if soma >= 100:
            print(f'Parabéns, ganhou em {jogadas} jogadas!!')
            break

        # caso torne visivel todas as posições do tabuleiro e não tenha atingido os 100 pontos, apresenta a seguinte mensagem:
        if  soma < 100 and jogadas == 9:
            print("Não conseguiu ganhar desta vez! Tente novamente!")
            break    

        # no final do jogo, apresenta a possibilidade de jogar novamente 'Press any key to continue . . .'
        # com ciclo while
        opcao = input("Press any key to continue . . .")
        if opcao != "":
            break
        else:
            continue

main()