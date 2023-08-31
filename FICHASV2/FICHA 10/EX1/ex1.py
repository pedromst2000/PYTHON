import os

texto = input("Digite um texto: ")


def escreveTexto(texto):
  # criar o ficheiro na pasta files com o nome dados.bin se não existir
    if not os.path.exists("ficheiros"):
        os.mkdir("ficheiros")
    if not os.path.exists("ficheiros/dados.bin"):
        f = open("ficheiros/dados.bin", "w")
        f.close()
    elif os.path.exists("ficheiros/dados.bin"):
        # substituir o conteudo do ficheiro
        f = open("ficheiros/dados.bin", "w")
        f.write(texto)
        f.close()

    lerTexto()

def lerTexto():
    # ler o ficheiro
    f = open("ficheiros/dados.bin", "r")
    print(f.read())
    f.close()


escreveTexto(texto)