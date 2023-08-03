# Numero : 40210465 Nome : Pedro Teixeira

#  Função topMask que receba a lista de produção de máscaras dos 6 postos, e devolva os dois postos de
# trabalho que produziram maior número de máscaras

#  Função moreMaterial que receba as listas de produção e de tecido gasto, e devolva qual o posto de trabalho
# que gastou mais tecido por máscara produzida

# input :
# Nº de máscaras produzidas no posto 1: 10
# Tecido gasto no posto (em cm) 1: 100

# Nº de máscaras produzidas no posto 2: 15
# Tecido gasto no posto (em cm) 2: 150

# Nº de máscaras produzidas no posto 3: 10
# Tecido gasto no posto (em cm) 3: 120

# Nº de máscaras produzidas no posto 4: 8
# Tecido gasto no posto (em cm) 4: 75

# Nº de máscaras produzidas no posto 5: 10
# Tecido gasto no posto (em cm) 5: 90

# Nº de máscaras produzidas no posto 6: 12
# Tecido gasto no posto (em cm) 6: 110

# output :
# os postos que produziram mais máscaras foram os 2 e 6
# o posto que gastou mais tecido por máscara foi: 3
# try except para verificar se o input é um numero inteiro e está entre 0 e 15
print()
# validações para o input das máscaras produzidas e do tecido gasto
try:
    print()
    mascaraProduzidaPosto1 = int(
        input("Nº de máscaras produzidas no posto 1: "))
    tecidoGastoPosto1 = int(input("Tecido gasto no posto (em cm) 1: "))
    print()
    if mascaraProduzidaPosto1 < 0 or mascaraProduzidaPosto1 > 15:
        print("O número de máscaras produzidas no posto 1 tem de ser entre 0 e 15")
        exit()
    print()
    mascaraProduzidaPosto2 = int(
        input("Nº de máscaras produzidas no posto 2: "))
    tecidoGastoPosto2 = int(input("Tecido gasto no posto (em cm) 2: "))    
    print()
    if mascaraProduzidaPosto2 < 0 or mascaraProduzidaPosto2 > 15:
        print("O número de máscaras produzidas no posto 2 tem de ser entre 0 e 15")
        exit()
    print()
    mascaraProduzidaPosto3 = int(
        input("Nº de máscaras produzidas no posto 3: "))
    tecidoGastoPosto3 = int(input("Tecido gasto no posto (em cm) 3: "))
    print()
    if mascaraProduzidaPosto3 < 0 or mascaraProduzidaPosto3 > 15:
        print("O número de máscaras produzidas no posto 3 tem de ser entre 0 e 15")
        exit()
    print()
    mascaraProduzidaPosto4 = int(
        input("Nº de máscaras produzidas no posto 4: "))
    tecidoGastoPosto4 = int(input("Tecido gasto no posto (em cm) 4: "))
    print()
    if mascaraProduzidaPosto4 < 0 or mascaraProduzidaPosto4 > 15:
        print("O número de máscaras produzidas no posto 4 tem de ser entre 0 e 15")
        exit()
    print()    
    mascaraProduzidaPosto5 = int(
        input("Nº de máscaras produzidas no posto 5: "))
    tecidoGastoPosto5 = int(input("Tecido gasto no posto (em cm) 5: "))
    print()
    if mascaraProduzidaPosto5 < 0 or mascaraProduzidaPosto5 > 15:
        print("O número de máscaras produzidas no posto 5 tem de ser entre 0 e 15")
        exit()
    print() 
    mascaraProduzidaPosto6 = int(
        input("Nº de máscaras produzidas no posto 6: "))
    tecidoGastoPosto6 = int(input("Tecido gasto no posto (em cm) 6: "))
    print()
    print()
    print()
    if mascaraProduzidaPosto6 < 0 or mascaraProduzidaPosto6 > 15:
        print("O número de máscaras produzidas no posto 6 tem de ser entre 0 e 15")
        exit()
except ValueError:
    print("O número de máscaras produzidas tem de ser um número inteiro")
    exit()


# função que calcula o posto que produziu mais máscaras e devolve os dois postos que produziram mais máscaras
def topMask(mascaraProduzidaPosto1, mascaraProduzidaPosto2, mascaraProduzidaPosto3, mascaraProduzidaPosto4, mascaraProduzidaPosto5, mascaraProduzidaPosto6):
    listaMascaras = [mascaraProduzidaPosto1, mascaraProduzidaPosto2,
                     mascaraProduzidaPosto3, mascaraProduzidaPosto4, mascaraProduzidaPosto5, mascaraProduzidaPosto6]
    
    # para devolver os dois postos que produziram mais mascaras e não a quantidade de máscaras produzidas
    indicesOrdenados = sorted(
        range(len(listaMascaras)), key=lambda i: listaMascaras[i], reverse=True)
    return indicesOrdenados[0], indicesOrdenados[1]


# função que calcula o posto que gastou mais tecido por máscara e devolve o posto que gastou mais tecido por máscara
def moreMaterial(mascaraProduzidaPosto1, mascaraProduzidaPosto2, mascaraProduzidaPosto3, mascaraProduzidaPosto4, mascaraProduzidaPosto5, mascaraProduzidaPosto6, tecidoGastoPosto1, tecidoGastoPosto2, tecidoGastoPosto3, tecidoGastoPosto4, tecidoGastoPosto5, tecidoGastoPosto6):
    listaMascaras = [mascaraProduzidaPosto1, mascaraProduzidaPosto2,
                     mascaraProduzidaPosto3, mascaraProduzidaPosto4, mascaraProduzidaPosto5, mascaraProduzidaPosto6]
    listaTecido = [tecidoGastoPosto1, tecidoGastoPosto2,
                   tecidoGastoPosto3, tecidoGastoPosto4, tecidoGastoPosto5, tecidoGastoPosto6]
    listaTecidoPorMascara = [tecido / mascara for tecido,
                             mascara in zip(listaTecido, listaMascaras)]
    
    # para devolver o posto que gastou mais tecido por máscara e não a quantidade de tecido gasto por máscara
    indicePostoMaisTecido = max(
        range(len(listaTecidoPorMascara)), key=lambda i: listaTecidoPorMascara[i])
    return indicePostoMaisTecido



topMask = topMask(mascaraProduzidaPosto1, mascaraProduzidaPosto2, mascaraProduzidaPosto3,
                    mascaraProduzidaPosto4, mascaraProduzidaPosto5, mascaraProduzidaPosto6)


print("os postos que produziram mais máscaras foram os", topMask[0] + 1, "e", topMask[1] + 1)
print()

indicePostoMaisTecido = moreMaterial(mascaraProduzidaPosto1, mascaraProduzidaPosto2, mascaraProduzidaPosto3,
                    mascaraProduzidaPosto4, mascaraProduzidaPosto5, mascaraProduzidaPosto6, tecidoGastoPosto1, tecidoGastoPosto2, tecidoGastoPosto3,
                    tecidoGastoPosto4, tecidoGastoPosto5, tecidoGastoPosto6)

print("o posto que gastou mais tecido por máscara foi:", indicePostoMaisTecido + 1)
print()
print()