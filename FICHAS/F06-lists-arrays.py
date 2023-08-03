# # lib: random, os
import random
import math
import os

# # ----------------------------------------------------------------------------------------------
# # 1.


def aboveAverage(*nums):
    average = sum(nums) / len(nums)
    return [num for num in nums if num > average]


nums = []

for i in range(10):
    nums.append(int(input("Enter a number: ")))

print(aboveAverage(*nums))

# # ----------------------------------------------------------------------------------------------
# # 2. gerar chaves euro milhões


def generateNumbers(limInferior, limSuperior, quantityNums):
    return [random.randint(limInferior, limSuperior) for i in range(quantityNums)]


numbers = []
op = ""

for i in range(5):
    numbers.append(generateNumbers(1, 50, 5))

stars = generateNumbers(1, 12, 2)

while True:
    print(" Chave do Euromilhões:   {}".format(numbers[0]), end="       ")
    print("Estrelas: {}".format(stars))
    op = input("Deseja gerar nova Chave? (S/N): ")
    if op == "S" or op == "s":
        # para gerar nova chave
        numbers.pop(0)
        numbers.append(generateNumbers(1, 50, 5))
        stars = generateNumbers(1, 12, 2)
    else:
        break

# # ----------------------------------------------------------------------------------------------
# # 3.
# # Crie um programa que leia a pontuação de 10 participantes num concurso de programação (a pontuação deve estar validada entre 0 a 20, por uma estrutura try -except ).
# # O programa deve invocar uma função, positiveList que receba a lista das 10 pontuações e devolva uma nova lista apenas com as pontuações positivas ( >= 10).


def positiveList(*nums):
    return [num for num in nums if num >= 10]


nums = []

for i in range(10):
    while True:
        try:
            num = int(input("Pontuação: "))
            if num < 0 or num > 20:
                raise ValueError
            else:
                nums.append(num)
                break
        except ValueError:
            print("Número Inválido! Tente novamente")

print("Pontuações Positivas: {}".format(positiveList(*nums)))

# # ----------------------------------------------------------------------------------------------
# # 4. versão 2 do exercício 3 com inclusão de nome dos participantes

# # exmplo de output
# # Nomes : ["João", "Maria", "Pedro"]
# # Pontuações : [10, 15, 20]


def positiveList(names, *nums):
    return [names[nums.index(num)] for num in nums if num >= 10]


names = []
nums = []

for i in range(3):
    while True:
        try:
            name = input("Nome: ")
            num = int(input("Pontuação: "))

            if num < 0 or num > 20:
                raise ValueError
            else:
                names.append(name)
                nums.append(num)
                break
        except ValueError:
            print("Número Inválido! Tente novamente")


os.system("cls")
print()
print("Participantes com pontuações positivas")
print()

print("Nomes: {}".format(positiveList(names, *nums)))
print("Pontuações: {}".format(positiveList(nums, *nums)))

print()

# # ----------------------------------------------------------------------------------------------
# # 5.  Elabore um programa que permita ler a faturação mensal de uma empresa ao longo
# # dos 12 meses do ano(de janeiro a dezembro).

# # invocar 3 funções:
# # o mês de maior faturação
# # o mês de menor faturação
# # a média de faturação


def maiorFaturacao(*nums):
    return max(nums)


def menorFaturacao(*nums):
    return min(nums)


def mediaFaturacao(*nums):
    return sum(nums) / len(nums)


januaryFat = int(input("Faturação de Janeiro: "))
februaryFat = int(input("Faturação de Fevereiro: "))
marchFat = int(input("Faturação de Março: "))
aprilFat = int(input("Faturação de Abril: "))
mayFat = int(input("Faturação de Maio: "))
juneFat = int(input("Faturação de Junho: "))
julyFat = int(input("Faturação de Julho: "))
augustFat = int(input("Faturação de Agosto: "))
septemberFat = int(input("Faturação de Setembro: "))
octoberFat = int(input("Faturação de Outubro: "))
novemberFat = int(input("Faturação de Novembro: "))
decemberFat = int(input("Faturação de Dezembro: "))

print()

nums = [januaryFat, februaryFat, marchFat, aprilFat, mayFat, juneFat,
        julyFat, augustFat, septemberFat, octoberFat, novemberFat, decemberFat]

# igualar as posições dos meses com as posições dos valores
months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
          "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]


print("Mês de maior faturação: {}".format(
    months[nums.index(maiorFaturacao(*nums))]))

print()

print("Mês de menor faturação: {}".format(
    months[nums.index(menorFaturacao(*nums))]))

print()

print("Valor médio de faturação: {:.2f}".format(mediaFaturacao(*nums)))

print()
# # ----------------------------------------------------------------------------------------------
# # 6. Elabore um programa que leia uma lista de 10 números inteiros.
# # Em seguida, dado um determinado valor de pesquisa, invoque a função searchNumber(lista, pesquisa) que deve devolver as posições em que encontra o valor de pesquisa,
# # na lista.
# # Caso o valor de pesquisa não exista na lista, deve surgir uma mensagem adequada


def searchNumber(lista, pesquisa):
    return [lista.index(num) for num in lista if num == pesquisa]


lista = []

for i in range(10):
    while True:
        try:
            num = int(input("Número: "))
            lista.append(num)
            break
        except ValueError:
            print("Número Inválido! Tente novamente")

pesquisa = int(input("Valor de pesquisa: "))

print()

if pesquisa in lista:
    print("Posições em que o valor de pesquisa se encontra na lista: {}".format(
        searchNumber(lista, pesquisa)))
else:
    print("O valor de pesquisa não existe na lista!")

print()

# # ----------------------------------------------------------------------------------------------
# # 7. O Instituto de metereologia pretende registar o valor total de pluviosidade ocorrida em
# # cada mês, ao longo de um ano(de janeiro a dezembro).
# # Implemente a função pluviosidade que receba a lista com a pluviosidade de cada mês,
# # e imprima esses mesmos dados(lista de pluviosidade), mas ordenados por ordem decrescente de pluviosidade.


def pluviosidade(*nums):
    return sorted(nums, reverse=True)


januaryPluv = int(input("Pluviosidade de Janeiro: "))
februaryPluv = int(input("Pluviosidade de Fevereiro: "))
marchPluv = int(input("Pluviosidade de Março: "))
aprilPluv = int(input("Pluviosidade de Abril: "))
mayPluv = int(input("Pluviosidade de Maio: "))
junePluv = int(input("Pluviosidade de Junho: "))
julyPluv = int(input("Pluviosidade de Julho: "))
augustPluv = int(input("Pluviosidade de Agosto: "))
septemberPluv = int(input("Pluviosidade de Setembro: "))
octoberPluv = int(input("Pluviosidade de Outubro: "))
novemberPluv = int(input("Pluviosidade de Novembro: "))
decemberPluv = int(input("Pluviosidade de Dezembro: "))
print()

numsPluv = [januaryPluv, februaryPluv, marchPluv, aprilPluv, mayPluv, junePluv,
            julyPluv, augustPluv, septemberPluv, octoberPluv, novemberPluv, decemberPluv]


mouthsPluv = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
              "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]


for i in range(len(numsPluv)):
    # igualar as posições dos meses com as posições dos valores de pluviosidade e ordenar por ordem decrescente
    print("{}: {}".format(mouthsPluv[numsPluv.index(
        pluviosidade(*numsPluv)[i])], pluviosidade(*numsPluv)[i]))

print()

# # ----------------------------------------------------------------------------------------------
# # 8. Dado uma lista de N elementos (N deve ser pedido ao utilizador), crie uma função que
# # ordene a lista e que permita gerar uma outra lista sem valores duplicados.


def ordenarLista(lista):
    return sorted(lista, reverse=False)


def listaSemDuplicados(lista):
    return list(set(lista))


lista = []

while True:
    try:
        n = int(input("Número de elementos da lista: "))
        break
    except ValueError:
        print("Número Inválido! Tente novamente")

print()

for i in range(n):
    while True:
        try:
            num = int(input("Número: "))
            lista.append(num)
            break
        except ValueError:
            print("Número Inválido! Tente novamente")

print()

print("Lista inicial: {}".format(ordenarLista(lista)))

print()

print("Lista gerada: {}".format(listaSemDuplicados(lista)))

print()

# # ----------------------------------------------------------------------------------------------
# # 9.Implemente um programa que permita ler o número de visitantes numa exposição, que
# # decorre de Domingo a Sábado

# # três funções:
# # função para número de média de visitantes diários
# # função para listar o número de vistantes de cada dia por ordem decrescente
# # função para devolver o dia mais próximo da média


def mediaVisitantes(*nums):
    return sum(nums) / len(nums)

# função para listar o número de vistantes de cada dia por ordem decrescente


def listaVisitantes(*nums):
    return sorted(nums, reverse=True)


def diaMaisProximoMedia(*nums):
    return nums.index(min(nums, key=lambda x: abs(x - mediaVisitantes(*nums))))


# lista com os dias da semana
days = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

# lista com os valores de visitantes
visitantes = []


for i in range(len(days)):

    while True:

        try:
            num = int(input("{}: ".format(days[i])))
            visitantes.append(num)
            break

        except ValueError:
            print("Número Inválido! Tente novamente")


print()

for i in range(len(visitantes)):
    # igualar as posições dos dias com as posições dos valores de visitantes e ordenar por ordem decrescente
    print("{}: {}".format(days[visitantes.index(
        listaVisitantes(*visitantes)[i])], listaVisitantes(*visitantes)[i]))


print()

print("Nº média de visitas diárias: {:.2f}".format(
    mediaVisitantes(*visitantes)))

print()

print("Dia mais próximo do valor médio: {}".format(
    days[diaMaisProximoMedia(*visitantes)]))

print()

# ----------------------------------------------------------------------------------------------
# 10. Elabore um programa que permita gerir uma fila de espera (como num supermercado,
# ou num serviço de atendimento) com capacidade máxima para 20 lugares.
#     Quando o programa se inicia, todos os lugares da fila devem estar livres.

#     O programa deve apresentar um menu com as seguintes opções:
# 1 – Tirar Ticket
# 2 - Atendimento
# 3 - Estado da fila de espera
# 0 - Sair

# Opção Tirar Ticket
# Deve chamar uma função que permita ocupar o primeiro lugar que estiver livre
# na fila de espera, indicando na consola a posição ocupada(ou seja, o número do
#                                                           ticket).
# Se todos os lugares estiverem ocupados deverá surgir a mensagem de “Fila completa”.

# • Opção Atendimento
# Deve invocar uma função que permita atender sempre o elemento que está na
# primeira posição da fila de espera, num dado momento(imprime o nº da sua senha na consola).
# Neste caso, todos os restantes elementos da fila de espera devem avançar uma
# posição à frente

# • Opção Estado da fila de espera
# Deve invocar uma função que imprima, na consola, o número de lugares ocupados e o número lugares livres na fila de espera.

# • Opção Sair
# Termina a execução do programa


def tirarTicket(fila):
    if fila.count(0) == 0:
        print("Fila completa")
    else:
        fila[fila.index(0)] = fila.index(0) + 1
        print("Ticket nº {}".format(fila.index(0) + 1))


def atendimento(fila):
    if fila.count(0) == 20:
        print("Fila vazia")
    else:
        print("Ticket nº {}".format(fila[0]))
        fila.remove(fila[0])
        fila.append(0)


def estadoFila(fila):
    print("Lugares ocupados: {}".format(20 - fila.count(0)))
    print("Lugares livres: {}".format(fila.count(0)))


fila = [0] * 20

# while loop para o menu e verificar se o input é um número com isdigit()

while True:
    print("1 - Tirar Ticket")
    print("2 - Atendimento")
    print("3 - Estado da fila de espera")
    print("0 - Sair")

    opcao = input("Opção: ")

    if opcao.isdigit():
        opcao = int(opcao)

        if opcao == 1:
            tirarTicket(fila)
        elif opcao == 2:
            atendimento(fila)
        elif opcao == 3:
            estadoFila(fila)
        elif opcao == 0:
            break
        else:
            print("Opção inválida")

    else:
        print("Opção inválida")

    print()

# ----------------------------------------------------------------------------------------------
