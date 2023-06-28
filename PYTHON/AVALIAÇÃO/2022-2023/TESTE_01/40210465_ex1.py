# Numero : 40210465  Nome: Pedro Teixeira

# função removeDuplicates
def removeDuplicates(texto):
    # variavel para guardar o texto sem duplicados
    textoSemDuplicados = ""
    # variavel para guardar o numero de palavras removidas
    palavrasRemovidas = 0
    # variavel para guardar as palavras que ja foram adicionadas
    palavrasAdicionadas = []
    # variavel para guardar as palavras do texto
    palavras = texto.split()
    # ciclo para percorrer as palavras
    for palavra in palavras:
        # se a palavra ainda nao foi adicionada
        if palavra not in palavrasAdicionadas:
            # adiciona a palavra ao texto sem duplicados
            textoSemDuplicados += palavra + " "
            # adiciona a palavra as palavras adicionadas
            palavrasAdicionadas.append(palavra)
        # se a palavra ja foi adicionada
        else:
            # incrementa o numero de palavras removidas
            palavrasRemovidas += 1
    # retorna o texto sem duplicados e o numero de palavras removidas
    return textoSemDuplicados, palavrasRemovidas


# input do texto
texto = input("Texto:")

print()
# chama a função removeDuplicates
textoSemDuplicados, palavrasRemovidas = removeDuplicates(texto)

# imprime o texto sem duplicados
print(f'Resultado pretendido: {textoSemDuplicados}')

# imprime o numero de palavras removidas
print(f'Foram removidas {palavrasRemovidas-1} palavras diferentes')


# while loop caso o utilizador queira testar mais textos com Press any key to continue . . .
while True:
    print()
    input("Press any key to continue . . .")
    print()
    # input do texto
    texto = input("Texto:")

    print()
    # chama a função removeDuplicates
    textoSemDuplicados, palavrasRemovidas = removeDuplicates(texto)

    # imprime o texto sem duplicados
    print(f'Resultado pretendido: {textoSemDuplicados}')

    # imprime o numero de palavras removidas
    print(f'Foram removidas {palavrasRemovidas-1} palavras diferentes')
