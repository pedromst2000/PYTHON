from classes.prova import prova

# display the races of the logged in user


def displayRaces(username):

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


def addProof(proof, date, local, distance, creator):

    prova(proof, date, local, distance, creator).addProva()

    return True

def deleteProof(selectedProof):

    file = open("files/provas.txt", "r", encoding="utf-8")

    lines = file.readlines()

    file.close()

    file = open("files/provas.txt", "w+", encoding="utf-8")

    for line in lines:
        # compare the selected proof with the line in the file and if they match remove the selected line by replacing it with nothing
        if selectedProof in line:
            line = ""
        file.write(line)

    file.close()

    return True


def isAlreadyAdded(proof):

    file = open("files/provas.txt", "r", encoding="utf-8")

    lines = file.readlines()

    file.close()

    for line in lines:
        if proof in line:
            return True

    return False