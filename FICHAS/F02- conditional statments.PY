# 1. Escreva um programa que determine se um dado número é par ou ímpar.

number = int(input("Insira um número: "))

if number % 2 == 0:
    print("o número", number, "é par")
else:
    print("o número", number, "é ímpar")

# ----------------------------------------------------------------------
# 2. Escreva um programa que permita classificar um triângulo lendo as medidas
# dos 3 lados
# (equilátero: todos iguais
#  isósceles: dois iguais
#  escaleno: todos diferentes)

lado1 = int(input("primeiro lado : "))
lado2 = int(input("segundo lado : "))
lado3 = int(input("terceiro lado : "))

if lado1 == lado2 == lado3:
    print("Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Isósceles")
else:
    print("Escaleno")

# ----------------------------------------------------------------------
# 3. Escreva um programa que implemente um simulador do peso ideal (meramente
# indicativo!). O algoritmo deve pedir ao utilizador o género(M para
# masculino e F para feminino) e a altura(em cm).

# formula
# Peso ideal = (h-100) - (h-150)/k
# k = 2 para género feminino
# k = 4 para género masculino
# h = altura em cm

genrer = input("INSIRA O GÉNERO (M/F): ")
height = int(input("INSIRA A ALTURA EM CM: "))

if genrer == "M" or genrer == "m":
    ideal_weight = (height - 100) - (height - 150) / 4
    print("O peso ideal é", ideal_weight, "kg")
elif genrer == "F" or genrer == "f":
    ideal_weight = (height - 100) - (height - 150) / 2
    print("O peso ideal é", ideal_weight, "kg")
elif not (genrer == "M" or genrer == "m") and not (genrer == "F" or genrer == "f"):
    print("Género inválido")

# -------------------------------------------------------------------------------
# 4. O índice de massa corporal (IMC) de um indivíduo é obtido dividindo-se
# o seu peso(em Kg) pela sua altura(em m) ao quadrado.
# Assim, por exemplo, uma pessoa de 1, 67m e pesando 55kg tem IMC igual a
# 19, 72.

weight = float(input("Insira o seu peso em Kg: "))
height = float(input("Insira a sua altura em m: "))

# # imc formula
imc = weight / pow(height, 2)

if imc < 18.5:
    print("IMC=", format(imc, '.2f'))
    print("Abaixo do peso")
elif imc >= 18.6 and imc <= 24.9:
    print("IMC=", format(imc, '.2f'))
    print("Saudável")
elif imc >= 25 and imc <= 29.9:
    print("IMC=", format(imc, '.2f'))
    print("Sobrepeso")
elif imc >= 30 and imc <= 34.9:
    print("IMC=", format(imc, '.2f'))
    print("Obesidade grau 1")
elif imc >= 35 and imc <= 39.9:
    print("IMC=", format(imc, '.2f'))
    print("Obesidade grau 2")
elif imc >= 40:
    print("IMC=", format(imc, '.2f'))
    print("Obesidade grau 3")

# -------------------------------------------------------------------------------
# 5. Escreva um programa que leia 3 números e os imprima por ordem crescente.

# with complex solution
numbers = []

firstNumber = int(input("Insira o primeiro número: "))
numbers.append(firstNumber)
secondNumber = int(input("Insira o segundo número: "))
numbers.append(secondNumber)
thirdNumber = int(input("Insira o terceiro número: "))
numbers.append(thirdNumber)

numbers.sort()

print(" ".join(str(number) for number in numbers))

# -------------------------------------------------------------------------------
# 6. Implemente um programa que funcione como um pequeno simulador de esforço
# cardíaco, quando um atleta desenvolve atividade física.
# O esforço cardíaco de um atleta desenvolve depende da sua frequência
# cardíaca máxima(FCM), que se
# calcula da seguinte forma(depende da idade e do género):
# • Nas mulheres, 226 – idade.
# • Nos homens, 220 – idade.

genrer = input("Insira o género (M/F): ")
age = int(input("Insira a sua idade: "))

if genrer == "M" or genrer == "m":
    max_heart_rate = 220 - age
    print("FCM=", max_heart_rate, "bpm")
elif genrer == "F" or genrer == "f":
    max_heart_rate = 226 - age
    print("FCM=", max_heart_rate, "bpm")

# -------------------------------------------------------------------------------
# 7. Implemente um simulador do seu peso noutro Planeta. O programa deverá
# ler o seu peso na Terra, assim como o código identificador de planeta, e
# calcular o peso respetivo nesse planeta, de acordo com a seguinte tabela:

# Código Planeta Planeta Gravidade relativa
# 1 Mercúrio 0, 37
# 2 Vénus 0, 88
# 3 Marte 0, 38
# 4 Júpiter 2, 64
# 5 Saturno 1, 15
# 6 Urano 1, 17

# formula de calculo
# peso_planeta = peso_terra * gravidade_planeta

weight = float(input("Insira o seu peso na Terra em KG:"))
planet_code = int(input("Insira o código do planeta: "))
weight_planet = 0

if planet_code == 1:
    weight_planet = weight * 0.37
    print("O seu peso no planeta Mercúrio é", weight_planet, "kg")
elif planet_code == 2:
    weight_planet = weight * 0.88
    print("O seu peso no planeta Vénus é", weight_planet, "kg")
elif planet_code == 3:
    weight_planet = weight * 0.38
    print("O seu peso no planeta Marte é", weight_planet, "kg")
elif planet_code == 4:
    weight_planet = weight * 2.64
    print("O seu peso no planeta Júpiter é", weight_planet, "kg")
elif planet_code == 5:
    weight_planet = weight * 1.15
    print("O seu peso no planeta Saturno é", weight_planet, "kg")
elif planet_code == 6:
    weight_planet = weight * 1.17
    print("O seu peso no planeta Urano é", weight_planet, "kg")
else:
    print("Código inválido ou planeta inexistente !!")
