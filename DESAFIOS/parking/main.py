
matriculas = [
    "AZX-1234",
    "AZX-1235",
    "AZX-1236",
    "AZX-1237",
    "AZX-1238",
    "AZX-1239",
    "AZX-1240",
    "AZX-1241",
    "AZX-1242",
    "AZX-1243",
    "AZX-1244",
    "AZX-1245",
    "AZX-1246",
    "AZX-1247",
    "AZX-1248",
]

entradas =  []
saidas = []
lotacao = 0


def entrada():
    global lotacao
    # while loop para gerir as entradas
    while True:
        # maximo de lotacao do parque = 10
        if lotacao == 10:

            print("O parque está cheio")
            break

        # pedir matricula
        matricula = input("Insira a matricula: ")

        # verificar se a matricula existe na lista de matriculas
        if matricula in matriculas:
            # verificar se matricula é valida
            if matricula in matriculas:
                # se a matricula ja estiver no parque
                if matricula in entradas:
                    print("Matricula já está no parque")
                    break

                # se a matricula não estiver no parque
                else:
                    # adicionar matricula à lista de entradas
                    entradas.append(matricula)
                    # adicionar 1 à lotacao
                    lotacao += 1
                    print("Entrada registada")
                    break


            # se a matricula não for valida
            else:
                print("Matricula não é valida")
                break

        # se a matricula não existir na lista de matriculas
        else:
            print("Matricula não existe")
            break

    print("Lotacao: ", lotacao)

def saida():
    global lotacao
    # while loop para gerir as saidas
    while True:
        # pedir matricula
        matricula = input("Insira a matricula: ")

        # verificar se a matricula existe na lista de matriculas
        if matricula in matriculas:
            # verificar se matricula é valida
            if matricula in matriculas:
                # se a matricula ja estiver no parque
                if matricula in saidas:
                    print("Matricula já está fora do parque")
                    break

                # se a matricula não estiver no parque
                else:
                    # adicionar matricula à lista de saidas
                    saidas.append(matricula)
                    # remover 1 à lotacao
                    lotacao -= 1
                    print("Saida registada")
                    break


            # se a matricula não for valida
            else:
                print("Matricula não é valida")
                break

        # se a matricula não existir na lista de matriculas
        else:
            print("Matricula não existe")
            break

    print("Lotacao: ", lotacao)

def main():
    # while loop para gerir o programa
    while True:
        # pedir ao utilizador o que quer fazer
        escolha = input("Entrada ou saida? ")

        # se o utilizador escolher entrada
        if escolha == "entrada":
            entrada()

        # se o utilizador escolher saida
        elif escolha == "saida":
            saida()

        # se o utilizador escolher sair
        elif escolha == "sair":
            print("A sair do programa")
            break

        # se o utilizador escolher uma opcao invalida
        else:
            print("Escolha invalida")


main()