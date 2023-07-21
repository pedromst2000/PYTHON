import random

# duas listas
lista1 = []
lista2 = []

# gera aleatoriamente 10 numeros para cada lista
for i in range(10):
    lista1.append(random.randint(1, 100))
    lista2.append(random.randint(1, 100))

# imprime as listas


def imprimir_listas(lista1, lista2):
    for i in range(len(lista1)):
        # se for o ultimo elemento da lista, imprime o elemento e pula uma linha
        if i == len(lista1) - 1:
            print(lista1[i])
        else:
            # se não for o ultimo elemento da lista, imprime o elemento e uma virgula
            print(lista1[i], end=', ')
    for i in range(len(lista2)):
        if i == len(lista2) - 1:
            print(lista2[i])
        else:
            print(lista2[i], end=', ')


# verifica se existem elementos repetidos nas listas
def verifica_repeticao(lista1, lista2):
    # lista auxiliar para armazenar os elementos que se repetem
    aux = []
    # contar os elementos que se repetem
    count = 0
    # percorrer as duas listas
    for i in range(len(lista1)):
        # percorrer a lista 2
        for j in range(len(lista2)):
          # se o elemento da lista 1 for igual ao elemento da lista 2, incrementa o contador e adiciona o elemento na lista auxiliar
            if lista1[i] == lista2[j]:
                count += 1
                # se o elemento não estiver na lista auxiliar, adiciona
                aux.append(lista1[i])
    # se o contador for igual a 0, não existem elementos repetidos
    if count == 0:
        print("Não existem elementos repetidos")
    # caso contrario, imprime a quantidade de elementos repetidos e os elementos que se repetem
    else:
        print("Existem", count,
              "elementos da lista 1 que se repetem na lista :", end=' ')
        # percorre a lista auxiliar e imprime os elementos
        for i in range(len(aux)):
            # se for o ultimo elemento da lista, imprime o elemento e pula uma linha
            if i == len(aux) - 1:
                print(aux[i])
            else:
                print(aux[i], end=', ')


imprimir_listas(lista1, lista2)
print()
verifica_repeticao(lista1, lista2)
print()
