class prova:
    # constructor
    def __init__(self ,Prova, Data, Local) :
        
        self.Prova = Prova
        self.Data = Data
        self.Local = Local

    # addProva method
    def addProva(self):
        file = open("files/provas.txt", "a", encoding="utf-8")
        file.write(f'\n{self.Prova};{self.Data};{self.Local}')
        file.close()

    # deleteProva method
    def deleteProva(self):
        file = open("files/provas.txt", "r", encoding="utf-8")
        lines = file.readlines()
        file.close()

        file = open("files/provas.txt", "w+", encoding="utf-8")
        for line in lines:
            if line.strip("\n") != f'{self.Prova};{self.Data};{self.Local}':
                file.write(line)
        file.close()