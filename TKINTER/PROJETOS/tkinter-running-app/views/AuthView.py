import tkinter as tk
from tkinter import messagebox
from models.users import login, register

# global variables
userIsLogged = False
userLogged = ""
passwordIsVisible = False


def LOGIN(Window, canvasHome):

    containerLogin = tk.Frame(Window, bg="#2c2c2c", width=780, height=300)
    containerLogin.place(x=310, y=150)

    # destroy the containerLogin when  clicked on the canvas
    canvasHome.bind("<Button-1>", lambda event: containerLogin.destroy())

    labelUsername = tk.Label(
        containerLogin, text="Username", fg="white", font=("Arial", 12))
    labelUsername.place(x=220, y=90)

    # remove the background of the label
    labelUsername.config(bg="#2c2c2c")

    entryUsername = tk.Entry(containerLogin, width=20, font=("Arial", 12))
    entryUsername.place(x=320, y=90)

    labelPassword = tk.Label(
        containerLogin, text="Password", fg="white", font=("Arial", 12))
    labelPassword.place(x=220, y=140)

    labelPassword.config(bg="#2c2c2c")

    entryPassword = tk.Entry(containerLogin, width=20,
                             font=("Arial", 12), show="*")
    entryPassword.place(x=320, y=140)

    btnPassword = tk.Button(containerLogin, text="Show",
                            width=10, height=1, font=("Arial", 10))
    btnPassword.place(x=530, y=140)

    btnLogin = tk.Button(containerLogin, text="Login",
                         width=15, height=2, font=("Arial", 12))
    btnLogin.place(x=320, y=200)

    btnPassword.config(command=lambda: managePassword(
        entryPassword, btnPassword))
    btnLogin.config(command=lambda: checkLogin(
        entryUsername, entryPassword, containerLogin))


def REGISTER(Window, canvasHome):

    containerRegister = tk.Frame(Window, bg="#2c2c2c", width=780, height=350)
    containerRegister.place(x=310, y=150)

    # destroy the containerRegister when  clicked on the canvas
    canvasHome.bind("<Button-1>", lambda event: containerRegister.destroy())

    labelUsername = tk.Label(
        containerRegister, text="Username", fg="white", font=("Arial", 12))
    labelUsername.place(x=220, y=90)

    # remove the background of the label
    labelUsername.config(bg="#2c2c2c")

    entryUsername = tk.Entry(containerRegister, width=20, font=("Arial", 12))
    entryUsername.place(x=320, y=90)

    labelPassword = tk.Label(
        containerRegister, text="Password", fg="white", font=("Arial", 12))
    labelPassword.place(x=220, y=140)

    labelPassword.config(bg="#2c2c2c")

    entryPassword = tk.Entry(containerRegister, width=20,
                             font=("Arial", 12), show="*")
    entryPassword.place(x=320, y=140)

    labelConfirmPassword = tk.Label(
        containerRegister, text="Confirmar Password", fg="white", font=("Arial", 12))
    labelConfirmPassword.place(x=220, y=190)

    labelConfirmPassword.config(bg="#2c2c2c")

    entryConfirmPassword = tk.Entry(
        containerRegister, width=20, font=("Arial", 12), show="*")
    entryConfirmPassword.place(x=390, y=190)

    btnPassword = tk.Button(containerRegister, text="Show",
                            width=10, height=1, font=("Arial", 10))
    btnPassword.place(x=530, y=140)

    btnConfirmPassword = tk.Button(
        containerRegister, text="Show", width=10, height=1, font=("Arial", 10))
    btnConfirmPassword.place(x=590, y=190)

    btnRegister = tk.Button(
        containerRegister, text="Registar", width=15, height=2, font=("Arial", 12))
    btnRegister.place(x=320, y=250)

    btnPassword.config(command=lambda: managePassword(
        entryPassword, btnPassword))
    btnConfirmPassword.config(command=lambda: managePassword(
        entryConfirmPassword, btnConfirmPassword))

    btnRegister.config(command=lambda: checkRegister(
        entryUsername, entryPassword, entryConfirmPassword, containerRegister))


def checkLogin(username, password, containerLogin):

    global userIsLogged
    global userLogged

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
            userLogged = username.get()
            containerLogin.destroy()
            # headerView()
        else:
            messagebox.showerror("Login", "Username ou password incorretos!")
            userIsLogged = False


def checkRegister(username, password, confirmPassword, containerRegister):
    global userIsLogged
    global userLogged

    userLogged = username.get()

    if username.get() == "" and password.get() == "" and confirmPassword.get() == "":
        messagebox.showerror("Registar", "Preencha todos os campos!")

    if username.get() != "" and password.get() == "" and confirmPassword.get() == "":
        messagebox.showerror("Registar", "Preencha o campo password!")

    if username.get() != "" and password.get() != "" and confirmPassword.get() == "":
        messagebox.showerror(
            "Registar", "Preencha o campo confirmar password!")

    if username.get() == "" and password.get() != "" and confirmPassword.get() != "":
        messagebox.showerror("Registar", "Preencha o campo username!")

    if username.get() == "" and confirmPassword.get() == "" and password.get() != "":
        messagebox.showerror("Registar", "Preencha o campo username!")

    if username.get() != "" and password.get() != "" and confirmPassword.get() != "":
        if password.get() != confirmPassword.get():
            messagebox.showerror("Registar", "As passwords não coincidem!")
        else:
            if register(username.get(), password.get()):
                messagebox.showinfo(
                    "Registar", f"Registo efetuado com sucesso! Bem-vindo(a) {username.get()}!")
                userIsLogged = True
                userLogged
                containerRegister.destroy()
                # headerView()
            else:
                messagebox.showerror("Registar", "O username já existe!")


def logout(Window):
    Window.destroy()


def managePassword(password, btnManagePassword):
    global passwordIsVisible

    if passwordIsVisible == False:
        password.config(show="")
        btnManagePassword.config(text="hide")
        passwordIsVisible = True
    else:
        password.config(show="*")
        btnManagePassword.config(text="show")
        passwordIsVisible = False

