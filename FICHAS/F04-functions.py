# 1.  Adapte o exercício doa ficha 03 – sequência de Fibonacci, de forma
# que implemente uma função Finbonacci que imprima os n primeiros
# termos da sequência, sendo esse n passado como argumento da função.

import math


def fibonnaci(number):
    a = 0
    b = 1
    c = 0
    for i in range(0, number):
        if i == number - 1:
            print(a, end="")
        else:
            print(a, end=", ")
        c = a + b
        a = b
        b = c


number = int(input("Indique um número: "))

fibonnaci(number)

# ------------------------------------------------------------------------
# # 2. Implemente a função somatório que receba 2 números como argumento
# de entrada, e imprima o somatório de todos os números desse intervalo.
# Exemplo:
# somatório(1, 3) a função deve imprimir 6
# somatório(3, 6) a função deve imprimir 18


def somatorio(num1, num2):
    soma = 0
    for i in range(num1, num2+1):
        soma += i
    print(soma)


somatorio(1, 3)

# ------------------------------------------------------------------------
# 3.  Implemente a função abundante que receba um número inteiro e devolva True ou False, conforme o número seja abundante ou não.


def abundante(num):
    soma = 0
    for i in range(1, num):
        if num % i == 0:
            soma += i
    if soma > num:
        return True
    else:
        return False


print(abundante(10))  # False
print(abundante(12))  # True
print(abundante(18))  # True
print(abundante(20))  # True
# ------------------------------------------------------------------------
# 4. Implemente uma função media que receba n números inteiros positivos (n é variável, dependendo da quantidade de números que o
# utilizador pretenda inserir.


def media(*args):
    soma = 0
    for i in args:
        soma += i
    return soma / len(args)


valorMedio1 = media(10, 20, 30)
valorMedio2 = media(15, 25)
valorMedio3 = media(15, 35)

# printed with 2 decimal places
print("{:.2f}".format(valorMedio1))
print("{:.2f}".format(valorMedio2))
print("{:.2f}".format(valorMedio3))
