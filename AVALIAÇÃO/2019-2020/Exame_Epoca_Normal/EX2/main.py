import random
import sys
import os

# para armazenar os numeros
numeros = []
# para armazenar as estrelas
estrelas = []

while True:
    print(f'Chave Euromilhões: {numeros} + {estrelas}')
    resposta = input('pretende gerar nova chave Euromilhões? (s/n) ')
    if resposta == 's': # se a resposta for 's' => gera nova chave
        numeros = []
        estrelas = []
        # para gerar numeros aleatorios entre 1 e 50
        while len(numeros) < 5:
            num = random.randint(1, 50)
            # se o numero não estiver na lista, adiciona a lista
            if num not in numeros: # para lidar com numeros repetidos
                numeros.append(num)
        # para gerar numeros aleatorios entre 1 e 12
        while len(estrelas) < 2: # para gerar 2 estrelas aleatorias
            estrela = random.randint(1, 12) # para gerar numeros aleatorios entre 1 e 12
            if estrela not in estrelas: # para lidar com numeros repetidos
                estrelas.append(estrela)
        numeros.sort() # ordena os numeros
        estrelas.sort() # ordena as estrelas
    elif resposta == 'n': # se a resposta for 'n' => termina o programa
        os.system('cls') # limpa o ecrã / consola
        sys.exit() # termina o programa

    else:
        print('resposta inválida')