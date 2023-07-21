import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import IntVar
from tkinter import messagebox

Window = tk.Tk()
Window.title("Trails App")
Window.geometry("1000x500")

checkVar1 = IntVar()
checkVar2 = IntVar()

checkTrailCurto = tk.Checkbutton(
    Window, text="Trail Curto", variable=checkVar1)
checkTrailCurto.place(x=18, y=20)

checkTrailLongo = tk.Checkbutton(
    Window, text="Ultra Trail", variable=checkVar2)
checkTrailLongo.place(x=128, y=20)

# por defeito o checkTrailCurto está selecionado
checkTrailCurto.select()

btnSearch = tk.Button(Window, text="", width=35, height=35)
btnSearch.place(x=280, y=10)

# incluir uma imagem no botão 'pesquisar.png' na pasta imagens
imgSearch = tk.PhotoImage(file="imagens/pesquisar.png")
# reduzir o tamanho da imagem
imgSearch = imgSearch.subsample(12, 12)
# remover a borda do botão
btnSearch.config(bd=0)
btnSearch.config(image=imgSearch, compound=tk.TOP, cursor="hand2")


ascButtonn = tk.Button(Window, text="", width=50, height=80)
ascButtonn.place(x=380, y=-10)

# incluir uma imagem no botão 'asc.png' na pasta imagens
imgAsc = tk.PhotoImage(file="imagens/asc.png")
# aumentar o tamanho da imagem
imgAsc = imgAsc.zoom(1, 1)
ascButtonn.config(bd=0)
ascButtonn.config(image=imgAsc, compound=tk.TOP, cursor="hand2")


descButtonn = tk.Button(Window, text="", width=50, height=80)
descButtonn.place(x=460, y=-10)

imgDesc = tk.PhotoImage(file="imagens/desc.png")
imgDesc = imgDesc.zoom(1, 1)
descButtonn.config(bd=0)
descButtonn.config(image=imgDesc, compound=tk.TOP, cursor="hand2")


# treeview com três colunas 'Prova' 'Data' 'Local' abaixo das checkboxes
tree = ttk.Treeview(Window, columns=(
    "Prova", "Data", "Local"), show="headings")
tree.heading("Prova", text="Prova", anchor=tk.CENTER)
tree.heading("Data", text="Data", anchor=tk.CENTER)
tree.column("Prova", width=300)
tree.column("Data", width=100)
tree.heading("Local", text="Local", anchor=tk.CENTER)
tree.place(x=18, y=60)

# texto da 'prova' alinhado a esquerda
tree.column("Prova", anchor=tk.W)
# texto da coluna 'data' e 'local' alinhado ao centro
tree.column("Data", anchor=tk.CENTER)
tree.column("Local", anchor=tk.CENTER)

# label 'Nº de provas'
labelNumProvas = tk.Label(Window, text="Nº de provas", fg="black")
labelNumProvas.place(x=38, y=300)

# entry 'Nº de provas'
entryNumProvas = tk.Entry(Window, width=10)
entryNumProvas.place(x=120, y=300)

# Botão 'Selecionar Imagem'
btnSelecionarImagem = tk.Button(
    Window, text="Selecionar Imagem", width=20, height=2)
btnSelecionarImagem.place(x=88, y=400)

# canvas
canvas = tk.Canvas(Window, width=350, height=170,
                   relief="sunken", borderwidth=1)
canvas.place(x=268, y=300)


# botão 'Adicionar Favoritos'
btnAdicionarFavoritos = tk.Button(
    Window, text="Adicionar Favoritos", width=15, height=3)
btnAdicionarFavoritos.place(x=638, y=120)

# botão 'Remover Favoritos'
btnRemoverFavoritos = tk.Button(
    Window, text="Remover Favoritos", width=15, height=3)
btnRemoverFavoritos.place(x=638, y=180)

# container
container = tk.Frame(Window, width=240, height=900,
                     relief="sunken", borderwidth=3)
container.place(x=760, y=10)

# label 'Favoritos'com letra Helvetica, tamanho 11
labelFavoritos = tk.Label(container, text="Favoritos",
                          font=("Helvetica", 11), fg="black")
labelFavoritos.place(x=100, y=10)

# listbox
listboxFavoritos = tk.Listbox(container, width=33, height=20)
listboxFavoritos.place(x=15, y=40)

# Botão 'Guardar Favoritos'
btnGuardarFavoritos = tk.Button(
    container, text="Guardar Favoritos", width=20, height=3)
btnGuardarFavoritos.place(x=55, y=400)


def trailView():
    # limpar a treeview
    tree.delete(*tree.get_children())
    # ler o checkbutton selecionado
    checkTrailCurtoState = checkVar1.get()
    checkTrailLongoState = checkVar2.get()

    if checkTrailCurtoState == 1:
        # le o conteúdo do ficheiro 'trails.txt' e separar por ';'
        file = open("ficheiros/trails.txt", "r", encoding="utf-8")
        for line in file:
            prova, data, local = line.split(";")
            # inserir os dados na treeview
            tree.insert("", tk.END, values=(prova, data, local))
        file.close()
    if checkTrailLongoState == 1:
        # ler o conteúdo do ficheiro 'ultratrails.txt' e separar por ';' dar espaços entre palavras
        file = open("ficheiros/ultratrails.txt", "r", encoding="utf-8")
        for line in file:
            prova, data, local = line.split(";")
            # dar espaços entre palavras
            prova = prova.replace(" ", " ")
            # inserir os dados na treeview
            tree.insert("", tk.END, values=(prova, data, local))
        file.close()

    if checkTrailCurtoState == 1 and checkTrailLongoState == 1:
        # apresenta os dados dos dois ficheiros
        file = open("ficheiros/trails.txt", "r", encoding="utf-8")
        for line in file:
            prova, data, local = line.split(";")
            tree.insert("", tk.END, values=(prova, data, local))
        file.close()
        file = open("ficheiros/ultratrails.txt", "r", encoding="utf-8")
        for line in file:
            prova, data, local = line.split(";")
            prova = prova.replace(" ", " ")
            tree.insert("", tk.END, values=(prova, data, local))
        file.close()

    if checkTrailCurtoState == 0 and checkTrailLongoState == 0:
        messagebox.showerror("Erro", "Selecione o tipo de prova")


def ascView():
    # ordenar a treeview por ordem ascendente por local da prova
    tree.delete(*tree.get_children())
    checkTrailCurtoState = checkVar1.get()
    checkTrailLongoState = checkVar2.get()

    if checkTrailCurtoState == 1:
        file = open("ficheiros/trails.txt", "r", encoding="utf-8")
        # ordenar a treeview por ordem ascendente por local da prova
        for line in sorted(file):
            prova, data, local = line.split(";")
            tree.insert("", tk.END, values=(prova, data, local))
        file.close()
    if checkTrailLongoState == 1:
        file = open("ficheiros/ultratrails.txt", "r", encoding="utf-8")
        for line in sorted(file):
            prova, data, local = line.split(";")
            prova = prova.replace(" ", " ")
            tree.insert("", tk.END, values=(prova, data, local))
        file.close()

    if checkTrailCurtoState == 1 and checkTrailLongoState == 1:
        file = open("ficheiros/trails.txt", "r", encoding="utf-8")
        for line in sorted(file):
            prova, data, local = line.split(";")
            tree.insert("", tk.END, values=(prova, data, local))
        file.close()
        file = open("ficheiros/ultratrails.txt", "r", encoding="utf-8")
        for line in sorted(file):
            prova, data, local = line.split(";")
            prova = prova.replace(" ", " ")
            tree.insert("", tk.END, values=(prova, data, local))
        file.close()

    if checkTrailCurtoState == 0 and checkTrailLongoState == 0:
        messagebox.showerror("Erro", "Selecione o tipo de prova")


def descView():
    # ordena a treeview por ordem descendente por local da prova
    tree.delete(*tree.get_children())
    checkTrailCurtoState = checkVar1.get()
    checkTrailLongoState = checkVar2.get()

    if checkTrailCurtoState == 1:

        file = open("ficheiros/trails.txt", "r", encoding="utf-8")
        # ordenar a treeview por ordem descendente por local da prova
        for line in sorted(file, reverse=True):
            prova, data, local = line.split(";")
            tree.insert("", tk.END, values=(prova, data, local))
        file.close()
    if checkTrailLongoState == 1:

        file = open("ficheiros/ultratrails.txt", "r", encoding="utf-8")
        for line in sorted(file, reverse=True):
            prova, data, local = line.split(";")
            prova = prova.replace(" ", " ")
            tree.insert("", tk.END, values=(prova, data, local))
        file.close()

    if checkTrailCurtoState == 1 and checkTrailLongoState == 1:
        file = open("ficheiros/trails.txt", "r", encoding="utf-8")
        for line in sorted(file, reverse=True):
            prova, data, local = line.split(";")
            tree.insert("", tk.END, values=(prova, data, local))
        file.close()
        file = open("ficheiros/ultratrails.txt", "r", encoding="utf-8")
        for line in sorted(file, reverse=True):
            prova, data, local = line.split(";")
            prova = prova.replace(" ", " ")
            tree.insert("", tk.END, values=(prova, data, local))
        file.close()

    if checkTrailCurtoState == 0 and checkTrailLongoState == 0:
        messagebox.showerror("Erro", "Selecione o tipo de prova")


def numProvas():
    # apresenta o numero de provas da treeview
    checkTrailCurtoState = checkVar1.get()
    checkTrailLongoState = checkVar2.get()
    if checkTrailCurtoState == 1:
        # apresenta o numero de provas da treeview na entry 'numProvas'
        file = open("ficheiros/trails.txt", "r", encoding="utf-8")
        numProvas = len(file.readlines())

        entryNumProvas.delete(0, tk.END)
        entryNumProvas.insert(0, numProvas)
        file.close()
    
    if checkTrailLongoState == 1:
        file = open("ficheiros/ultratrails.txt", "r", encoding="utf-8")
        numProvas = len(file.readlines())

        entryNumProvas.delete(0, tk.END)
        entryNumProvas.insert(0, numProvas)
        file.close()
    
    if checkTrailCurtoState == 1 and checkTrailLongoState == 1:
        file = open("ficheiros/trails.txt", "r", encoding="utf-8")
        numProvas = len(file.readlines())
        file.close()
        file = open("ficheiros/ultratrails.txt", "r", encoding="utf-8")
        numProvas += len(file.readlines())
        file.close()

        entryNumProvas.delete(0, tk.END)
        entryNumProvas.insert(0, numProvas)

    if checkTrailCurtoState == 0 and checkTrailLongoState == 0:
        messagebox.showerror("Erro", "Selecione o tipo de prova")


def addFav():
    # adiciona a prova selecionada da treeview à lista de favoritos
    checkTrailCurtoState = checkVar1.get()
    checkTrailLongoState = checkVar2.get()

    if checkTrailCurtoState == 1:
        prova = tree.item(tree.selection())['values'][0]
        file = open("ficheiros/favoritos.txt", "a", encoding="utf-8")
        file.write(prova + "\n")
        messagebox.showinfo("Info", "Prova adicionada aos favoritos")
        listboxFavoritos.insert(tk.END, prova)
        file.close()
    if checkTrailLongoState == 1:
        prova = tree.item(tree.selection())['values'][0]
        file = open("ficheiros/favoritos.txt", "a", encoding="utf-8")
        file.write(prova + "\n")
        messagebox.showinfo("Info", "Prova adicionada aos favoritos")
        listboxFavoritos.insert(tk.END, prova)
        file.close()
    if checkTrailCurtoState == 1 and checkTrailLongoState == 1:
        prova = tree.item(tree.selection())['values'][0]
        file = open("ficheiros/favoritos.txt", "a", encoding="utf-8")
        file.write(prova + "\n")
        messagebox.showinfo("Info", "Prova adicionada aos favoritos")
        listboxFavoritos.insert(tk.END, prova)
        file.close()
    if checkTrailCurtoState == 0 and checkTrailLongoState == 0:
        messagebox.showerror("Erro", "Selecione o tipo de prova")

def guardar_fav():
    # guarda a lista de favoritos no ficheiro 'favoritos.txt'
    # e apresentar a lista de favoritos na aberura da aplicação
    file = open("ficheiros/favoritos.txt", "w", encoding="utf-8")
    for i in listboxFavoritos.get(0, tk.END):
        file.write(i + "\n")
    file.close()


def show_fav():
    # apresenta a lista de favoritos na abertura da aplicação
    file = open("ficheiros/favoritos.txt", "r", encoding="utf-8")
    for line in file:
        listboxFavoritos.insert(tk.END, line.strip())
    file.close()

def remover_fav():
    # remove a prova selecionada da lista de favoritos
    prova = listboxFavoritos.get(listboxFavoritos.curselection())
    listboxFavoritos.delete(listboxFavoritos.curselection())
    file = open("ficheiros/favoritos.txt", "r", encoding="utf-8")
    lines = file.readlines()
    file.close()
    file = open("ficheiros/favoritos.txt", "w", encoding="utf-8")
    for line in lines:
        if line.strip("\n") != prova:
            file.write(line)
    file.close()

def selec_imagem():
        # abre uma janela para selecionar uma imagem no caminho da pasta 'images'
    path = filedialog.askopenfilename(initialdir='imagens')
    # adiciona a imagem selecionada no canvas
    canvas.image = tk.PhotoImage(file=path)
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')
    # imagem com mesmo tamanho do canvas
    canvas.config(width=canvas.image.width(), height=canvas.image.height())


btnSearch.config(command=trailView)
ascButtonn.config(command=ascView)
descButtonn.config(command=descView)
btnAdicionarFavoritos.config(command=addFav)
btnGuardarFavoritos.config(command=guardar_fav)
btnRemoverFavoritos.config(command=remover_fav)
btnSelecionarImagem.config(command=selec_imagem)

show_fav()
guardar_fav()
numProvas()
Window.mainloop()