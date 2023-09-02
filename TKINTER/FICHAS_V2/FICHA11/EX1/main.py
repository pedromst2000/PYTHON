import tkinter as tk
import os
from tkinter import *


Window = tk.Tk()
Window.title("Ex1")
Window.geometry("800x400")

# caixa de texto
txt = Text(Window, width=50, height=10)
txt.place(x=300, y=40)


btnSave = Button(Window, text="Guardar ficheiro", width=20, height=2, fg="blue")
btnSave.place(x=40, y=40)

btnClean = Button(Window, text="Limpar", width=20, height=2, fg="blue")
btnClean.place(x=40, y=140)

btnRead = Button(Window, text="Ler ficheiro", width=20, height=2, fg="blue")
btnRead.place(x=40, y=240)


def saveFile():
    # guardar o conteudo no ficheiro texo.txt, se nao existir cria um novo ficheiro
    if os.path.exists("EX1/texto.txt"):
        f = open("EX1/texto.txt", "a", encoding="utf-8")
        f.write(txt.get("1.0", END))
        f.close()
    else:
        f = open("EX1/texto.txt", "w")
        f.write(txt.get("1.0", END))
        f.close()


def clean():
    # limpar a caixa de texto
    txt.delete("1.0", END)


def readFile():
    file = open("EX1/texto.txt", "r", encoding="utf-8")

    # ler o conteudo do ficheiro
    txt.insert(END, file.read())

    file.close()


btnSave.config(command=saveFile)
btnClean.config(command=clean)
btnRead.config(command=readFile)



Window.mainloop()