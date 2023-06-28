# jogo do adivinha o país com implementação de ficheiros

import random
import os

# => Deve ler o ficheiro paises.txt para uma lista e em seguida sortear, aleatoriamente,
# um país da lista, em função da dimensão da própria lista.

# => Deve dispor no máximo de 3 tentativas para o utilizador acertar no nome do país.

# => Antes de cada tentativa, deve invocar a função imprimePais(), que funciona como
# uma ajuda ao utilizador: a função deve imprimir tantos “-“ quantos os caracteres
# que constituem o nome do país sorteado. A cada tentativa, a função deve desvendar um novo caracter do nome do país, como surge nas imagens abaixo.

# exemplo de output:
# Adivinha o nome do país
#
#   L - - - - - - - -
#
# Qual o nome do país? Libia
#
#   L i - - - - - - -
#
# Qual o nome do país? Lituânia

# ACERTOU!!

filename = "DESAFIOS\\jogoAdivinhaPais\\paises.txt"
file = open(filename, encoding="utf8")

countries = []

for line in file:
    countries.append(line.strip())

file.close()

print()
print("          Adivinha o nome do país             ")


def imprimePais(pais, tentativa):
    print()
    for i in range(len(pais)):
        if i < tentativa:
            print(pais[i], end=" ")
        else:
            print("-", end=" ")
    print()


def main():
    while True:
        # escolhe um país aleatório
        country = random.choice(countries)

        # imprime o país com as letras escondidas
        for i in range(3):
            imprimePais(country, i + 1)
            print()
            guess = input("Qual o nome do país? ")
            print()
            if guess == country:
                print("ACERTOU!!")
                break
            else:
                print("ERROU!!")
        else:
            print("O país era", country)

        # pergunta se quer jogar novamente
        print()
        again = input("jogar novamente? (S/N) ")
        print()
        if again == "S" or again == "s":
            os.system("cls")
            print("          Adivinha o nome do país             ")
            continue
        elif again == "N" or again == "n":
            print("Obrigado por jogar")
            break
        else:
            print("Opção inválida")
            break
main()
