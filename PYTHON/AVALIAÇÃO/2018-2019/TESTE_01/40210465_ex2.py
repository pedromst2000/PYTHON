# implementar um programa que leia um número (entre 1 e 99) e determine a sua representação em linguagem binária

# Exemplo:

# Número: 12  Resultado: 1 1 0 0

import os  # para limpar a consola
print()


def convert_to_binary(number):
    binary = ''
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
# to return each digit separated by a space
    return ' '.join(binary)

#  indicação ao utilizador se pretende introduzir um novo número ou terminar o programa
# se o utilizador introduzir um número fora do intervalo [1, 99] deve continuar a pedir um novo número
# se o utilizador não introduzir um número inteiro deve continuar a pedir um novo número
# validação dos dados de entrada do número se é inteiro e se est+a entre 1 e 99


while True:
    try:
        print()
        number = int(input('Introduza um número entre 1 e 99: '))
        if number < 1 or number > 99:
            print()
            print('Número inválido!')
            print()
            continue
        print()
        print(f'Número: {number}    Resultado: {convert_to_binary(number)}')
        print()
        while True:
            print()
            answer = input('Deseja introduzir um novo número? (s/n): ')
            if answer == 's':
                break
            elif answer == 'n':
                os.system('cls')
                # close the program
                exit()
            else:
                print()
                print('Resposta inválida!')
                print()
                continue
    except ValueError:
        print()
        print('Número inválido!')
        print()
        continue
