import tkinter as tk
from tkinter import ttk, messagebox, StringVar, IntVar
from tkcalendar import DateEntry

from models.consultarProvas import *
from models.gerirProvas import *
from models.users import *

Window = tk.Tk()
Window.title("my Running App")
Window.geometry("1200x600")

# logical variables
userIsLogged = False
userLogged = ""
passwordIsVisible = False
selectedRace = StringVar()
deletedImage = tk.PhotoImage(file="images/remover.png")

# --------------------------------------------------------------------HOME VIEW --------------------------------------------------------------------

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

btnManageUsers = tk.Button(containerMenuBackground, text="Sair App", width=170, height=92,
                           image=imgbtnOpt3, compound="left", font=("Arial", 12, "bold"))
btnManageUsers.place(x=20, y=350)

btnManageUsers.config(anchor=tk.CENTER)

btnManageUsers.config(wraplength=90)

# button 'Iniciar Sessão' on the top of the window
btnLogin = tk.Button(Window, text="Iniciar Sessão",
                     width=15, height=2, font=("Arial", 12))
btnLogin.place(x=860, y=20)

btnCreateAccount = tk.Button(
    Window, text="Criar Conta", width=15, height=2, font=("Arial", 12))
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
    btnLogin.config(command=lambda: checkLoginView(
        entryUsername, entryPassword, containerLogin))


def RegisterView():

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

    btnRegister.config(command=lambda: checkRegisterView(
        entryUsername, entryPassword, entryConfirmPassword, containerRegister))


def checkLoginView(username, password, containerLogin):

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
            headerView()
        else:
            messagebox.showerror("Login", "Username ou password incorretos!")
            userIsLogged = False


def checkRegisterView(username, password, confirmPassword, containerRegister):
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
                headerView()
            else:
                messagebox.showerror("Registar", "O username já existe!")


def logout():
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

# ----------------------------------------------------------------------HEADER VIEW-------------------------------------------------------


def headerView():
    global userIsLogged
    global userLogged

    if userIsLogged == True:
        # hidden the login and register buttons~
        btnLogin.place_forget()
        btnCreateAccount.place_forget()
        labelWelcome = tk.Label(
            Window, text=f"Bem-vindo(a) {userLogged} !", font=("Arial", 14), fg="blue")
        labelWelcome.place(x=260, y=40)
        btnLogOut = tk.Button(Window, text="Terminar Sessão",
                              width=15, height=2, font=("Arial", 12))
        btnLogOut.place(x=1030, y=20)
        btnLogOut.config(command=lambda: logout())
# ----------------------------------------------------------------------MANAGE RACES VIEW-------------------------------------------------------


def manageRacesOption():
    global userIsLogged
    global userLogged

    if userIsLogged == False:
        return messagebox.showerror("Gerir Corridas", "Tem de fazer login para aceder a esta funcionalidade!")
    else:
        # destroy the canvas
        canvasHome.place_forget()
        manageRacesView()


def manageRacesView():

    global selectedRace
    global userLogged
    global addImage
    global deletedImage

    selectedRace.set("Caminhada")

    containerRacesView = tk.Frame(Window, width=980, height=600)
    containerRacesView.place(x=220, y=100)

    labelProof = tk.Label(containerRacesView,
                          text="Prova", font=("Arial", 12))
    labelProof.place(x=50, y=30)

    entryProof = tk.Entry(containerRacesView, width=30)
    entryProof.place(x=120, y=30)

    labelDate = tk.Label(containerRacesView,
                         text="Data", font=("Arial", 12))
    labelDate.place(x=50, y=70)

    # calendar
    entryDate = DateEntry(containerRacesView, width=12,
                          background='darkblue', foreground='white', borderwidth=2)
    entryDate.place(x=120, y=70)

    labeLocal = tk.Label(containerRacesView,
                         text="Local", font=("Arial", 12))
    labeLocal.place(x=50, y=110)

    entryLocal = tk.Entry(containerRacesView, width=30)
    entryLocal.place(x=120, y=110)

    labelType = tk.Label(containerRacesView,
                         text="Tipo", font=("Arial", 12))
    labelType.place(x=50, y=150)

    radioTrail = tk.Radiobutton(
        containerRacesView, text="Caminhada", variable=selectedRace, value="Caminhada")
    radioTrail.place(x=120, y=150)

    radio5K = tk.Radiobutton(
        containerRacesView, text="5K", variable=selectedRace, value="5K")
    radio5K.place(x=120, y=180)

    radio10K = tk.Radiobutton(
        containerRacesView, text="10K", variable=selectedRace, value="10K")
    radio10K.place(x=120, y=210)

    radio21K = tk.Radiobutton(
        containerRacesView, text="21K", variable=selectedRace, value="21K")
    radio21K.place(x=120, y=240)

    listUserRaces = tk.Listbox(containerRacesView, width=70, height=15)
    listUserRaces.place(x=520, y=10)

    # insert the races from the logged user in the listbox
    loggedUserRaces = displayRaces(userLogged)

    # iterate the dictionary
    for i in loggedUserRaces:
        listUserRaces.insert(
            tk.END, f'{i["name"]}  {i["date"]}  {i["local"]}  {i["distance"]}')

    # increase the font size of the listbox
    listUserRaces.config(font=("Arial", 11))

    # add scrollbar horizontal and vertical
    scrollbar = tk.Scrollbar(containerRacesView, orient="vertical")
    scrollbar.config(command=listUserRaces.yview)

    scrollbar.place(x=960, y=10, height=300)

    # add scrollbar horizontal and vertical
    scrollbar = tk.Scrollbar(containerRacesView, orient="horizontal")
    scrollbar.config(command=listUserRaces.xview)

    scrollbar.place(x=520, y=300, width=440)

    addImage = tk.PhotoImage(file="images/adicionar.png")
    addImage.subsample(1, 1)

    btnAddRace = tk.Button(containerRacesView, width=90, height=70,
                           image=addImage, compound="left", bd=0, cursor="hand2")
    btnAddRace.place(x=650, y=350)

    btnRemoveRace = tk.Button(containerRacesView,  width=90,
                              height=70, image=deletedImage, bd=0, cursor="hand2")
    btnRemoveRace.place(x=740, y=350)

    btnAddRace.config(command=lambda: addProofView(
        entryProof.get(), entryDate.get_date(), entryLocal.get(), selectedRace.get(), userLogged, listUserRaces))

    btnRemoveRace.config(command=lambda: deleteProofView(
        # got the index of the selected line
        listUserRaces.curselection(), listUserRaces
    ))


def addProofView(proof, date, local, distance, creator, listProof):

    if proof == "" and local == "":
        return messagebox.showerror("Adicionar Prova", "Tem de preencher todos os campos!")

    if proof != "" and local == "":
        return messagebox.showerror("Adicionar Prova", "Tem de preencher o campo Local!")

    if proof == "" and local != "":
        return messagebox.showerror("Adicionar Prova", "Tem de preencher o campo Prova!")

    else:
        messagebox.showinfo("Adicionar Prova", "Prova adicionada com sucesso!")
        addProof(proof, date, local, distance, creator)
        listProof.insert(tk.END, f'{proof}  {date}  {local}  {distance}')


def deleteProofView(selectedLine, listProof):

    if listProof.curselection() == ():
        return messagebox.showerror("Remover Prova", "Tem de selecionar uma prova!")

    else:
        checkDelete = messagebox.askyesno(
            "Remover Prova", "Tem a certeza que pretende remover a prova selecionada?")

        if checkDelete == True:
            messagebox.showinfo("Remover Prova", "Prova removida com sucesso!")

            # get the index of the selected line
            index = listProof.curselection()[0]

            # get the text of the selected line
            text = listProof.get(index)

            # split the text
            text = text.split()

            # get the name of the proof
            proof = text[0]

            # delete the proof
            deleteProof(proof)

            # delete the selected line
            listProof.delete(index)

        return False

# -------------------------------------------------------------------CONSULT RACES VIEW-------------------------------------------------------


def consultRacesOption():
    global userIsLogged

    if userIsLogged == False:
        return messagebox.showerror("Consultar Corridas", "Tem de fazer login para aceder a esta funcionalidade!")
    else:
        consultRacesView()


def consultRacesView():

    containerRacesView = tk.Frame(Window, width=980, height=600)
    containerRacesView.place(x=220, y=100)


# ------------------------------------------------------------------------------------------------------------------------------------------
btnLogin.config(command=loginView)
btnCreateAccount.config(command=RegisterView)
btnManageRaces.config(command=manageRacesOption)
btnConsultRaces.config(command=consultRacesOption)

Window.mainloop()
