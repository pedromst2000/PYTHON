# implementar um programa que lê o número de visitantes numa exposição,
# que decorre de Domingo a Sábado

# Passos de resolução:

# => try except para verificar se o input é um número inteiro e positivo

# => implementar uma função que ordena uma lista de número de visitantes diários por ordem decrescente

# => implementar uma função que calcula a média de visitantes diários

# => implementa uma função que determine o dia mais próximo do valor médio


# input :
#                             ordenar lista de visitantes diários por ordem decrescente
# Domingo: 100                sexta   140
# Segunda: 80                 sábado  135
# Terça: 120                  terça   120
# Quarta: 110                 quarta  110
# Quinta: 70                  domingo 100
# Sexta: 140                  segunda 80
# Sábado: 135                 quinta  70


visDomingo = 0
visSegunda = 0
visTerca = 0
visQuarta = 0
visQuinta = 0
visSexta = 0
visSabado = 0


try:
    visDomingo = int(input("Domingo:"))
#   check if is number and positive
    if visDomingo < 0 or type(visDomingo) != int:
        raise ValueError
    visSegunda = int(input("Segunda:"))
    if visSegunda < 0 or type(visSegunda) != int:
        raise ValueError
    visTerca = int(input("Terça:"))
    if visTerca < 0 or type(visTerca) != int:
        raise ValueError
    visQuarta = int(input("Quarta:"))
    if visQuarta < 0 or type(visQuarta) != int:
        raise ValueError
    visQuinta = int(input("Quinta:"))
    if visQuinta < 0 or type(visQuinta) != int:
        raise ValueError
    visSexta = int(input("Sexta:"))
    if visSexta < 0 or type(visSexta) != int:
        raise ValueError
    visSabado = int(input("Sábado:"))
    if visSabado < 0 or type(visSabado) != int:
        raise ValueError
except ValueError:
    print("Input inválido")
    exit()

# ordenar lista de visitantes diários por ordem decrescente
listaVis = [visDomingo, visSegunda, visTerca,
            visQuarta, visQuinta, visSexta, visSabado]


listaDias = ["Domingo", "Segunda", "Terça",
             "Quarta", "Quinta", "Sexta", "Sábado"]



# calcular a média de visitantes diários
def mediaVis(listaVis):
    soma = 0
    for i in range(len(listaVis)):
        soma += listaVis[i]
    media = soma / len(listaVis)
    return media


# ordenar lista de visitantes diários por ordem decrescente
def ordenarLista(listaVis):
    # primeiro associar o valor da listaVis ao dia correspondente da listaDias
    listaVisDias = []
    for i in range(len(listaVis)):
        listaVisDias.append([listaVis[i], listaDias[i]])
    # ordenar a listaVisDias por ordem decrescente
    listaVisDias.sort(reverse=True)
    # imprimir o dia e valor de visitantes eg: "Sexta   140"
    for i in range(len(listaVisDias)):
        print(f'{listaVisDias[i][1]}   {listaVisDias[i][0]}')
    return listaVisDias

# determinar o dia mais próximo da média de visitantes diários
def diaMaisProximo(listaVis):
    # encontra o dia mais próximo da média de visitantes diários
    media = mediaVis(listaVis)
    # primeiro associar o valor da listaVis ao dia correspondente da listaDias
    listaVisDias = []
    for i in range(len(listaVis)):
        listaVisDias.append([listaVis[i], listaDias[i]])
    # ordenar a listaVisDias por ordem decrescente
    listaVisDias.sort(reverse=True)
    # determinar o dia mais próximo da média de visitantes diários
    diaMaisProximo = listaVisDias[0][1]
    for i in range(len(listaVisDias)):
        if listaVisDias[i][0] < media and listaVisDias[i][0] > listaVisDias[i+1][0]:
            diaMaisProximo = listaVisDias[i][1]
            break
    return diaMaisProximo

print()
# imprimir a lista de visitantes diários por ordem decrescente no lado direito do input dos dias
ordenarLista(listaVis)
print()
print()
print()
# imprimir a média de visitantes diários duas casas decimais
print(f'Dia mais próximo do valor médio: {diaMaisProximo(listaVis)}')
print(f'Média de visitantes diários: {mediaVis(listaVis):.2f}')
print()
print()