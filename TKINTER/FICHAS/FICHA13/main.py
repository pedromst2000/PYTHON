import tkinter as tk
from tkinter import ttk, messagebox
# from PIL import ImageTk, Image

from consultarProvas import *
from gerirProvas import *
from users import *

Window = tk.Tk()
Window.title("my Running App")
Window.geometry("1200x600")

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

btnManageUsers = tk.Button(containerMenuBackground, text="Sair App", width=170, height=92,
                            image=imgbtnOpt3, compound="left", font=("Arial", 12, "bold"))
btnManageUsers.place(x=20, y=350)

btnManageUsers.config(anchor=tk.CENTER)

btnManageUsers.config(wraplength=90)

# button 'Iniciar Sessão' on the top of the window
btnLogin = tk.Button(Window, text="Iniciar Sessão", width=15, height=2, font=("Arial", 12))
btnLogin.place(x=860, y=20)

btnCreateAccount = tk.Button(Window, text="Criar Conta", width=15, height=2, font=("Arial", 12))
btnCreateAccount.place(x=1030, y=20)


canvasHome = tk.Canvas(Window, width=980, height=600, bg="white")
canvasHome.place(x=220, y=100)

# put the image 'mainImage.png' from the images folder on the canvas
imgMainImage = tk.PhotoImage(file="images/mainImage.png")
canvasHome.create_image(490, 230, image=imgMainImage)


def loginView():
        containerLogin = tk.Frame(Window, bg="#2c2c2c", width=780, height=300)
        containerLogin.place(x=310, y=150)

        # destroy the containerLogin when  clicked on the canvas
        canvasHome.bind("<Button-1>", lambda event: containerLogin.destroy())

        labelUsername = tk.Label(containerLogin, text="Username", fg="white", font=("Arial", 12))
        labelUsername.place(x=220, y=90)

        # remove the background of the label
        labelUsername.config(bg="#2c2c2c")

        entryUsername = tk.Entry(containerLogin, width=20, font=("Arial", 12))
        entryUsername.place(x=320, y=90)

        labelPassword = tk.Label(containerLogin, text="Password", fg="white", font=("Arial", 12))
        labelPassword.place(x=220, y=140)

        labelPassword.config(bg="#2c2c2c")

        entryPassword = tk.Entry(containerLogin, width=20, font=("Arial", 12))
        entryPassword.place(x=320, y=140)

        btnLogin = tk.Button(containerLogin, text="Login", width=15, height=2, font=("Arial", 12))
        btnLogin.place(x=320, y=200)

        # get the username and the password from the entryUsername and the entryPassword
        username = entryUsername.get()
        password = entryPassword.get()

        checkLogin(username, password)



def checkLogin(username, password):
        print(username, password)



btnLogin.config(command=loginView)
Window.mainloop()
