# Adivinha o País

# implementar programa com o objetivo de adivivinhar um país,
# em função de letras que vão sendo geradas aleatoriamente pelo o programa

# => deve sortear um dos países da lista de países e imprimir tantos "_"
#   quantas as letras que o país tem a adivinhar

# => deve sortear letras aleatórias e nunca repetidas. Se a letra sorteada
# existir no país a adivinhar, deve apresenta-la na posição correta

# => deve perguntar ao utilizador se deseja obter uma nova letra, em caso de sim
# o jogo gera uma nova letra e o processo repete-se.

# => caso indique que não deseja uma nova letra, poderá tentar adivinhar o nome do país

# => Indicar se o jogador acertou o nome do país ou não
import random

# lista de países
paises = ["Portugal", "Espanha", "Franca", "Alemanha", "Holanda",
          "Itália", "Polonia", "Belgica", "Bulgaria", "Austria"]
# lista de letras de A a Z
letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
          "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
          "U", "V", "X", "Y", "Z"]


print()
# imprimir tantos "_" quantas as letras que o país tem a adivinhar


def imprimePais(pais):
    for i in range(len(pais)):
        print(" _ ", end=" ")
    print("\n")


def sortearLetra():
    # sortear uma letra aleatória
    letra = random.choice(letras)
    print("Letra sorteada: ", letra)
    caracteres = len(letra)
    return letra


def verificarLetra(letra, pais):
    # se a letra gerada existir no país , apresentar nos tantos "_" na posição correta
    if letra in pais:
        print("Letra existe no país")
        print("Letra: ", letra)
        for i in range(len(pais)):
            if letra == pais[i]:
                print(letra, end=" ")
            else:
                print(" _ ", end=" ")
        print("\n")


print()
print()
print()


    
def main():
    caracteres = 0
    pais = random.choice(paises)
    letra = sortearLetra()
    imprimePais(pais)
    op = input("Deseja obter uma nova letra? (S/N): ")

    print()
    print()
    print()
    while op == "S":
        imprimePais(pais)
        print(f'pais sorteado: {pais}')
        verificarLetra(letra, pais)
        op = input("Deseja obter uma nova letra? (S/N): ")
        if op == "S" or op == "s":
            letra = sortearLetra()
            # # incrementar o número de caracteres
            caracteres += 1
            print(f'caracteres: {caracteres}')
        elif op == "N" or op == "n":
            adivinhar = input("Qual o país? ")
            if adivinhar == pais:
                print(f'Parabéns, acertou o país com {caracteres} caracteres!')
                break
            break

main()
