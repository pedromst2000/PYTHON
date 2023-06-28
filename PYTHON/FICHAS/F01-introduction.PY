# Elabore um programa que dada uma medida em polegadas, converta o resultado
# para mm e cm.
# Nota: 1 polegada = 25.4 mm

# polegadas = int(input("Indique um valor em polegadas: "))

# mm = polegadas * 25.4
# cm = mm / 10

# print("O valor em mm é: ", mm)

# # ---------------------------------------------------------------------------
# # 2) Escreva um programa que leia uma temperatura em º Celsius e imprima o equivalente em º Fahrenheit

# celsius = int(input("Indique uma temperatura em ºC: "))

# # converter para fahrenheit
# fahrenheit = (celsius * 9/5) + 32

# print("A temperatura em Fahnrenheit é: ", fahrenheit)

# # ---------------------------------------------------------------------------
# # 3) Escreva um pequeno programa que calcule o seu peso ideal!
# # Existem inúmeras fórmulas para determinar o peso ideal de uma pessoa, dependendo do género, altura, idade, estrutura óssea, etc.
# # Neste exercício vamos usar(para já) uma fórmula de cálculo simplificada,
# # baseado na fórmula:
# # Peso ideal = (altura-100) * 0.9

# altura = int(input("Indique a sua altura: "))

# peso_ideal = (altura - 100) * 0.9

# print("O seu peso ideal é: ", peso_ideal)

# # ---------------------------------------------------------------------------
# # 4) O índice de massa corporal (IMC) de um indivíduo é obtido dividindo-se o seu
# # peso (em Kg) pela sua altura (em m) ao quadrado.
# # Assim, por exemplo, uma pessoa de 1,67m e pesando 55kg tem IMC igual a 19,72.
# # Escreva um programa que solicite ao utilizador a
# # indicação do seu peso em kg e da sua altura em
# # metros, e calcule o respetivo índice de massa corporal(IMC).

# peso = int(input("Indique o seu peso em Kg: "))
# altura = float(input("Indique a sua altura em metros: "))

# # calcular o IMC
# imc = peso / (altura * altura)

# # output IMC
# print("O seu IMC é: ", round(imc, 2))

# ---------------------------------------------------------------------------
# 5) Escreva um programa que a partir de um determinado número de segundos calcula
# o número de horas, minutos e segundos correspondentes. Conforme o seguinte
# exemplo:
# input => 8054 segundos
# output => 2 horas, 14 minutos e 14 segundos

import os

# segundos = int(input("Indique o tempo em segundos: "))

# # calcular horas
# horas = segundos // 3600

# # calcular minutos
# minutos = (segundos % 3600) // 60

# # calcular segundos
# segundos = (segundos % 3600) % 60

# print(horas, "horas,", minutos, "minutos,", segundos, "segundos")

while True:
    segundos = int(input("Indique o tempo em segundos: "))
    # calcular horas
    horas = segundos // 3600

    # calcular minutos
    minutos = (segundos % 3600) // 60

    # calcular segundos
    segundos = (segundos % 3600) % 60

    print(horas, "horas,", minutos, "minutos,", segundos, "segundos")

    op = input("Deseja outro cálculo? (S/N): ")
    if op == "S" or op == "s":
        continue
    elif op == "N" or op == "n":
        break
