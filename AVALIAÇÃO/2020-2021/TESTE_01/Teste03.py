# programa que leia um texto e o nº de caracteres que se pretende imprimir por cada linha.
# O progama invoca uma função que recebe o texto e o nº de caracteres a imprimir por linha e devolve o texto em função desse valor.

texto = input("Texto: ")
caracteres = int(input("Nº de caracteres por linha: "))

def imprimir(texto, caracteres):
    for i in range(0, len(texto), caracteres):
        print(texto[i:i+caracteres])


imprimir(texto, caracteres)