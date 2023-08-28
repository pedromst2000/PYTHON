from classes.user import User

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
        line = line.strip()
        user = line.split(";")

        if user[0] == username:
            return False
        
    User(username, password).addUser()      
    return True  