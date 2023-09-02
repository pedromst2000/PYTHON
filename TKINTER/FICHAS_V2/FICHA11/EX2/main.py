import tkinter as tk
from tkinter import *

Window = tk.Tk()
Window.title("Ex2")
Window.geometry("800x400")

genrerSelected = StringVar()

lblAltura = Label(Window, text="Altura em cm:", fg="blue")
lblAltura.place(x=40, y=40)

entryAltura = Entry(Window, width=20)
entryAltura.place(x=120, y=40)

containerGenrer = LabelFrame(Window, text="Género", width=190, height=160, relief="sunken", borderwidth=2, fg="blue")
containerGenrer.place(x=40, y=130)

# radio buttons
radioM = Radiobutton(containerGenrer, text="Masculino", value="M", variable=genrerSelected)
radioM.place(x=10, y=10)

radioF = Radiobutton(containerGenrer, text="Feminino", value="F", variable=genrerSelected)
radioF.place(x=10, y=80)
radioM.select() 

btnCalcular = Button(Window, text="Calcular Peso Ideal", width=20, height=7)
btnCalcular.place(x=280, y=160)

# wrap no texto do botao
btnCalcular.config(wraplength=90)


containerResult = LabelFrame(Window, width=280, height=160, relief="sunken", borderwidth=2)
containerResult.place(x=470, y=130)

labelPesoIdeal = Label(containerResult, text="Peso Ideal em Kg", fg="blue")
labelPesoIdeal.place(x=120, y=10)

entryPesoIdeal = Entry(containerResult, width=20)
entryPesoIdeal.place(x=100, y=40)


def calcularPeso():
    # buscar o valor da altura
    altura = float(entryAltura.get())
    genero = genrerSelected.get()

    # formula do calculo do peso ideal
    if genero == "M":
        pesoIdeal = (altura-100) - ((altura-150)/4)
    else:
        pesoIdeal = (altura-100) - ((altura-150)/2)

    # mostrar o resultado
    entryPesoIdeal.delete(0, END)
    entryPesoIdeal.insert(0, pesoIdeal)

btnCalcular.config(command=calcularPeso)    

Window.mainloop()