# aplicação que permita gerir um ficheiro de países

# deve incluir um menu:
# MENU
# 1 - Inserir Países
# 2 - Consulta Países
# 3 - Consulta por continente
# 4 - Consulta nº países por continente
# 0 - Sair
#          opção:

# 1 - Inserir Países
# => Pede ao utilizador a introdução de país e de continente
# => Caso o ficheiro países.txt não exista, a sua aplicação deve criá-lo, numa
# sub-pasta files dentro da pasta do seu projeto.
# => Verifica se o país já existe no ficheiro. Caso exista deve informar o utilizador e não duplicar o nome do país no ficheiro
# => Caso o país ainda não exista no ficheiro, deve acrescentá-lo ao ficheiro de
# países

# 2 - Consulta Países
# => Deve invocar uma função que permita listar todos os países existentes no ficheiro países.txt
# listar todos os países com o seguinte output:
# País         Continente
# --------------------------
# Portugal     Europa
# Portugal   Europa
# Espanha    Europa
# França     Europa
# Grécia     Europa
# Hungria    Europa
# Irlanda    Europa
# Itália     Europa
# Letónia    Europa
# Lituânia   Europa
# Luxemburgo Europa
# EUA        América
# Brasil     América
# Peru       América
# Colombia   América
# China      Asia
# Japão      Asia
# Tailândia  Asia
# Malásia    Asia
# Pág. 1. Prima <Enter> para continuar

# 3 - Consulta por continente
# => Deve solicitar ao utilizador a indicação do continente.
# => Em seguida, deve invocar uma função(que receba o continente indicado pelo
#                                       utilizador) que permita listar os países, em ficheiro, desse continente.

# exemplo de input
# input: continente : Europa

# listar todos os países desse continente com o seguinte output:
# País         Continente
# --------------------------
# Portugal    Europa
# Espanha     Europa
# França      Europa
# Grécia      Europa
# Hungria     Europa
# Irlanda     Europa
# Itália      Europa
# Letónia     Europa
# Lituânia    Europa
# Luxemburgo  Europa

# 4 - Consulta nº países por continente
# => Esta opção deve invocar uma função que imprima o nº de países, em ficheiro, para cada continente

# exemplo de output
# Continente  Nº Países
# --------------------------
# Europa      10
# América     3
# Ásia        4

# 0 - Sair
# => Termina a aplicação

import os


def menu():
    print('MENU')
    print('1 - Inserir Países')
    print('2 - Consulta Países')
    print('3 - Consulta por continente')
    print('4 - Consulta nº países por continente')
    print('0 - Sair')
    opcao = int(input('opção: '))
    return opcao


def inserir_paises():
    # => Pede ao utilizador a introdução de país e de continente
    pais = input('País: ')
    continente = input('Continente: ')

    # => Caso o ficheiro países.txt não exista, a sua aplicação deve criá-lo, numa
    # sub-pasta files dentro da pasta do seu projeto.
    if not os.path.exists('files'):
        os.mkdir('files')

    # => Verifica se o país já existe no ficheiro. Caso exista deve informar o utilizador e não duplicar o nome do país no ficheiro
    # => Caso o país ainda não exista no ficheiro, deve acrescentá-lo ao ficheiro de
    # países
    with open('Files\\paises.txt', 'a+') as ficheiro:
        ficheiro.seek(0)
        for linha in ficheiro:
            if linha.split(';')[0] == pais:
                print('País já existe')
                break
        else:
            ficheiro.write('\n'f'{pais};{continente}')


def consulta_paises():

    with open('Files\\paises.txt', 'r') as ficheiro:
        print('País         Continente')
        print('--------------------------')
        for linha in ficheiro:
            print(linha.strip().replace(';', ' ' * 10))


def consulta_continente():

    continente = input('Continente: ')
    with open('Files\\paises.txt', 'r') as ficheiro:
        print('País         Continente')
        print('--------------------------')
        for linha in ficheiro:
            if linha.split(';')[1].strip() == continente:
                print(linha.strip().replace(';', ' ' * 10))


def consulta_paises_continente():
    continentes = {}
    with open('Files\\paises.txt', 'r') as ficheiro:
        for linha in ficheiro:
            continente = linha.split(';')[1].strip()
            if continente not in continentes:
                continentes[continente] = 1
            else:
                continentes[continente] += 1
    print('Continente  Nº Países')
    print('--------------------------')
    for continente, count in continentes.items():
        print(f'{continente}      {count}')


def main():
    opcao = menu()
    while opcao != 0:
        if opcao == 1:
            inserir_paises()
        elif opcao == 2:
            consulta_paises()
        elif opcao == 3:
            consulta_continente()
        elif opcao == 4:
            consulta_paises_continente()
        else:
            print('Opção inválida')
        opcao = menu()


main()

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# aplicação que permita gerir um ficheiro de leitura de dados

# etende-se desenvolver um programa que permita
# ler/consultar os dados registados no ficheiro temperatura.txt, ficheiro esse que contém dados devolvidos pela leitura de um sensor de temperatura

# deve incluir um menu:
# MENU
# 1 - Consulta por data
# 2 - Consulta Estatística
# 0 - Sair
# opção:


def menu():
    print('MENU')
    print('1 - Consulta por data')
    print('2 - Consulta Estatística')
    print('0 - Sair')
    opcao = int(input('opção: '))
    return opcao

# consulta por data
# => Deve solicitar ao utilizador a indicação de uma data e consulta
# todos os registos no ficheiro para a data pretendida

# exemplo de input
# input: data de Consulta : 2020-01-01

# exemplo de output
# Data       Hora    Temperatura
# --------------------------------
# 2020-01-01 00:00:00  20.0
# 2020-01-01 00:01:00  20.0
# 2020-01-01 00:02:00  20.0


def consulta_data():
    data = input('Data de Consulta: ')
    with open('Files\\temperatura.txt', 'r') as ficheiro:
        print('Data       Hora    Temperatura')
        print('--------------------------------')
        for linha in ficheiro:
            if linha.split(';')[0] == data:
                print(linha.strip().replace(';', ' ' * 8))
        # se não existir a data no ficheiro imprime a mensagem abaixo
        else:
            print('Data não encontrada')

# coonsulta estatística
# Esta opção permite obter a temperatura mínima, temperatura máxima e temperatura
# média observada nos dados contidos no ficheiro temperatura.txt.

# exemplo de output
# O maior valor de temperatura registado foi de 27
# O menor valor de temperatura registado foi de 18
# O valor médio de temperatura registado foi de 22.69


def consulta_estatistica():
    temperaturas = []
    with open('Files\\temperatura.txt', 'r') as ficheiro:
        for linha in ficheiro:
            temperaturas.append(int(linha.split(';')[2]))
    print(
        f'O maior valor de temperatura registado foi de {max(temperaturas)} ºC')
    print(
        f'O menor valor de temperatura registado foi de {min(temperaturas)} ºC')
    print(
        f'O valor médio de temperatura registado foi de {sum(temperaturas) / len(temperaturas):.2f} ºC')


def main():
    opcao = menu()
    while True:
        if opcao == 1:
            consulta_data()
        elif opcao == 2:
            consulta_estatistica()
        elif opcao == 0:
            break
        else:
            print('Opção inválida')
        opcao = menu()


main()
