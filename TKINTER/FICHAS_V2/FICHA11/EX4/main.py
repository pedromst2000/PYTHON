import tkinter as tk
from tkinter import *

Window = tk.Tk()
Window.title("EX4")
Window.geometry("800x500")


containerValues = Frame(Window, bd=5, relief=RAISED, width=300, height=180)
containerValues.place(x=10, y=10)

labelWeight = Label(containerValues, text="Peso:", font=("Arial", 12), fg="blue")
labelWeight.place(x=10, y=10)

entryWeight = Entry(containerValues, font=("Arial", 12), width=10)
entryWeight.place(x=90, y=10)

labelHigh = Label(containerValues, text="Altura:", font=("Arial", 12), fg="blue")
labelHigh.place(x=10, y=50)

entryHigh = Entry(containerValues, font=("Arial", 12), width=10)
entryHigh.place(x=90, y=50)

containerIMC = Frame(Window, bd=5, relief=RAISED, width=300, height=180)
containerIMC.place(x=10, y=300)

labelIMC = Label(containerIMC, text="Índice de Massa Corporal", font=("Arial", 12), fg="blue")
labelIMC.place(x=10, y=10)

labelResult = Label(containerIMC, text="Resultado:", font=("Arial", 12))
labelResult.place(x=10, y=50)

btnIMC = Button(Window, text="Calcular IMC", font=("Arial", 12), height=2, width=15)
btnIMC.place(x=420, y=40)

# wrap no texto do botão
btnIMC["wraplength"] = 80

btnExit = Button(Window, text="Sair", font=("Arial", 12), height=2, width=15)
btnExit.place(x=420, y=100)

canvasIMC = Canvas(Window, width=300, height=180, bd=5, relief=RAISED)
canvasIMC.place(x=420, y=300)

# colocar a imagem 'images.png'
img = PhotoImage(file="EX4/images.png")

# posicionar a imagem no canvas
canvasIMC.create_image(0, 0, anchor=NW, image=img)

def caculateIMC():
    weight = float(entryWeight.get())
    higth = float(entryHigh.get())
    imc = weight / (higth * higth)
    imc = round(imc * 10000, 2)

    if imc < 18.5:
        labelResult["text"] = "Resultado: Abaixo do peso"
    elif imc >= 18.5 and imc <= 24.9:
        labelResult["text"] = "Resultado: Peso normal"
    elif imc >= 25 and imc <= 29.9:
        labelResult["text"] = "Resultado: Sobrepeso"
    elif imc >= 30 and imc <= 34.9:
        labelResult["text"] = "Resultado: Obesidade grau 1"
    elif imc >= 35 and imc <= 39.9:
        labelResult["text"] = "Resultado: Obesidade grau 2"
    else:
        labelResult["text"] = "Resultado: Obesidade grau 3"

btnIMC["command"] = caculateIMC
btnExit["command"] = Window.quit


Window.mainloop()