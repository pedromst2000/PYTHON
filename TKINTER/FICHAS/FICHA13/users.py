def login(username, password):
    file = open("users.txt", "r", encoding="utf-8")

    for line in file:
        line = line.strip()
        user = line.split(";")

        if user[0] == username and user[1] == password:
            return True
        
    return False

def register(username, password, confirmPassword):

    file = open("users.txt", "r", encoding="utf-8")

    for line in file:
        # check if the username already exists
        if username in line:
            return False
        # check if the password and the confirm password are the same
        elif password != confirmPassword:
            return False
        else:
            # if the username doesn't exist and the password and the confirm password are the same,
            # write the username and the password in the file
            file = open("users.txt", "a", encoding="utf-8")
            file.write(f'\n{username};{password}')
            file.close()
            return True