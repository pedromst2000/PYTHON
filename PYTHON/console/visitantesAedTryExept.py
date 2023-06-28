def diaSemana():
    values = list(visitantes.values())

    avg = sum(values) / len(values)

    max_diff = 0

    farthest_day = ""

    for dia, value in visitantes.items():
        # GIVE THE ABSOLUTE NUMBER
        diff = abs(value - avg)

        if diff > max_diff:

            max_diff = diff

    farthest_day = dia

    print(f"\n\n\n Dia da semana mais distante da média: {farthest_day} \n\n\n")


def ordemVisitas(visitantes):
    # TAKE EVERY ITEM FROM THE DICTIONARY AND REVERSE IT BASED ON THE VALUE OF EACH KEY IN THIS CASE THE AMOUNT OF PEOPLE IN EACH DAY "item[1]"
    sorted_visitantes = sorted(visitantes.items(), key=lambda item: item[1], reverse=True)
    result = ""

    for item in sorted_visitantes:
        result += f"{item[0]} {item[1]}\n"
    return result




dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

visitantes = {}

for dia in dias:
    while True:
        try:
            valor = int(input(f"Nº visitantes no/a {dia}: "))
            if valor >= 0 and valor <= 100:
                visitantes[dia] = valor
                break
            else:
                print("Erro, o valor inserido deve ser um número inteiro entre 0 e 100!")
        except ValueError:
            print("Erro, o valor inserido deve ser um número inteiro entre 0 e 100!")
diaSemana()
print(ordemVisitas(visitantes))
   