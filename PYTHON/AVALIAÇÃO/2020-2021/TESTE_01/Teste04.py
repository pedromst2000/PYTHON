# Programa que lê para cada posto de trabalho, a produção (nº de máscaras produzidas)
# e o tecido gasto (em cm)

# 6 postos de trabalho

# implementação das seguintes funções:

# Função que devolve os dois postos de trabalho que produziram maior número de máscaras
# Função que devolve qual o posto de trabalho que gastou mais tecido

print()
maskPosto1 = int(input("Máscaras produzidas no posto 1: "))
tecidoPosto1 = int(input("Tecido gasto no posto 1 (em cm): "))
print()
maskPosto2 = int(input("Máscaras produzidas no posto 2: "))
tecidoPosto2 = int(input("Tecido gasto no posto 2 (em cm): "))
print()
maskPosto3 = int(input("Máscaras produzidas no posto 3: "))
tecidoPosto3 = int(input("Tecido gasto no posto 3 (em cm): "))
print()
maskPosto4 = int(input("Máscaras produzidas no posto 4: "))
tecidoPosto4 = int(input("Tecido gasto no posto 4 (em cm): "))
print()
maskPosto5 = int(input("Máscaras produzidas no posto 5: "))
tecidoPosto5 = int(input("Tecido gasto no posto 5 (em cm): "))
print()
maskPosto6 = int(input("Máscaras produzidas no posto 6: "))
tecidoPosto6 = int(input("Tecido gasto no posto 6 (em cm): "))
print()


# função que calcula o posto que produziu mais máscaras e devolve os dois postos que produziram mais máscaras
def topMask(mascaraProduzidaPosto1, mascaraProduzidaPosto2, mascaraProduzidaPosto3, mascaraProduzidaPosto4, mascaraProduzidaPosto5, mascaraProduzidaPosto6):
    listaMascaras = [mascaraProduzidaPosto1, mascaraProduzidaPosto2,
                     mascaraProduzidaPosto3, mascaraProduzidaPosto4, mascaraProduzidaPosto5, mascaraProduzidaPosto6]

    # para devolver os dois postos que produziram mais mascaras e não a quantidade de máscaras produzidas
    indicesOrdenados = sorted(
        range(len(listaMascaras)), key=lambda i: listaMascaras[i], reverse=True)
    return indicesOrdenados[0], indicesOrdenados[1]



def maiorGasto(tecidoPosto1, tecidoPosto2, tecidoPosto3, tecidoPosto4, tecidoPosto5, tecidoPosto6):
    # devolve qual o posto de trabalho que gastou mais tecido
    lista = [tecidoPosto1, tecidoPosto2, tecidoPosto3, tecidoPosto4, tecidoPosto5, tecidoPosto6]
    # para devolver o posto que gastou mais tecido e não a quantidade de tecido gasto
    indicesOrdenados = sorted(range(len(lista)), key=lambda i: lista[i], reverse=True)
    return indicesOrdenados[0]


topMask = topMask(maskPosto1, maskPosto2, maskPosto3, maskPosto4, maskPosto5, maskPosto6)

print("Os dois postos que produziram mais máscaras foram o posto", topMask[0]+1, "e o posto", topMask[1]+1)

maiorGasto = maiorGasto(tecidoPosto1, tecidoPosto2, tecidoPosto3, tecidoPosto4, tecidoPosto5, tecidoPosto6)

print("O posto que gastou mais tecido foi o posto", maiorGasto+1)