import tkinter as tk
from tkinter import ttk, filedialog, StringVar
import datetime
import random


Window = tk.Tk()
Window.title("Quizz Capitais de Países")
Window.geometry("1200x500")


selectedCountry = StringVar()
selectedTheme = StringVar()
right = 0
wrong = 0


containerProfile = tk.Frame(Window, width=200, height=300, relief="sunken", bd=3)
containerProfile.place(x=5, y=5)

canvasProfile = tk.Canvas(containerProfile, width=160, height=120, bg="white")
canvasProfile.place(x=15, y=15)


btnSelect = tk.Button(containerProfile, text="Selecionar", width=20, height=2)
btnSelect.place(x=15, y=160)

btnGuardar = tk.Button(Window, text="Guardar", width=20, height=2)
btnGuardar.place(x=23, y=230)

containerResult = tk.Frame(Window, width=200, height=150, relief="sunken", bd=3)
containerResult.place(x=5, y=320)

labelRight = tk.Label(containerResult, text="Nº de respostas certas:", font=("Arial", 10))
labelRight.place(x=15, y=15)

entryRight = tk.Entry(containerResult, width=9, font=("Arial", 10), textvariable=right)
entryRight.place(x=70, y=45)

labelWrong = tk.Label(containerResult, text="Nº de respostas erradas:", font=("Arial", 10))
labelWrong.place(x=15, y=75)

entryWrong = tk.Entry(containerResult, width=9, font=("Arial", 10), textvariable=wrong)
entryWrong.place(x=70, y=105)

containerFooter = tk.Frame(Window, width=1200, height=35, relief="groove", bd=3)
containerFooter.place(x=0, y=470)


labelDate = tk.Label(containerFooter, text=datetime.datetime.now().strftime("%d/%m/%Y    %H:%M:%S"), font=("Arial", 10))
labelDate.place(x=0, y=0)

containerQuizz = tk.Frame(Window, width=770, height=300, relief="sunken", bd=3)
containerQuizz.place(x=210, y=5)

labelQuestion = tk.Label(containerQuizz, text="Questão?", font=("Arial", 18, "bold"))
labelQuestion.place(x=385, y=30, anchor="center")

entryAwnser = tk.Entry(containerQuizz, width=22, font=("Arial", 16))
entryAwnser.place(x=385, y=100, anchor="center")

# treeview with the columns 'Capital' 'Status'
treeview = ttk.Treeview(Window, columns=('Capital', 'Status'), show='headings', height=5)
treeview.place(x=575, y=390, anchor="center")

# define headings
treeview.heading('Capital', text='Capital')
treeview.heading('Status', text='Status')

# set column width
treeview.column('Capital', width=400, anchor='center')
treeview.column('Status', width=300, anchor='center')

containerThemes = tk.Frame(Window, width=210, height=460, relief="sunken", bd=3)
containerThemes.place(x=985, y=5)

labelThemes = tk.Label(containerThemes, text="Temas", font=("Arial", 18, "bold"))
labelThemes.place(x=105, y=30, anchor="center")

europeRadio = tk.Radiobutton(containerThemes, text="Europa", value="Europe", variable=selectedTheme)
europeRadio.place(x=105, y=100, anchor="center")

americaRadio = tk.Radiobutton(containerThemes, text="América", value="América", variable=selectedTheme)
americaRadio.place(x=105, y=150, anchor="center")

asiaRadio = tk.Radiobutton(containerThemes, text="Ásia", value="Asia", variable=selectedTheme)
asiaRadio.place(x=105, y=200, anchor="center")

# select europe by default
europeRadio.select()


btnNewQuestion = tk.Button(containerThemes, text="Nova Questão", width=20, height=2)
btnNewQuestion.place(x=105, y=250, anchor="center")

btnAwnser = tk.Button(containerThemes, text="Responder", width=20, height=2)
btnAwnser.place(x=105, y=300, anchor="center")


def quizz_view(continent, fileContinent):
    if selectedTheme.get() == continent:
        file = open(f"files/{fileContinent}", "r", encoding="utf-8")

        # generate a random line 
        line = random.choice(file.readlines())
        print(line)

        capital = line.split(";")[0]

        entryAwnser.insert(0, capital)

        labelCapital = tk.Label(containerQuizz, text="É capital de ", font=("Arial", 12))
        labelCapital.place(x=385, y=130, anchor="center")

        # give the capitals of the line generated to the four radiobuttons unless the last one 
        
        # first capital
        capital1, capital2, capital3, capital4 = line.split(";")[1], line.split(";")[2], line.split(";")[3], line.split(";")[4].replace("\n", "")
        
        radio1 = tk.Radiobutton(containerQuizz, text=capital1, value=capital1, variable=selectedCountry)
        radio1.place(x=185, y=260, anchor="center")

        radio2 = tk.Radiobutton(containerQuizz, text=capital2, value=capital2, variable=selectedCountry)
        radio2.place(x=185, y=210, anchor="center")

        radio3 = tk.Radiobutton(containerQuizz, text=capital3, value=capital3, variable=selectedCountry)
        radio3.place(x=485, y=260, anchor="center")

        radio4 = tk.Radiobutton(containerQuizz, text=capital4, value=capital4, variable=selectedCountry)
        radio4.place(x=485, y=210, anchor="center")

        radio1.select()




def next_question():

    if selectedTheme.get() == "Europe":
        quizz_view("Europe", "europa.txt")
    elif selectedTheme.get() == "América":
        quizz_view("América", "America.txt")
    elif selectedTheme.get() == "Asia":
        quizz_view("Asia", "Asia.txt")

quizz_view("Europe", "europa.txt")
btnNewQuestion.config(command=next_question)
Window.mainloop()