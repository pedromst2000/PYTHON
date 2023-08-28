import tkinter as tk
from tkinter import *
from views.AuthView import *


Window = tk.Tk()
Window.title("Running App")
Window.geometry("1200x600")

# remove the maximize button
Window.resizable(False, False)

# disable the X button
Window.protocol("WM_DELETE_WINDOW", False)


containerMenuBackground = tk.Frame(Window, bg="#2c2c2c", width=220, height=600)
containerMenuBackground.grid(row=0, column=0, sticky="nsew")

# put the image 'menuOpt1.png' from the images folder on the button
imgbtnOpt1 = tk.PhotoImage(file="images/menuOpt1.png")

# reduce the size of the image
imgbtnOpt1 = imgbtnOpt1.subsample(2, 2)


btnManageRaces = tk.Button(containerMenuBackground, text="Gerir Provas",  width=170, height=92,
                           image=imgbtnOpt1, compound="left", font=("Arial", 12, "bold"))
btnManageRaces.place(x=20, y=100)


# center the text 'Gerir Provas' on the button
btnManageRaces.config(anchor=tk.CENTER)

# wrap the text 'Gerir Provas' on the button
btnManageRaces.config(wraplength=90)

imgbtnOpt2 = tk.PhotoImage(file="images/menuOpt2.png")
imgbtnOpt2 = imgbtnOpt2.subsample(2, 2)

btnConsultRaces = tk.Button(containerMenuBackground, text="Consultar Provas", width=170, height=92,
                            image=imgbtnOpt2, compound="left", font=("Arial", 12, "bold"))
btnConsultRaces.place(x=20, y=220)

btnConsultRaces.config(anchor=tk.CENTER)

btnConsultRaces.config(wraplength=90)

imgbtnOpt3 = tk.PhotoImage(file="images/menuOpt3.png")
imgbtnOpt3 = imgbtnOpt3.subsample(2, 2)

btnExitApp = tk.Button(containerMenuBackground, text="Sair App", width=170, height=92,
                       image=imgbtnOpt3, compound="left", font=("Arial", 12, "bold"), command=lambda: logout(
                            Window
                       ))
btnExitApp.place(x=20, y=350)

btnExitApp.config(anchor=tk.CENTER)

btnExitApp.config(wraplength=90)

# button 'Iniciar Sessão' on the top of the window
btnLogin = tk.Button(Window, text="Iniciar Sessão",
                     width=15, height=2, font=("Arial", 12), command=lambda: login(
                            Window, canvasHome
                     ))
btnLogin.place(x=860, y=20)

btnCreateAccount = tk.Button(
    Window, text="Criar Conta", width=15, height=2, font=("Arial", 12), command=lambda: Register(
        Window, canvasHome
    ))
btnCreateAccount.place(x=1030, y=20)


canvasHome = tk.Canvas(Window, width=980, height=600, bg="white")
canvasHome.place(x=220, y=100)

# put the image 'mainImage.png' from the images folder on the canvas
imgMainImage = tk.PhotoImage(file="images/mainImage.png")
canvasHome.create_image(490, 230, image=imgMainImage)


Window.mainloop()