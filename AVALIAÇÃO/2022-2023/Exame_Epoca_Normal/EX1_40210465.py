# Numero : 40210465
# Nome : Pedro Miguel Silva Teixeira

# programa que permite gerir os acessos ao parte de estacionamento da ESMAD

# lista de matriculas autorizadas a entrar no parque
gessList = ['00-CC-00','01-CC-01','02-CC-02','03-CC-03','04-CC-04', '05-CC-05','06-CC-06','07-CC-07','08-CC-08','09-CC-09']

# lista para gerir a ocupação do parque
parkList = []

movimento = ''

# função que valida se o movimento é válido (True) ou não (False)
def parkValidator(matricula, movimento):
    if movimento == 'E':
        if matricula in gessList and matricula not in parkList:
            return True
        else:
            return False
    elif movimento == 'S':
        if matricula in parkList:
            return True
        else:
            return False
    else:
        return False
    
# função que gere a entrada ou saída do veiculo
def parkManager(matricula, movimento):
    if movimento == 'E':
        parkList.append(matricula)
    elif movimento == 'S':
        parkList.remove(matricula)
    else:
        return False


# valida o tipo de movimento com tratamento de exceções
while movimento != '00-00-00':
    try:
        matricula = input('Introduza a matricula: ')
        movimento = input('Introduza o movimento: ')
        if movimento == 'E' or movimento == 'S':
            if parkValidator(matricula, movimento) == True:
                parkManager(matricula, movimento)
                print('Movimento realizado com sucesso')
                op = input('Deseja continuar? (S/N): ')
                if op == 'N':
                    # apresentar quantos carros entraram no parque
                    print('Entraram', len(parkList), 'carros no parque')
                    break
                if op == 'S':
                    continue
            else:
                print('Movimento não é possível')
        else:
            print('Movimento não é possível')
    except:
        print('Movimento não é possível')