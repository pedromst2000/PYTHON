import tkinter as tk
from tkinter import filedialog
from tkinter import IntVar


Window = tk.Tk()
Window.title("Setup")
Window.geometry("700x500")

container1 = tk.Frame(Window, width=250, height=480,
                      relief="sunken", borderwidth=2)
container1.place(x=10, y=10)

# label 'As minhas Provas'
label1 = tk.Label(container1, text="As minhas Provas",
                  font=("Arial", 10, "bold"))
label1.place(x=60, y=10)

label2 = tk.Label(container1, text="Logotipo da prova", font=("Arial", 9))
label2.place(x=20, y=40)

button1 = tk.Button(container1, text="Selecionar", font=(
    "Arial", 9), relief="raised", borderwidth=2)
button1.place(x=150, y=40)

canvas1 = tk.Canvas(container1, width=200, height=300,
                    relief="sunken", borderwidth=2)
canvas1.place(x=20, y=90)

# renderizar no canvas a imagem do file setup.txt
f = open("files/setup.txt", "r")
filename = f.read()
f.close()
canvas1.image = tk.PhotoImage(file=filename)
canvas1.create_image(0, 0, anchor="nw", image=canvas1.image)

button2 = tk.Button(container1, text="Guardar", font=(
    "Arial", 9), relief="raised", borderwidth=2, width=10)
button2.place(x=20, y=400)

container2 = tk.Frame(Window, width=400, height=480,
                      relief="sunken", borderwidth=2)
container2.place(x=270, y=10)

label3 = tk.Label(container2, text="As minhas notificações",
                  font=("Arial", 10, "bold"))
label3.place(x=120, y=10)

container3 = tk.Frame(container2, width=380, height=100,
                      relief="sunken", borderwidth=2)
container3.place(x=10, y=40)

label4 = tk.Label(container3, text="Ver notificações de:", font=("Arial", 9))
label4.place(x=10, y=10)

checkVar1 = IntVar()
checkVar2 = IntVar()
checkVar3 = IntVar()

check1 = tk.Checkbutton(container3, text="5K",
                        font=("Arial", 9), variable=checkVar1)
check1.place(x=10, y=40)

check2 = tk.Checkbutton(container3, text="10K",
                        font=("Arial", 9), variable=checkVar2)
check2.place(x=100, y=40)

check3 = tk.Checkbutton(container3, text="21K",
                        font=("Arial", 9), variable=checkVar3)
check3.place(x=190, y=40)

button3 = tk.Button(container2, text="Ver", font=(
    "Arial", 9), relief="raised", borderwidth=2, width=10)
button3.place(x=10, y=150)


# listbox abaixo do botão 'Ver'
listbox1 = tk.Listbox(container2, width=90, height=40,
                      relief="sunken", borderwidth=2)
listbox1.place(x=10, y=190)

# para selecionar o logotipo


def selecionar_logo():
    # abrir na pasta images para selecionar o logotipo
    filename = filedialog.askopenfilename(initialdir="images", title="Selecione o logotipo", filetypes=(
        ("png files", "*.png"), ("all files", "*.*")))
    # colocar a imagem selecionada no canvas
    canvas1.image = tk.PhotoImage(file=filename)
    canvas1.create_image(0, 0, anchor="nw", image=canvas1.image)


# guarda a imagem
def guardar_logo():
    # abrir o ficheiro setup.txt em modo de escrita
    f = open("files/setup.txt", "w")
    # guardar o caminho da imagem selecionada no ficheiro setup.txt
    f.write(canvas1.image.cget("file"))
    # fechar o ficheiro
    f.close()


def ver_notificacoes():
    # ler o valor do checkbutton 5K
    if checkVar1.get() == 1:
        # abrir o ficheiro AgendasProvas.txt em modo de leitura
        f = open("files/AgendaProvas.txt", "r")
        # apresentar as provas de 5K no listbox
        for line in f:
            if line.startswith("5K"):
                listbox1.insert(tk.END, line)
        # fechar o ficheiro
        f.close()
    # ler o valor do checkbutton 10K
    if checkVar2.get() == 1:
        # abrir o ficheiro AgendasProvas.txt em modo de leitura
        f = open("files/AgendaProvas.txt", "r")
        # apresentar as provas de 10K no listbox
        for line in f:
            if line.startswith("10K"):
                listbox1.insert(tk.END, line)
        # fechar o ficheiro
        f.close()
    # ler o valor do checkbutton 21K
    if checkVar3.get() == 1:
        f = open("files/AgendaProvas.txt", "r")
        # apresentar as provas de 21K no listbox
        for line in f:
            if line.startswith("21K"):
                listbox1.insert(tk.END, line)
        # fechar o ficheiro
        f.close()


# associar o botão 'Selecionar' à função selecionar_logo
button1.config(command=selecionar_logo)
# associar o botão 'Guardar' à função guardar_logo
button2.config(command=guardar_logo)
# associar o botão 'Ver' à função ver_notificacoes
button3.config(command=ver_notificacoes)
Window.mainloop()
