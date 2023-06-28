gessList = ['00-CC-00','01-CC-01','02-CC-02','03-CC-03','04-CC-04', '05-CC-05','06-CC-06','07-CC-07','08-CC-08','09-CC-09']
parkList = []

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

def parkManager(matricula, movimento):
    if movimento == 'E':
        parkList.append(matricula)
    elif movimento == 'S':
        parkList.remove(matricula)

counter = 0
while True:

    matricula = input("Insira a matrícula: ")
    
    if matricula == '00-00-00':
        break

    movimento = input("Insira o movimento (E - entrada, S - saída): ")

    if parkValidator(matricula, movimento):
        parkManager(matricula, movimento)
        if movimento == 'E':
            counter += 1
    else:
        print("Movimento inválido.")

print("Número de carros que entraram no parque de estacionamento: ", counter)
