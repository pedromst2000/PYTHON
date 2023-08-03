# 1.1
# Escreva a função escreveTexto(texto) que receba um texto(lido, p.e. através de um
# input) e o guarde num ficheiro binário, com a designação de dados.bin. Se o ficheiro
# não existir, deve ser criado com a path .\\ficheiros\\dados.bin.

# 1.2 Escreva a função lerTexto() que lê o conteúdo do ficheiro .\\ficheiros\\dados.bin e
# devolve o texto correspondente. Imprima o resultado, devolvido pela função, na consola.

# Nota: a path e o nome do ficheiro devem ser facilmente parametrizáveis no seu código
# (variáveis globais), sem que haja necessidade de alterar o código das funções acima solicitadas.


# declarar variáveis globais para a path e nome do ficheiro binário
# path = 'files'
# nome_ficheiro = 'dados.bin'

# import os

# # 1.1
# def escreveTexto(texto):
#     # => Caso o ficheiro dados.bin não exista, a sua aplicação deve criá-lo, numa
#     # sub-pasta files dentro da pasta do seu projeto.
#     if not os.path.exists(path):
#         os.mkdir(path)

#     # => Escreve o texto no ficheiro binário
#     with open(f'{path}\\{nome_ficheiro}', 'wb') as ficheiro:
#         ficheiro.write(texto.encode())

# # ------------------------------------------------------------------------------
# # 1.2
# def lerTexto():
#     # => Lê o texto do ficheiro binário
#     with open(f'{path}\\{nome_ficheiro}', 'rb') as ficheiro:
#         texto = ficheiro.read().decode()
#     return texto

# escreveTexto('texto')
# print(lerTexto())

# ----------------------------------------------------------------
# 2
# criar um programa com o objetivo de escrever/ler texto para um ficheiro criptografado. O
# seu programa deve ter duas opções:

# 2.1 Escrever em ficheiro
# Deve ler um texto, em seguida invocar uma função designada encript(texto, chave)
# que recebe esse texto e um número que representa o nº de posições a avançar na
# codificação de Cesar(neste caso, tabela ASCII).
# Vamos assumir que a Cifra de Cesar baseia-se na tabela ACSII, incluindo uma codificação de caracteres entre as posições 0 e 127.

# 2.2 Ler ficheiro
# Deve ler o ficheiro de texto criado na opção anterior, invocar a função decript(texto,
#                                                                                 chave) que devolve op texto do ficheiro, descodificado e o imprime na tela.

# MENU
# 1 - Escrever em ficheiro
# 2 - Ler ficheiro
# 0 - Sair


def menu():
    print('MENU')
    print('1 - Escrever em ficheiro')
    print('2 - Ler ficheiro')
    print('0 - Sair')
    opcao = int(input('Opção: '))
    return opcao

# 2.1
def encript(texto, chave):
    # encripta o texto
    texto_encriptado = ''
    for letra in texto:
        # converte a letra para o seu código ASCII
        codigo = ord(letra)
        # soma a chave ao código ASCII
        codigo_encriptado = codigo + chave
        # converte o código ASCII encriptado para a letra correspondente
        letra_encriptada = chr(codigo_encriptado)
        # adiciona a letra encriptada ao texto encriptado
        texto_encriptado += letra_encriptada
    # escreve o texto encriptado no ficheiro
    with open('Files\\text.txt', 'wb') as ficheiro:
        ficheiro.write(texto_encriptado.encode())

def escreverFicheiro():
    texto = input('Texto: ')
    chave = int(input('Chave: '))
    encript(texto, chave)


#2.2
def decript(texto, chave):
    # decripta o texto
    texto_decriptado = ''
    for letra in texto:
        # converte a letra para o seu código ASCII
        codigo = ord(letra)
        # subtrai a chave ao código ASCII
        codigo_decriptado = codigo - chave
        # converte o código ASCII decriptado para a letra correspondente
        letra_decriptada = chr(codigo_decriptado)
        # adiciona a letra decriptada ao texto decriptado
        texto_decriptado += letra_decriptada
    return texto_decriptado

def lerFicheiro():
    chave = int(input('Chave: '))
    with open('Files\\text.txt', 'rb') as ficheiro:
        texto = ficheiro.read().decode()
    print(decript(texto, chave))

def main():
    opcao = menu()
    while True:
        if opcao == 1:
            escreverFicheiro()
        elif opcao == 2:
            lerFicheiro()
        elif opcao == 0:
            break
        else:
            print('Opção inválida')
        opcao = menu()

main()

# ----------------------------------------------------------------