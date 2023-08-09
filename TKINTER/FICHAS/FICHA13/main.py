import tkinter as tk
from tkinter import ttk, messagebox
# from PIL import ImageTk, Image

from models.consultarProvas import *
from models.gerirProvas import *
from models.users import *

Window = tk.Tk()
Window.title("my Running App")
Window.geometry("1200x600")

# logical variables
userIsLogged = False
loggedUser = ""
registeredUser = ""

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


# --------------------------------------------------------------------AUTHENTICATION VIEW --------------------------------------------------------------------
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

        btnLogin.config(command=lambda: checkLoginView(entryUsername, entryPassword, containerLogin))


def RegisterView():
        containerRegister = tk.Frame(Window, bg="#2c2c2c", width=780, height=350)
        containerRegister.place(x=310, y=150)

        # destroy the containerRegister when  clicked on the canvas
        canvasHome.bind("<Button-1>", lambda event: containerRegister.destroy())

        labelUsername = tk.Label(containerRegister, text="Username", fg="white", font=("Arial", 12))
        labelUsername.place(x=220, y=90)

        # remove the background of the label
        labelUsername.config(bg="#2c2c2c")

        entryUsername = tk.Entry(containerRegister, width=20, font=("Arial", 12))
        entryUsername.place(x=320, y=90)

        labelPassword = tk.Label(containerRegister, text="Password", fg="white", font=("Arial", 12))
        labelPassword.place(x=220, y=140)

        labelPassword.config(bg="#2c2c2c")

        entryPassword = tk.Entry(containerRegister, width=20, font=("Arial", 12))
        entryPassword.place(x=320, y=140)

        labelConfirmPassword = tk.Label(containerRegister, text="Confirmar Password", fg="white", font=("Arial", 12))
        labelConfirmPassword.place(x=220, y=190)

        labelConfirmPassword.config(bg="#2c2c2c")

        entryConfirmPassword = tk.Entry(containerRegister, width=20, font=("Arial", 12))
        entryConfirmPassword.place(x=390, y=190)
        
        btnRegister = tk.Button(containerRegister, text="Registar", width=15, height=2, font=("Arial", 12))
        btnRegister.place(x=320, y=250)

        btnRegister.config(command=lambda: checkRegisterView(entryUsername, entryPassword, entryConfirmPassword, containerRegister))


def checkLoginView(username, password, containerLogin):
 
  global userIsLogged
  global loggedUser

  if username.get() == "" and password.get() == "":
        messagebox.showerror("Login", "Preencha todos os campos!")
        userIsLogged = False

  if username.get() == "" and password.get() != "":
        messagebox.showerror("Login", "Preencha o campo username!")
        userIsLogged = False 

  if username.get() != "" and password.get() == "":
        messagebox.showerror("Login", "Preencha o campo password!")
        userIsLogged = False

  if username.get() != "" and password.get() != "":
       if login(username.get(), password.get()):
           messagebox.showinfo("Login", "Login efetuado com sucesso!")
           userIsLogged = True
           loggedUser = username.get()
           containerLogin.destroy()
           headerView()
       else:
           messagebox.showerror("Login", "Username ou password incorretos!")
           userIsLogged = False      


def checkRegisterView(username, password, confirmPassword, containerRegister):
        global userIsLogged
        global loggedUser

        if username.get() == "" and password.get() == "" and confirmPassword.get() == "":
                messagebox.showerror("Registar", "Preencha todos os campos!")

        if username.get() != "" and password.get() == "" and confirmPassword.get() == "":
                messagebox.showerror("Registar", "Preencha o campo password!")

        if username.get() != "" and password.get() != "" and confirmPassword.get() == "":
                messagebox.showerror("Registar", "Preencha o campo confirmar password!")
  
        if username.get() == "" and password.get() != "" and confirmPassword.get() != "":
                messagebox.showerror("Registar", "Preencha o campo username!")

        if username.get() == "" and confirmPassword.get() == "" and password.get() != "":
                messagebox.showerror("Registar", "Preencha o campo username!")

        elif username.get() != "" and password.get() != "" and confirmPassword.get() != "":
                if password.get() != confirmPassword.get():
                        messagebox.showerror("Registar", "As passwords não coincidem!")
                else:
                        if register(username.get(), password.get()):
                                messagebox.showinfo("Registar", "Registo efetuado com sucesso!")
                                containerRegister.destroy()
                                userIsLogged = True
                                loggedUser = username.get()
                                headerView()
                        else:
                                messagebox.showerror("Registar", "O username já existe!")

def headerView():
  global userIsLogged
  global loggedUser

  if userIsLogged == True:
       btnLogin.destroy()
       btnCreateAccount.destroy()
       labelWelcome = tk.Label(Window, text=f"Bem-vindo(a) {loggedUser} !", font=("Arial", 14), fg="blue")
       labelWelcome.place(x=260, y=40)
       btnLogOut = tk.Button(Window, text="Terminar Sessão", width=15, height=2, font=("Arial", 12))
       btnLogOut.place(x=1030, y=20)


# ------------------------------------------------------------------------------------------------------------------------------------------

btnLogin.config(command=loginView)
btnCreateAccount.config(command=RegisterView)
Window.mainloop()