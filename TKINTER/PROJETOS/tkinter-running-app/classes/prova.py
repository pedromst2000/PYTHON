import os


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

        # if the last line of the file is empty, don't add a new line
        if os.stat("files/provas.txt").st_size != 0:
            file.write("\n")

            file.write(self.Creator + self.Prova + ";" + self.Data +
                       ";" + self.Local + ";" + self.Distance + ";")

        else:
            file.write(
                f'\n{self.Prova};{self.Data};{self.Local};{self.Distance};{self.Creator}')

        file.close()
