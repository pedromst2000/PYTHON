
def filterRunner(username):
    file = open("provas.txt", "r", encoding="utf-8")

    lines = file.readlines()

    userRunners = []

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
                        # add to the list as dict item with id (the number of the line)
                        userRunners.append({"id": len(userRunners) + 1, "name": line.split(";")[0], "date": line.split(
                            ";")[1], "local": line.split(";")[2], "distance": line.split(";")[3]})

                        break

    print(userRunners)

    file.close()


filterRunner("pedromst2000")
