# implementar um pequeno simulador do esforço cardíaco, no desenvolvimento do exercício físico.
# da atividade física

# O esforço cardíaco de um atleta depende da sua frequencia cardíaca
# máxima (FCM), que se calcula da seguinte forma (depende da idade e do género):
# = nas mulheres, 226-idade
# = nos homens, 220-idade

# Por exemplo, num indíviduo do género masculino de 35 anos, a FCM = 220-35 = 185 bpm

# O simulador deve pedir ao utilizador:
# = O género (M ou F) - deve aceitar a introdução de minúsculas e maiúsculas
# = A idade
# = A frequência cardíaca atual (FCA)

# Deve calcular e apresentar:
# = A frequência cardíaca máxima (FCM), de acordo com a forma indicada acima
# = A classificação da atividade física, em função da frequência cardíaca atual (FCA) e da frequência cardíaca indicada, e que se 
# obtém da seguinte forma:

# = Atividade moderada : 50% a 60% da FCM
# = Atividade intensa : 61% a 70% da FCM
# = Nível aeróbico : 71% a 80% da FCM
# = Nível anaeróbico : 81% a 90% da FCM
# = Red zone : 91% a 100% da FCM

# No final de cada execução, o programa deve perguntar ao utilizador se pretende continuar a utilizar o simulador.
# "Deseja continuar? (S/N)", agindo em conformidade com a resposta dada.

genero = input("Qual o seu género? (M/F) ")
idade = int(input("Qual a sua idade? "))

if genero == "M" or genero == "m":
    fcm = 220 - idade
elif genero == "F" or genero == "f":
    fcm = 226 - idade
else:
    print("Género inválido!")


fca = int(input("Qual a sua frequência cardíaca atual? "))
if fca >= 0.5 * fcm and fca <= 0.6 * fcm:
    print("Atividade moderada")
elif fca >= 0.61 * fcm and fca <= 0.7 * fcm:
    print("Atividade intensa")
elif fca >= 0.71 * fcm and fca <= 0.8 * fcm:
    print("Nível aeróbico")
elif fca >= 0.81 * fcm and fca <= 0.9 * fcm:
    print("Nível anaeróbico")
elif fca >= 0.91 * fcm and fca <= 1 * fcm:
    print("Red zone")
else:
    print("Frequência cardíaca atual inválida!")


continuar = input("Deseja continuar? (S/N) ")

while continuar == "S" or continuar == "s":
    genero = input("Qual o seu género? (M/F) ")
    idade = int(input("Qual a sua idade? "))

    if genero == "M" or genero == "m":
        fcm = 220 - idade
    elif genero == "F" or genero == "f":
        fcm = 226 - idade
    else:
        print("Género inválido!")

    fca = int(input("Qual a sua frequência cardíaca atual? "))
    if fca >= 0.5 * fcm and fca <= 0.6 * fcm:
        print("Atividade moderada")
    elif fca >= 0.61 * fcm and fca <= 0.7 * fcm:
        print("Atividade intensa")
    elif fca >= 0.71 * fcm and fca <= 0.8 * fcm:
        print("Nível aeróbico")
    elif fca >= 0.81 * fcm and fca <= 0.9 * fcm:
        print("Nível anaeróbico")
    elif fca >= 0.91 * fcm and fca <= 1 * fcm:
        print("Red zone")
    else:
        print("Frequência cardíaca atual inválida!")

    continuar = input("Deseja continuar? (S/N) ")