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
countProof = 0
selectedRace = StringVar()
# for solving the bug of the image not showing
deletedImage = tk.PhotoImage(file="images/remover.png")
searchImage = tk.PhotoImage(file="images/pesquisar.png")
ascImage = tk.PhotoImage(file="images/asc.png")
descImage = tk.PhotoImage(file="images/desc.png")

# all the possibile filters while checking the proofs
allProofs = IntVar()
myProofs = IntVar()
fiveKproofs = IntVar()
tenKproofs = IntVar()
twentyOneKproofs = IntVar()
trailProofs = IntVar()

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

btnExitApp = tk.Button(containerMenuBackground, text="Sair App", width=170, height=92,
                       image=imgbtnOpt3, compound="left", font=("Arial", 12, "bold"))
btnExitApp.place(x=20, y=350)

btnExitApp.config(anchor=tk.CENTER)

btnExitApp.config(wraplength=90)

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
        listUserRaces
    ))


def addProofView(proof, date, local, distance, creator, listProof):

    if proof == "" and local == "":
        return messagebox.showerror("Adicionar Prova", "Tem de preencher todos os campos!")

    if proof != "" and local == "":
        return messagebox.showerror("Adicionar Prova", "Tem de preencher o campo Local!")

    if proof == "" and local != "":
        return messagebox.showerror("Adicionar Prova", "Tem de preencher o campo Prova!")

    if proof != "" and local != "":
        if isAlreadyAdded(proof):
            return messagebox.showerror("Adicionar Prova", "A prova já existe!")

        else:
            messagebox.showinfo("Adicionar Prova",
                                "Prova adicionada com sucesso!")
            addProof(proof, date, local, distance, creator)
            listProof.insert(tk.END, f'{proof}  {date}  {local}  {distance}')


def deleteProofView(listProof):

    if listProof.curselection() == ():
        return messagebox.showerror("Remover Prova", "Tem de selecionar uma prova!")

    else:
        checkDelete = messagebox.askyesno(
            "Remover Prova", "Tem a certeza que pretende remover a prova selecionada?")

        if checkDelete == True:
            messagebox.showinfo("Remover Prova", "Prova removida com sucesso!")

            # get the index of the selected line
            index = listProof.curselection()[0]

            # get the proof name
            proofName = listProof.get(index).split("  ")[0]

            listProof.delete(index)
            deleteProof(proofName)

        return False

# -------------------------------------------------------------------CONSULT RACES VIEW-------------------------------------------------------


def consultRacesOption():
    global userIsLogged

    if userIsLogged == False:
        return messagebox.showerror("Consultar Corridas", "Tem de fazer login para aceder a esta funcionalidade!")
    else:
        consultRacesView()


def consultRacesView():

    global allProofs
    global myProofs
    global fiveKproofs
    global tenKproofs
    global twentyOneKproofs
    global trailProofs
    global searchImage
    global ascImage
    global descImage
    global userLogged

    allProofs.set(1)
    myProofs.set(0)
    fiveKproofs.set(0)
    tenKproofs.set(0)
    twentyOneKproofs.set(0)
    trailProofs.set(0)

    containerRacesView = tk.Frame(Window, width=980, height=600)
    containerRacesView.place(x=220, y=100)

    allProofOpt = tk.Checkbutton(
        containerRacesView, text="Todas as provas", variable=allProofs, onvalue=1, offvalue=0)
    allProofOpt.place(x=50, y=30)

    myProofOpt = tk.Checkbutton(
        containerRacesView, text="As minhas provas", variable=myProofs, onvalue=1, offvalue=0)
    myProofOpt.place(x=50, y=60)

    fiveKproofOpt = tk.Checkbutton(
        containerRacesView, text="5K", variable=fiveKproofs, onvalue=1, offvalue=0)
    fiveKproofOpt.place(x=50, y=90)

    tenKproofOpt = tk.Checkbutton(
        containerRacesView, text="10K", variable=tenKproofs, onvalue=1, offvalue=0)
    tenKproofOpt.place(x=50, y=120)

    twentyOneKproofOpt = tk.Checkbutton(
        containerRacesView, text="21K", variable=twentyOneKproofs, onvalue=1, offvalue=0)
    twentyOneKproofOpt.place(x=50, y=150)

    trailProofOpt = tk.Checkbutton(
        containerRacesView, text="Caminhada", variable=trailProofs, onvalue=1, offvalue=0)
    trailProofOpt.place(x=50, y=180)

    treeviewProofs = ttk.Treeview(containerRacesView, columns=(
        "Prova", "Data", "Local", "Distância"), show="headings", height=13)
    treeviewProofs.place(x=200, y=20)

    treeviewProofs.heading("Prova", text="Prova")
    treeviewProofs.heading("Data", text="Data")
    treeviewProofs.heading("Local", text="Local")
    treeviewProofs.heading("Distância", text="Distância")

    treeviewProofs.column("Prova", width=200)
    treeviewProofs.column("Data", width=140)
    treeviewProofs.column("Local", width=200)
    treeviewProofs.column("Distância", width=100)

    # scrollbar vertical
    scrollbar = tk.Scrollbar(containerRacesView, orient="vertical")
    scrollbar.config(command=treeviewProofs.yview)

    scrollbar.place(x=830, y=20, height=300)

    allRaces = showAllRaces()

    for i in allRaces:
        treeviewProofs.insert("", tk.END, values=(
            i["name"], i["date"], i["local"], i["distance"]))

    searchImage.subsample(1, 1)
    ascImage.subsample(1, 1)
    descImage.subsample(1, 1)

    btnSearch = tk.Button(containerRacesView, width=70, height=62,
                          image=searchImage, compound="center", bd=0, cursor="hand2")
    btnSearch.place(x=880, y=20)

    btnAsc = tk.Button(containerRacesView, width=70, height=62,
                       image=ascImage, compound="center", bd=0, cursor="hand2")
    btnAsc.place(x=880, y=140)

    btnDesc = tk.Button(containerRacesView, width=70, height=62,
                        image=descImage, compound="center", bd=0, cursor="hand2")
    btnDesc.place(x=880, y=260)

    labelProofs = tk.Label(
        containerRacesView, text="Nº de provas:", font=("Arial", 12))
    labelProofs.place(x=160, y=360)

    entryProofs = tk.Entry(containerRacesView, width=8,
                           font=("Arial", 12))
    entryProofs.place(x=270, y=360)
    entryProofs.insert(0, len(allRaces))
    entryProofs.config(state="readonly")

    btnSearch.config(command=lambda: searchProof(entryProofs, treeviewProofs, allProofs,
                     myProofs, fiveKproofs, tenKproofs, twentyOneKproofs, trailProofs))

    btnAsc.config(command=lambda: ascSort(
        treeviewProofs))

    btnDesc.config(command=lambda: descSort(
        treeviewProofs))

    def searchProof(entryProofs, treeProofs, allOption, myOption, fiveKOption, tenKOption, twentyOneKOption, trailOption):

        global countProof

        if allOption.get() == 0 and myOption.get() == 0 and fiveKOption.get() == 0 and tenKOption.get() == 0 and twentyOneKOption.get() == 0 and trailOption.get() == 0:
            return messagebox.showerror("Pesquisar Provas", "Selecione pelo menos uma opção!")

        if allOption.get() == 1 and myOption.get() == 1:
            if fiveKOption.get() == 1 or tenKOption.get() == 1 or twentyOneKOption.get() == 1 or trailOption.get() == 1 or allOption.get() == 1 or myOption.get() == 1:
                return messagebox.showerror("Pesquisar Provas", "Pode apenas visualizar as suas provas ou todas!")

        elif allOption.get() == 1 and myOption.get() == 0 and fiveKOption.get() == 0 and tenKOption.get() == 0 and twentyOneKOption.get() == 0 and trailOption.get() == 0:

            allProofs_ = showAllRaces()

            treeProofs.delete(*treeProofs.get_children())

            for i in allProofs_:
                treeProofs.insert("", tk.END, values=(
                    i["name"], i["date"], i["local"], i["distance"]))

            countProof = len(allProofs_)

            entryProofs.config(state="normal")
            entryProofs.delete(0, tk.END)
            entryProofs.insert(0, countProof)
            entryProofs.config(state="readonly")

        elif allOption.get() == 0 and myOption.get() == 1 and fiveKOption.get() == 0 and tenKOption.get() == 0 and twentyOneKOption.get() == 0 and trailOption.get() == 0:
            treeProofs.delete(*treeProofs.get_children())

            myProofs_ = displayRaces(userLogged)

            for i in myProofs_:
                treeProofs.insert("", tk.END, values=(
                    i["name"], i["date"], i["local"], i["distance"]))

            countProof = len(myProofs_)

            entryProofs.config(state="normal")
            entryProofs.delete(0, tk.END)
            entryProofs.insert(0, countProof)
            entryProofs.config(state="readonly")

        elif allOption.get() == 1 and myOption.get() == 0 and fiveKOption.get() == 1 and tenKOption.get() == 0 and twentyOneKOption.get() == 0 and trailOption.get() == 0:

            fiveK = filterProofs("5K")

            treeProofs.delete(*treeProofs.get_children())

            for i in fiveK:
                treeProofs.insert("", tk.END, values=(
                    i["name"], i["date"], i["local"], i["distance"]))

            countProof = len(fiveK)

            entryProofs.config(state="normal")
            entryProofs.delete(0, tk.END)
            entryProofs.insert(0, countProof)
            entryProofs.config(state="readonly")

        elif allOption.get() == 1 and myOption.get() == 0 and fiveKOption.get() == 0 and tenKOption.get() == 1 and twentyOneKOption.get() == 0 and trailOption.get() == 0:

            tenK = filterProofs("10K")

            treeProofs.delete(*treeProofs.get_children())

            for i in tenK:
                treeProofs.insert("", tk.END, values=(
                    i["name"], i["date"], i["local"], i["distance"]))

            countProof = len(tenK)

            entryProofs.config(state="normal")
            entryProofs.delete(0, tk.END)
            entryProofs.insert(0, countProof)
            entryProofs.config(state="readonly")

        elif allOption.get() == 1 and myOption.get() == 0 and fiveKOption.get() == 0 and tenKOption.get() == 0 and twentyOneKOption.get() == 1 and trailOption.get() == 0:

            twentyOneK = filterProofs("21K")

            treeProofs.delete(*treeProofs.get_children())

            for i in twentyOneK:
                treeProofs.insert("", tk.END, values=(
                    i["name"], i["date"], i["local"], i["distance"]))

            countProof = len(twentyOneK)

            entryProofs.config(state="normal")
            entryProofs.delete(0, tk.END)
            entryProofs.insert(0, countProof)
            entryProofs.config(state="readonly")

        elif allOption.get() == 1 and myOption.get() == 0 and fiveKOption.get() == 0 and tenKOption.get() == 0 and twentyOneKOption.get() == 0 and trailOption.get() == 1:

            trails = filterProofs("Caminhada")

            treeProofs.delete(*treeProofs.get_children())

            for i in trails:
                treeProofs.insert("", tk.END, values=(
                    i["name"], i["date"], i["local"], i["distance"]))

            countProof = len(trails)

            entryProofs.config(state="normal")
            entryProofs.delete(0, tk.END)
            entryProofs.insert(0, countProof)
            entryProofs.config(state="readonly")

        elif allOption.get() == 0 and myOption.get() == 1 and fiveKOption.get() == 1 and tenKOption.get() == 0 and twentyOneKOption.get() == 0 and trailOption.get() == 0:

            MyfiveK = filterLoggedUserProofs("5K", userLogged)

            treeProofs.delete(*treeProofs.get_children())

            for i in MyfiveK:
                treeProofs.insert("", tk.END, values=(
                    i["name"], i["date"], i["local"], i["distance"]))

            countProof = len(MyfiveK)

            entryProofs.config(state="normal")
            entryProofs.delete(0, tk.END)
            entryProofs.insert(0, countProof)
            entryProofs.config(state="readonly")

        elif allOption.get() == 0 and myOption.get() == 1 and fiveKOption.get() == 0 and tenKOption.get() == 1 and twentyOneKOption.get() == 0 and trailOption.get() == 0:

            MytenK = filterLoggedUserProofs("10K", userLogged)

            treeProofs.delete(*treeProofs.get_children())

            for i in MytenK:
                treeProofs.insert("", tk.END, values=(
                    i["name"], i["date"], i["local"], i["distance"]))

            countProof = len(MytenK)

            entryProofs.config(state="normal")
            entryProofs.delete(0, tk.END)
            entryProofs.insert(0, countProof)
            entryProofs.config(state="readonly")

        elif allOption.get() == 0 and myOption.get() == 1 and fiveKOption.get() == 0 and tenKOption.get() == 0 and twentyOneKOption.get() == 21 and trailOption.get() == 0:

            MytwentyOneK = filterLoggedUserProofs("21K", userLogged)

            treeProofs.delete(*treeProofs.get_children())

            for i in MytwentyOneK:
                treeProofs.insert("", tk.END, values=(
                    i["name"], i["date"], i["local"], i["distance"]))

            countProof = len(MytwentyOneK)

            entryProofs.config(state="normal")
            entryProofs.delete(0, tk.END)
            entryProofs.insert(0, countProof)
            entryProofs.config(state="readonly")

        elif allOption.get() == 0 and myOption.get() == 1 and fiveKOption.get() == 0 and tenKOption.get() == 0 and twentyOneKOption.get() == 0 and trailOption.get() == 1:

            Mytrails = filterLoggedUserProofs("Caminhada", userLogged)

            treeProofs.delete(*treeProofs.get_children())

            for i in Mytrails:
                treeProofs.insert("", tk.END, values=(
                    i["name"], i["date"], i["local"], i["distance"]))

            countProof = len(Mytrails)

            entryProofs.config(state="normal")
            entryProofs.delete(0, tk.END)
            entryProofs.insert(0, countProof)
            entryProofs.config(state="readonly")


def ascSort(treeviewProofs):

    Proofs = []

    for i in treeviewProofs.get_children():
        Proofs.append(treeviewProofs.item(i)["values"])

    # sort the list by the second element of the tuple
    Proofs.sort(key=lambda x: x[0])

    # delete the treeview
    treeviewProofs.delete(*treeviewProofs.get_children())

    # insert the sorted list
    for i in Proofs:
        treeviewProofs.insert("", tk.END, values=(
            i[0], i[1], i[2], i[3]))


def descSort(treeviewProofs):

    Proofs = []

    for i in treeviewProofs.get_children():
        Proofs.append(treeviewProofs.item(i)["values"])

    # descending order by the first element of the tuple
    Proofs.sort(key=lambda x: x[0], reverse=True)

    # delete the treeview
    treeviewProofs.delete(*treeviewProofs.get_children())

    # insert the sorted list
    for i in Proofs:
        treeviewProofs.insert("", tk.END, values=(
            i[0], i[1], i[2], i[3]))

# ----------------------------------------------------------------------EXIT APP VIEW   -------------------------------------------------------


def exitApp():
    checkExit = messagebox.askyesno(
        "Sair", "Tem a certeza que pretende sair da aplicação?")

    if checkExit == True:
        Window.destroy()

    return False


# ------------------------------------------------------------------------------------------------------------------------------------------
btnLogin.config(command=loginView)
btnCreateAccount.config(command=RegisterView)
btnManageRaces.config(command=manageRacesOption)
btnConsultRaces.config(command=consultRacesOption)
btnExitApp.config(command=lambda: exitApp())

Window.mainloop()
