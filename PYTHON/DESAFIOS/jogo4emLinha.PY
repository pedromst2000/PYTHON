#EM AMBIENTE PYTHON NORMAL
# VERSÃO 1 Jogo deve contar com Player 1 e Player 2.

# => Deve pedir a indicação do nome de cada jogador (Player 1 e Player 2), jogando
# alternadamente.

# => A cada jogador é atribuído um símbolo diferente

# => Para cada jogada pede coordenadas(linha e coluna) onde o jogador
# pretende colocar a sua peça(validar se a posição é viável, de acordo
#                             com as regras)


# => Ganha o player que conseguir primeiro 4 em linha, coluna ou diagonal

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PROGRAMA

# importar bibliotecas
import os

# variáveis globais
tabuleiro = []
jogador1 = ""
jogador2 = ""
simbolo1 = ""
simbolo2 = ""
jogadorAtual = ""
simboloAtual = ""
jogadas = 0
jogadasMaximas = 42
vencedor = False

# funções


def limparEcra():
    os.system("cls")


def criarTabuleiro():
    global tabuleiro
    tabuleiro = []
    for i in range(6):
        linha = []
        for j in range(7):
            linha.append(" ")
        tabuleiro.append(linha)


def mostrarTabuleiro():
    global tabuleiro
    print("  1 2 3 4 5 6 7")
    print("  - - - - - - -")
    for i in range(6):
        print(i + 1, "|", end="")
        for j in range(7):
            print(tabuleiro[i][j], end="|")
        print()
        print("  - - - - - - -")


def pedirNomeJogador(jogador):
    global jogador1
    global jogador2
    if jogador == 1:
        jogador1 = input("Nome do jogador 1: ")
    else:
        jogador2 = input("Nome do jogador 2: ")


def pedirSimboloJogador(jogador):
    global simbolo1
    global simbolo2
    if jogador == 1:
        simbolo1 = input("Simbolo do jogador 1: ")
    else:
        simbolo2 = input("Simbolo do jogador 2: ")


def pedirJogada():
    global jogadorAtual
    global simboloAtual
    global jogadas
    global jogadasMaximas
    global vencedor
    if jogadorAtual == jogador1:
        jogadorAtual = jogador2
        simboloAtual = simbolo2
    else:
        jogadorAtual = jogador1
        simboloAtual = simbolo1
    jogadas += 1
    print("Vez de", jogadorAtual)
    print("Simbolo:", simboloAtual)
    coluna = int(input("Coluna: "))
    linha = int(input("Linha: "))
    if tabuleiro[linha - 1][coluna - 1] == " ":
        tabuleiro[linha - 1][coluna - 1] = simboloAtual
    else:
        print("Jogada inválida")
        jogadas -= 1
    if jogadas == jogadasMaximas:
        vencedor = True
        print("Empate")


def verificarVencedor():
    global vencedor
    global tabuleiro
    global jogadorAtual
    global simboloAtual
    # verificar linhas
    for i in range(6):
        for j in range(4):
            if tabuleiro[i][j] == simboloAtual and tabuleiro[i][j + 1] == simboloAtual and tabuleiro[i][j + 2] == simboloAtual and tabuleiro[i][j + 3] == simboloAtual:
                vencedor = True
                print("Vencedor:", jogadorAtual)
    # verificar colunas
    for i in range(3):
        for j in range(7):
            if tabuleiro[i][j] == simboloAtual and tabuleiro[i + 1][j] == simboloAtual and tabuleiro[i + 2][j] == simboloAtual and tabuleiro[i + 3][j] == simboloAtual:
                vencedor = True
                print("Vencedor:", jogadorAtual)
    # verificar diagonais
    for i in range(3):
        for j in range(4):
            if tabuleiro[i][j] == simboloAtual and tabuleiro[i + 1][j + 1] == simboloAtual and tabuleiro[i + 2][j + 2] == simboloAtual and tabuleiro[i + 3][j + 3] == simboloAtual:
                vencedor = True
                print("Vencedor:", jogadorAtual)
    for i in range(3):
        for j in range(3, 7):
            if tabuleiro[i][j] == simboloAtual and tabuleiro[i + 1][j - 1] == simboloAtual and tabuleiro[i + 2][j - 2] == simboloAtual and tabuleiro[i + 3][j - 3] == simboloAtual:
                vencedor = True
                print("Vencedor:", jogadorAtual)


def finalizarJogo():
    global vencedor
    global jogadorAtual
    global simboloAtual
    if vencedor == True:
        print("Vencedor:", jogadorAtual)
    else:
        print("Empate")


def iniciarJogo():
    global jogadorAtual
    global simboloAtual
    global vencedor
    criarTabuleiro()
    pedirNomeJogador(1)
    pedirSimboloJogador(1)
    pedirNomeJogador(2)
    pedirSimboloJogador(2)
    jogadorAtual = jogador1
    simboloAtual = simbolo1
    while vencedor == False:
        mostrarTabuleiro()
        pedirJogada()
        verificarVencedor()
    mostrarTabuleiro()
    finalizarJogo()


def jogarNovamente():
    global vencedor
    global jogadas
    while True:
        resposta = input("Quer jogar novamente? (S/N): ")
        if resposta == "S":
            os.system("cls")
            vencedor = False
            jogadas = 0
            iniciarJogo()
        elif resposta == "N":
            print("Obrigado por jogar")
            break
        else:
            print("Resposta inválida")


iniciarJogo()
jogarNovamente()
