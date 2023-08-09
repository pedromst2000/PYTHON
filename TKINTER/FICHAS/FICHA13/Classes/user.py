class User:
    #constructor
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # addUser method
    def addUser(self):
        file = open("files/utilizadores.txt", "a", encoding="utf-8")
        file.write(f'\n{self.username};{self.password}')
        file.close()