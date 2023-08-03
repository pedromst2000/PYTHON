import tkinter as tk
import random
import os
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import time

window = tk.Tk()
window.title("Adivinha o País")
window.geometry("1000x500")


container1 = tk.Frame(window, relief="sunken",
                      borderwidth=5, width=500, height=200)
container1.place(x=480, y=100, anchor="center")


# label 'Nome do País' para adicionar o país
label = tk.Label(window, text="Nome do País", font=("Arial", 12))
label.place(x=380, y=50, anchor="center")

# input ao lado do label 'Nome do País'
input = tk.Entry(window, width=20)
input.place(x=520, y=50, anchor="center")


# botão 'Adicionar'
buttonAdd = tk.Button(window, text="Adicionar", width=10,
                      height=3, relief="raised", borderwidth=5)
buttonAdd.place(x=520, y=120, anchor="center")

container2 = tk.Frame(window, relief="sunken",
                      borderwidth=5, width=870, height=240)
container2.place(x=70, y=220)

# botão 'Selecionar Ficheiro'
buttonSelect = tk.Button(container2, text="Selecionar Ficheiro", width=20,
                         height=3, relief="raised", borderwidth=5)
buttonSelect.place(x=10, y=10)

# label 'Tema'
labelTema = tk.Label(container2, text="Tema", font=("Arial", 12))
labelTema.place(x=10, y=140)

# input ao lado do label 'Tema'
inputTema = tk.Entry(container2, width=20)
inputTema.place(x=90, y=145)

# botão '>'
buttonRight = tk.Button(container2, text=">", width=5,
                        height=10, relief="raised", borderwidth=5)
buttonRight.place(x=400, y=30)

# listbox  ao lado do botão '>'
listbox = tk.Listbox(container2, width=30, height=12)
listbox.place(x=490, y=15)

def selecionar_ficheiro():
    # se o campo tiver vazio 
    if inputTema.get() == "":
        # abre filedialog para selecionar ficheiro da pasta files com titulo 'Selecione Ficheiro de Texto'
        file = filedialog.askopenfilename( initialdir=os.getcwd() + "/files", title="Selecione Ficheiro de Texto",
                                            filetypes=(("Ficheiros de Texto", "*.txt"), ("Todos os Ficheiros", "*.*")))
        # apresenta o ficheiro selecionado no input 'tema' sem extensão .txt e o caminho do ficheiro
        inputTema.insert(0, file.split("/")[-1].split(".")[0])
        # remove o ficheiro selecionado ao selecionar outro ficheiro
        listbox.delete(0, tk.END)
    # se já existir um ficheiro selecionado atualiza o ficheiro selecionado
    else:
        # abre filedialog para selecionar ficheiro da pasta files com titulo 'Selecione Ficheiro de Texto'
        file = filedialog.askopenfilename( initialdir=os.getcwd() + "/files", title="Selecione Ficheiro de Texto",
                                            filetypes=(("Ficheiros de Texto", "*.txt"), ("Todos os Ficheiros", "*.*")))
        # apresenta o ficheiro selecionado no input 'tema' sem extensão .txt e o caminho do ficheiro
        inputTema.delete(0, tk.END)
        inputTema.insert(0, file.split("/")[-1].split(".")[0])
        # remove o ficheiro selecionado ao selecionar outro ficheiro
        listbox.delete(0, tk.END)

def listar_paises():
    # se não existir o ficheiro selecionado apresenta mensagem de erro
    if not os.path.exists(os.getcwd() + "/files/" + inputTema.get() + ".txt"):
        messagebox.showerror("Selecionar Ficheiro", "selecione um ficheiro")
        return
    
    # apresenta  na listbox os países do ficheiro selecionado
    listbox.delete(0, tk.END)
    file = open(os.getcwd() + "/files/" + inputTema.get() + ".txt", "r", encoding="utf-8")
    for line in file:
        listbox.insert(tk.END, line.strip())
    file.close()


def adicionar_pais():
    if input.get() == "":
        messagebox.showerror("Adicionar países", "insira um país")
        return
    if not os.path.exists(os.getcwd() + "/files/" + inputTema.get() + ".txt"):
        messagebox.showerror("Adicionar países", "selecione um ficheiro")
        return
    # verifica se o país já existe no ficheiro selecionado ou na listbox e apresenta mensagem de erro
    if input.get() in listbox.get(0, tk.END) or input.get() in open(os.getcwd() + "/files/" + inputTema.get() + ".txt", "r", encoding="utf-8").read():
        messagebox.showerror("Adicionar países", "O país já existe no ficheiro")
        return
    # adiciona o país ao ficheiro selecionado e apresenta na listbox
    file = open(os.getcwd() + "/files/" + inputTema.get() + ".txt", "a", encoding="utf-8")
    file.write(input.get() + "\n")
    file.close()
    # percorre a listbox e deixar o país na linha nova da listbox se tiver adjacente a outro país ex:PortugalEspanha
    for i in range(len(listbox.get(0, tk.END))):
        if listbox.get(i) > input.get():
            listbox.insert(i, input.get())
            break
    # se o país for o último da listbox adiciona o país na linha nova da listbox
    if input.get() not in listbox.get(0, tk.END):
        listbox.insert(tk.END, input.get())
    input.delete(0, tk.END)


def adivinhar_pais():
    # remove todos os widgets da janela
    for widget in window.winfo_children():
       widget.destroy()
 
    # label 'tema'
    labelTema = tk.Label(window, text="Tema :", font=("Arial", 12))
    labelTema.place(x=50, y=60)
    # combobox ao lado do label 'tema' 
    comboTema = ttk.Combobox(window, width=20)
    comboTema.place(x=120, y=65)
    # colocar os temas dos ficheiros na combobox
    comboTema["values"] = [file.split(".")[0] for file in os.listdir(os.getcwd() + "/files") if file.endswith(".txt")]

    # botão 'Sortear País'
    buttonSortear = tk.Button(window, text="Sortear País", width=15, height=2, relief="raised", borderwidth=5)
    buttonSortear.place(x=300, y=50)

    # input centrado na janela
    input = tk.Entry(window, width=30, justify="center")
    input.place(x=300, y=150)

    # botão "validar" abaixo do input
    buttonValidar = tk.Button(window, text="Validar", width=15, height=2, relief="raised", borderwidth=5)
    buttonValidar.place(x=300, y=200)

    # container com background branco ao lado do input 
    container = tk.Frame(window, width=200, height=400, bg="white")
    container.place(x=700, y=30)

  
        # se não existir o ficheiro selecionado apresenta mensagem de erro
    if not os.path.exists(os.getcwd() + "/files/" + comboTema.get() + ".txt"):
        messagebox.showerror("Selecione o Tema", "selecione um tema")
        return
    # sortear um país aleatório do ficheiro selecionado
    file = open(os.getcwd() + "/files/" + comboTema.get() + ".txt", "r", encoding="utf-8")
    pais = random.choice(file.readlines()).strip()
    file.close()

        # verificar se o país inserido no input é igual ao país sorteado
    if input.get() == pais:
        messagebox.showinfo("Adivinhar o País", "Parabéns, acertou no país")
        input.delete(0, tk.END)
        # se o país inserido no input for diferente do país sorteado apresenta mensagem de erro
    else:
        messagebox.showerror("Adivinhar o País", "O país não é " + input.get())
        input.delete(0, tk.END)

        # apresenta o país sorteado no container
        labelPais = tk.Label(container, text=pais, font=("Arial", 12), bg="white")
        labelPais.place(x=0, y=0)
        # botão 'Validar' abaixo do país sorteado
        buttonValidar = tk.Button(container, text="Validar", width=15, height=2, relief="raised", borderwidth=5)
        buttonValidar.place(x=0, y=50)

    
# associa o botão 'Selecionar Ficheiro' à função selecionar_ficheiro
buttonSelect.config(command=selecionar_ficheiro)
# associa o botão '>' à função listar_paises
buttonRight.config(command=listar_paises)
# associa o botão 'Adicionar' à função adicionar_pais
buttonAdd.config(command=adicionar_pais)


menu = tk.Menu(window)
window.config(menu=menu)

guess_menu = tk.Menu(menu)

guess_menu.add_command(label="Jogar", command=adivinhar_pais)
menu.add_cascade(label="Adivinhar o País", menu=guess_menu)

window.mainloop()
