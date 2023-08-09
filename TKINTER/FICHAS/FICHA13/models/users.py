from Classes.user import User

def login(username, password):
    file = open("files/utilizadores.txt", "r", encoding="utf-8")

    for line in file:
        line = line.strip()
        user = line.split(";")

        if user[0] == username and user[1] == password:
            return True
        
    return False

def register(username, password):

    file = open("files/utilizadores.txt", "r", encoding="utf-8")

    for line in file:
        # check if the username already exists
        if username in line:
            return False
        else:
            # if the username doesn't exist, create a new user+
            User(username, password).addUser()
            return True
        