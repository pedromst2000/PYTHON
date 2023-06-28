# 1. Escreva um programa que leia 10 números e no final indique o maior e a
# média.

sum = 0

for i in range(10):
    number = int(input("Indique um número: "))
    sum += number
    if i == 9:
        print("A média é", sum / (i + 1))
    elif i == 0:
        biggest = number
    else:
        if number > biggest:
            biggest = number
print("O maior é", biggest)

# -----------------------------------------------------------------------------
# 2. Adapte o programa anterior, de forma a que o utilizador
#  indique previamente quantos números pretende ler (em vez de serem sempre 10 números).

sum = 0

n = int(input("Quantos números deseja ler?: "))

for i in range(n):
    number = int(input("Indique um número: "))
    sum += number
    if i == n - 1:
        print("A média é", sum / (i + 1))
    elif i == 0:
        biggest = number
    else:
        if number > biggest:
            biggest = number
print("O maior é", biggest)

# -----------------------------------------------------------------------------
# 3. Elabore um programa que simule a função fatorial, isto é, que determine
# o fatorial de um determinado número.

print("Calcular o fatorial de um número")
n = int(input("Indique um número: "))
factorial = 1

for i in range(n, 0, -1):
    factorial *= i
    if i == 0:
        factorial = 1

print("Fatorial de", n, "é", factorial)
# -----------------------------------------------------------------------------
# 3.2 Fatorial com output => 5! = 5 * 4 * 3 * 2 * 1 = 120

print("Calcular o fatorial de um número")
n = int(input("Indique um número: "))

c = n
f = 1
print("Fatorial de", n, "=", end=" ")

while c > 0:
    print(c, end="")
    if c > 1:
        print(" * ", end="")
    f *= c
    c -= 1
print(" = ", f)

# -----------------------------------------------------------------------------
# 5. jogo Adivinha o número !

import random
import os

number = random.randint(1, 50)

print("Adivinha o número entre 1 e 50")

attempts = 1
op = ""

while True:
    guess = int(input("Indique o seu palpite: "))

    if attempts == 10:
        print("Esgotou as 10 tentativas! O número era {0}" .format(number))
        op = input("Novo jogo? (S/N): ")
        if op == "S" or op == "s":
            os.system('cls')
            attempts = 1
            number = random.randint(1, 50)
            continue
        else:
            os.system('cls')
            break

    elif guess == number:
        print("Parabéns! Acertou em {0} tentativas" .format(attempts))
        op = input("Novo jogo? (S/N): ")
        if op == "S" or op == "s":
            os.system('cls')
            attempts = 1
            number = random.randint(1, 50)
            continue
        else:
            os.system('cls')
            break

    elif guess > number:
        print("O número a adivinhar é MENOR")
        attempts += 1
        print(attempts)

    elif guess < number:
        print("O número a adivinhar é MAIOR")
        attempts += 1
        print(attempts)

# -----------------------------------------------------------------------------
# 6. Elabore um programa que permita gerar um número aleatório entre 1900 e
# 2020, número esse que representa um ano. Considerando o ano gerado aleatoriamente, pretende-se que o programa indique se o ano é bissexto ou
# não.

import os

print("Ano bissexto ou não? Insira um ano e descubra!")
op = ""

while True :
    year = int(input("Indique um ano: "))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("O ano", year, "é bissexto")
        op = input("Novo ano? (S/N): ")
        if op == "S" or op == "s":
            continue
        else:
            break
    else:
        print("O ano", year, "não é bissexto")
        op = input("Novo ano? (S/N): ")
        if op == "S" or op == "s":
            continue
        else:
            break

# -----------------------------------------------------------------------------
# 7. Elabore um programa que leia um número e indique se ele é primo ou não.

import os

print("Número primo ou não? Insira um número e descubra!")
op = ""

while True:
    number = int(input("Indique um número: "))
    if number == 1:
        print("O número", number, "não é primo")
        op = input("Novo número? (S/N): ")
        if op == "S" or op == "s":
            continue
        elif op == "N" or op == "n":
            break

    elif number == 2:
        print("O número", number, "é primo")
        op = input("Novo número? (S/N): ")
        if op == "S" or op == "s":
            continue
        elif op == "N" or op == "n":
            break

    else:
        for i in range(2, number):
            if number % i == 0:
                print("O número", number, "não é primo")
                op = input("Novo número? (S/N): ")
                if op == "S" or op == "s":
                    continue
                elif op == "N" or op == "n":
                    break

            else:
                print("O número", number, "é primo")
                op = input("Novo número? (S/N): ")
                if op == "S" or op == "s":
                    continue
                elif op == "N" or op == "n":
                    break

# -----------------------------------------------------------------------------
# # 8. Elabore um programa que ilustre os primeiros n termos da sequência de
# Fibonacci, sendo que o número de termos desejados(n) deve ser indicado
# pelo utilizador.
# output : primeiro 10 termos da sequência de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

print("Sequência de Fibonacci")

n = int(input("Indique o número de termos: "))
a = 0
b = 1
c = 0

print("Os primeiros", n, "termos da sequência de Fibonacci: ", end="")

for i in range(0, n):

    if i == n - 1:
        print(a, end="")
    else:
        print(a, end=", ")
    c = a + b
    a = b
    b = c

# -----------------------------------------------------------------------------
# 9. Escreva um programa que verifique se um determinado número é perfeito.
# Em Matemática, um número perfeito é um número inteiro para o qual a soma
# de todos os seus divisores positivos próprios é igual ao próprio número.
# Por exemplo, o número 6 é um número perfeito, pois:
# 6 é divisível por: 1, 2 e 3 1+2+3 = 6, logo é um número perfeito

print("Número perfeito ou não? Insira um número e descubra!")

number = int(input("Indique um número: "))

soma = 0

# check if the number is perfect or not
for i in range(1, number):
    if number % i == 0:
        soma += i

if soma == number:
    print("O número", number, "é perfeito")
else:
    print("O número", number, "não é perfeito")

# -----------------------------------------------------------------------------
# 10. Implemente um programa que leia um número (entre 1 e 99) e determine
# a sua representação em linguagem binária.
# Exemplo:
# Número: 12 Resultado: 1 1 0 0
# Número: 29 Resultado: 1 1 1 0 1

print("Número em binário")

number = int(input("Indique um número: "))

binary = []

while number > 0:
    binary.append(number % 2)
    # rest division
    number = number // 2
    
binary.reverse()

print("Resultado: ", end="")
for i in binary:
    print(i, end=" ")
print()

# -----------------------------------------------------------------------------
# 11. Dado uma conjunto de n números (n indicado pelo utilizador) inteiros
# e positivos, determine o segundo maior valor de entre o conjunto de números lido.


print("Segundo maior valor")

n = int(input("Indique o número de elementos: "))

lista = []

for i in range(0, n):

    number = int(input("Indique um número: "))
    lista.append(number)

lista.sort()

# -2 to acess the second highest value since with -1 with would acess the last element of the list
print("O segundo maior valor é", lista[-2])
# -----------------------------------------------------------------------------