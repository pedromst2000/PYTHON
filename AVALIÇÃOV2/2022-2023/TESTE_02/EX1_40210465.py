# Numero : 40210465
# Nome :  Pedro Miguel da Silva Teixeira
import random
score = 0
jogadas = 0

def tabuleiroInicial():

    tabuleiro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    return tabuleiro

def exibirTabuleiro(tabuleiro):

    print("         Tabuleiro do jogo")
    print(" -------------------------------------")
    print("        ", tabuleiro[0][0], "       ", tabuleiro[0][1], "       ", tabuleiro[0][2])
    print("        ", tabuleiro[1][0], "       ", tabuleiro[1][1], "       ", tabuleiro[1][2])
    print("        ", tabuleiro[2][0], "       ", tabuleiro[2][1], "       ", tabuleiro[2][2])
    print(" -------------------------------------")


def preencheTabuleiro(tabuleiro, linha, coluna):

    # preencher a linha ou coluna com numero aleatorio entre 1 e 30 nao repetido
    
    # preencher a linha
    for i in range(3):
        tabuleiro[linha][i] = random.randint(1, 30)

    # preencher a coluna
    for i in range(3):
        tabuleiro[i][coluna] = random.randint(1, 30)

    return tabuleiro



# função para validar a posição escolhida pelo jogador
def validarPosicao(tabuleiro, linha, coluna):	
    # verificar se a posição ja foi revelada 
    if tabuleiro[linha][coluna] == 0:
        return True
    else:
        return False
    


# função para verificar se coordenadas invalidas
def validarCoordenadas(linha, coluna):
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        return False
    else:
        return True


def somarTabuleiro(tabuleiro, linha, coluna):
    global score 
    
    # somar o total de pontos do tabuleiro
    score += tabuleiro[linha][coluna]

    return score


def imprimeTabuleiro(tabuleiro, linha, coluna):
    # atualiza o estado do tabuleiro após cada jogada
    tabuleiro[linha][coluna] = 0

    return tabuleiro

def main():

    global jogadas
    global score

    tabuleiro = tabuleiroInicial()

    exibirTabuleiro(tabuleiro)


    while True:
        # validar no fim se atingir pelo menos 100 pontos apos 9 jogadas "Parabens ganhou em 8 jogadas!! Press any key to continue..." - jogo reinicia
        # validar se o jogador atingir 9 jogadas e nao tiver 100 pontos "Não consegui ganhar desta vez! Tente Novamente! Press any key to continue..." - jogo reinicia 

        linha = int(input("Escolha a linha da célula a desvendar: "))
        coluna = int(input("Escolha a coluna da célula a desvendar: "))

        # validar se as coordenadas sao validas
        if validarCoordenadas(linha, coluna) == False:
            print("Coordenadas invalidas! Tente novamente!")
            continue

        # validar se a posição ja foi revelada
        if validarPosicao(tabuleiro, linha, coluna) == False:
            print("Posição já revelada! Tente novamente!")
            continue

        # preencher o tabuleiro com numeros aleatorios
        tabuleiro = preencheTabuleiro(tabuleiro, linha, coluna)

        # somar o total de pontos do tabuleiro
        score = somarTabuleiro(tabuleiro, linha, coluna)

        # atualiza o estado do tabuleiro após cada jogada
        tabuleiro = imprimeTabuleiro(tabuleiro, linha, coluna)

        # exibir o tabuleiro
        exibirTabuleiro(tabuleiro)

        # incrementar o numero de jogadas
        jogadas += 1

        # validar se o jogador atingir 9 jogadas e nao tiver 100 pontos "Não consegui ganhar desta vez! Tente Novamente! Press any key to continue..." - jogo reinicia
        if jogadas == 9 and score < 100:
            input("Não consegui ganhar desta vez! Tente Novamente! Press any key to continue...")
            break

        # validar no fim se atingir pelo menos 100 pontos apos 9 jogadas "Parabens ganhou em 8 jogadas!! Press any key to continue..." - jogo reinicia
        if jogadas == 9 and score >= 100:
            input("Parabens ganhou em 8 jogadas!! Press any key to continue...")
            break

main()