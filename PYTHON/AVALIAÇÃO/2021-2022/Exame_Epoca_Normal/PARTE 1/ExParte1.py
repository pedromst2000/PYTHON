# imprimir um texto por ordem inversa

texto = input("Digite um texto: ")

# eg: Este exercicío de AED é um exercício de exame
# resultado: exame do exercício um é AED de exercicío Este

def inverter(texto):
    lista = texto.split()
    lista.reverse()
    return " ".join(lista)

# contar palavra que surge mais vezes
# eg: Palavra que surge mais vezes : exercício
def conta_palavras(texto):
    # lista 
    lista = texto.split()
    # dicionario
    dicionario = {}
    # percorrer a lista
    for palavra in lista:
        # se a palavra não existe no dicionario
        if palavra not in dicionario:
            # adicionar a palavra ao dicionario
            dicionario[palavra] = 1
        else:
            # se a palavra existe no dicionario
            # incrementar o valor da chave
            dicionario[palavra] += 1
    # devolver a chave com o maior valor
    return max(dicionario, key=dicionario.get)
print()
print(f'Resultado: {inverter(texto)}')
print(f'Palavra que surge mais vezes: {conta_palavras(texto)}')