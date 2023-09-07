import tkinter as tk
from tkinter import *

Window = tk.Tk()
Window.title("Calculator")
Window.geometry("400x400")


selected = StringVar()


entradaOpt = Radiobutton(Window, text="Entrada", variable=selected, value="Entrada")
entradaOpt.place(x=10, y=10)

saidaOpt = Radiobutton(Window, text="Saida", variable=selected, value="Saida")
saidaOpt.place(x=10, y=30)


btnRegistar = Button(Window, text="Registar", width=10, height=1)
btnRegistar.place(x=10, y=60)

def Registar():
    print(selected.get())


btnRegistar.config(command=Registar)
Window.mainloop()