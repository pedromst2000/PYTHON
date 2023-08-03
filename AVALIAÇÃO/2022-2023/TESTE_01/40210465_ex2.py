# Numero : 40210465  Nome: Pedro Teixeira

print()
print("Exposição de Trabalhos de AED")
print()


try:
    visDom = int(input("Número de visitantes no Domingo: "))
    # verifica se é um número inteiro entre 0 e 100
    if visDom < 0 or visDom > 100:
        print("Número de visitantes inválido")
        exit()
    visSeg = int(input("Número de visitantes na Segunda-feira: "))
    # verifica se é um número inteiro entre 0 e 100
    if visSeg < 0 or visSeg > 100:
        print("Número de visitantes inválido")
        exit()
    visTer = int(input("Número de visitantes na Terça-feira: "))
    # verifica se é um número inteiro entre 0 e 100
    if visTer < 0 or visTer > 100:
        print("Número de visitantes inválido")
        exit()
    visQua = int(input("Número de visitantes na Quarta-feira: "))
    # verifica se é um número inteiro entre 0 e 100
    if visQua < 0 or visQua > 100:
        print("Número de visitantes inválido")
        exit()
    visQui = int(input("Número de visitantes na Quinta-feira: "))
    # verifica se é um número inteiro entre 0 e 100
    if visQui < 0 or visQui > 100:
        print("Número de visitantes inválido")
        exit()
    visSex = int(input("Número de visitantes na Sexta-feira: "))
    # verifica se é um número inteiro entre 0 e 100
    if visSex < 0 or visSex > 100:
        print("Número de visitantes inválido")
        exit()
    visSab = int(input("Número de visitantes no Sábado: "))
    # verifica se é um número inteiro entre 0 e 100
    if visSab < 0 or visSab > 100:
        print("Número de visitantes inválido")
        exit()

except ValueError:
    print("Número de visitantes inválido")
    exit()


# Em seguida, deve invocar uma função denominada diaSemana, que receba o nº de visitantes (ao longo da semana, de domingo a sábado) e devolva o dia da semana cujo nº de visitantes está mais distante do valor médio de visitas.

def diaSemana(visDom, visSeg, visTer, visQua, visQui, visSex, visSab):

    # calcula a média de visitantes
    media = (visDom + visSeg + visTer + visQua + visQui + visSex + visSab) / 7

    # calcula a diferença entre a média e o número de visitantes de cada dia
    difDom = abs(visDom - media)
    difSeg = abs(visSeg - media)
    difTer = abs(visTer - media)
    difQua = abs(visQua - media)
    difQui = abs(visQui - media)
    difSex = abs(visSex - media)
    difSab = abs(visSab - media)

    # verifica qual a diferença maior
    if difDom > difSeg and difDom > difTer and difDom > difQua and difDom > difQui and difDom > difSex and difDom > difSab:
        return "Domingo"
    elif difSeg > difDom and difSeg > difTer and difSeg > difQua and difSeg > difQui and difSeg > difSex and difSeg > difSab:
        return "Segunda"
    elif difTer > difDom and difTer > difSeg and difTer > difQua and difTer > difQui and difTer > difSex and difTer > difSab:
        return "Terça"
    elif difQua > difDom and difQua > difSeg and difQua > difTer and difQua > difQui and difQua > difSex and difQua > difSab:
        return "Quarta"
    elif difQui > difDom and difQui > difSeg and difQui > difTer and difQui > difQua and difQui > difSex and difQui > difSab:
        return "Quinta"
    elif difSex > difDom and difSex > difSeg and difSex > difTer and difSex > difQua and difSex > difQui and difSex > difSab:
        return "Sexta"
    elif difSab > difDom and difSab > difSeg and difSab > difTer and difSab > difQua and difSab > difQui and difSab > difSex:
        return "Sábado"

# Por fim, deve invocar a função diaSemana, passando-lhe como argumentos os nºs de visitantes de cada dia, e imprimir o dia da semana cujo nº de visitantes está mais distante do valor médio de visitas.
print()
print()
print()
print("Dia da semana mais distante da média de visitantes:", diaSemana(visDom, visSeg, visTer, visQua, visQui, visSex, visSab))

# Função Extra para ordenar o número de visitantes por ordem decrescente
def ordemVisitas(visDom, visSeg, visTer, visQua, visQui, visSex, visSab):
    
        # cria uma lista com os dias da semana
        diasSemana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
    
        # cria uma lista com os números de visitantes
        visitantes = [visDom, visSeg, visTer, visQua, visQui, visSex, visSab]
    
        # cria uma lista com os dias da semana e os respetivos números de visitantes - zip junta duas listas ou mais numa só
        # zip - concatena os elementos de duas ou mais listas numa só lista
        listaVisitas = list(zip(diasSemana, visitantes))
    
        # ordena a lista por ordem decrescente de visitantes
        listaVisitas.sort(key=lambda x: x[1], reverse=True)
    
        # imprime a lista
        for i in listaVisitas:
            print(i[0], ":", i[1])

# invoca a função ordemVisitas
print()
print()
print()
ordemVisitas(visDom, visSeg, visTer, visQua, visQui, visSex, visSab)
print()
print()