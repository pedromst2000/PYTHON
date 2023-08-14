class prova:

    # attributes
    Prova = ""
    Data = ""
    Local = ""
    Distance = ""
    Creator = ""

    # constructor
    def __init__(self, Prova, Data, Local, Distance, Creator):

        self.Prova = Prova
        self.Data = Data
        self.Local = Local
        self.Distance = Distance
        self.Creator = Creator

    # addProva method
    def addProva(self):
        file = open("files/provas.txt", "a", encoding="utf-8")

        file.write(
            f'\n{self.Prova};{self.Data};{self.Local};{self.Distance};{self.Creator}')
        file.close()
