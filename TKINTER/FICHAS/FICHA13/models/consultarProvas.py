def showAllRaces():

    file = open("files/provas.txt", "r", encoding="utf-8")

    lines = file.readlines()

    allRaces = []

    for line in lines:
        prova = line.split(";")[0]
        date = line.split(";")[1]
        local = line.split(";")[2]
        distance = line.split(";")[3]
        allRaces.append({"name": prova, "date": date,
                        "local": local, "distance": distance})

    file.close()

    return allRaces


def displayMyRaces(username):

    file = open("files/provas.txt", "r", encoding="utf-8")

    lines = file.readlines()

    userRaces = []

    for line in lines:
        if username in line:
            for i in range(0, len(line)):
                if line[i] == username[0]:
                    if line[i:i+len(username)] == username:
                        # remove the last \n and the username
                        line = line[:-1]
                        line = line.replace(username, "")
                        # remove the ; from the end of the line
                        line = line[:-1]
                        userRaces.append({"name": line.split(";")[0], "date": line.split(
                            ";")[1], "local": line.split(";")[2], "distance": line.split(";")[3]})
                        break
    file.close()

    return userRaces


def filterProofs(distance):

    file = open("files/provas.txt", "r", encoding="utf-8")

    lines = file.readlines()

    filteredRaces = []

    for line in lines:
        if distance in line:
            prova = line.split(";")[0]
            date = line.split(";")[1]
            local = line.split(";")[2]
            distance = line.split(";")[3]
            filteredRaces.append(
                {"name": prova, "date": date, "local": local, "distance": distance})

    file.close()

    return filteredRaces


def filterLoggedUserProofs(distance, loggedUser):

    file = open("files/provas.txt", "r", encoding="utf-8")

    lines = file.readlines()

    filteredRaces = []

    for line in lines:
        if distance in line and loggedUser in line:
            prova = line.split(";")[0]
            date = line.split(";")[1]
            local = line.split(";")[2]
            distance = line.split(";")[3]
            filteredRaces.append(
                {"name": prova, "date": date, "local": local, "distance": distance})

    file.close()

    return filteredRaces
