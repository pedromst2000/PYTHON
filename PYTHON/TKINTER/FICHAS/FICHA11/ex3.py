import tkinter as tk
import os

# window
window = tk.Tk()

# tamanho da janela
window.geometry("1000x500")

# titulo da janela
window.title("ToDoList")


# container para as tarefas
container = tk.LabelFrame(window, height=600, width=200, relief="sunken", borderwidth=6)
# posicionar o container no canto superior esquerdo
container.grid(row=0, column=0, padx=10, pady=10)
container.place(x=10, y=20)

# incluir uma listbox dentro do container centrado com espacamento de 10px
listbox = tk.Listbox(container, width=50, height=20)
listbox.pack(padx=10, pady=10)


# incluirum container ao lado do container de tarefas
container2 = tk.LabelFrame(window, height=100, width=400, relief="sunken", borderwidth=6)
# posicionar o container ao lado do container de tarefas
container2.grid(row=0, column=1, padx=10, pady=10)
container2.place(x=400, y=20)


# incluir um label dentro do container2
labelTask = tk.Label(container2, text="Tarefa :", fg="blue", font=("Arial", 10))
labelTask.place(x=10, y=20)

# incluir uma caixa de texto ao lado do labelTask
entryTask = tk.Entry(container2, width=45)
entryTask.place(x=70, y=20)

# incluir 3 botões fora do container2 mas abaixo dele
# botão adicionar
buttonAdd = tk.Button(window, text="Adicionar", width=12, height=3, borderwidth=4)
buttonAdd.place(x=400, y=190)

# botão remover
buttonRemove = tk.Button(window, text="Remove", width=12, height=3, borderwidth=4)
buttonRemove.place(x=520, y=190)

# botão clear
buttonClear = tk.Button(window, text="Clear", width=12, height=3, borderwidth=4)
buttonClear.place(x=640, y=190)

# botão Upload Download e Ordenar abaixo dos botões acima
# botão Upload
buttonUpload = tk.Button(window, text="Upload", width=12, height=3, borderwidth=4)
buttonUpload.place(x=400, y=300)

# botão Download
buttonDownload = tk.Button(window, text="Download", width=12, height=3, borderwidth=4)
buttonDownload.place(x=520, y=300)

# botão Ordenar
buttonSort = tk.Button(window, text="Ordenar", width=12, height=3, borderwidth=4)
buttonSort.place(x=640, y=300)


# colocar texto abaixo dos botões acima 'nº DE Tarefas Pendentes', com cor azul
labelPending = tk.Label(window, text="Nº de Tarefas Pendentes:", fg="blue", font=("Arial", 10))
labelPending.place(x=400, y=400)

# colocar uma caixa de texto pequena ao lado do labelPending
entryPending = tk.Entry(window, width=5)
entryPending.place(x=565, y=400)


def adicionar():
    # adicionar tarefa na listbox
    listbox.insert(tk.END, entryTask.get())
    # limpar a caixa de texto
    entryTask.delete(0, tk.END)


def Remove():
    # remove a tarefa selecionada da listbox
    listbox.delete(tk.ANCHOR)


def Clear():
    # remove todas as tarefas da listbox
    listbox.delete(0, tk.END)

def Upload():
    # lê o contéudo do ficheiro tafefas.txt e adiciona na listbox
    if os.path.isfile("tarefas.txt"):
        with open("tarefas.txt", "r") as f:
            for line in f:
                listbox.insert(tk.END, line.strip())


def Download():
    # guarda o contéudo da listbox no ficheiro tarefas.txt (substitui o contéudo)
    with open("tarefas.txt", "w") as f:
        for i in range(listbox.size()):
            f.write(listbox.get(i) + "\n")

def Ordenar():
 # buscar a lista de tarefas da listbox
    tarefas = list(listbox.get(0, tk.END))
    # ordenar a lista de tarefas por ordem alfabética
    sorted(tarefas, reverse=True)



def numeroTarefasPendentes():
    countTasks = 0
    # ao adicionar uma tarefa, incrementar o contador
    if adicionar():
        countTasks += 1
        # atualizar o contador na caixa de texto
        entryPending.insert(0, str(countTasks))
    # ao remover uma tarefa, decrementar o contador
    if Remove():
        countTasks -= 1
        # atualizar o contador na caixa de texto
        entryPending.insert(0, str(countTasks))
    # ao limpar a listbox, colocar o contador a zero
    elif Clear():
        countTasks = 0
        # atualizar o contador na caixa de texto
        entryPending.insert(0, str(countTasks))
    # ao fazer upload, o contador deve ser igual ao número de tarefas na listbox
    elif Upload():
        countTasks = listbox.size()
        # atualizar o contador na caixa de texto
        entryPending.insert(0, str(countTasks))
    # ao fazer download, o contador deve ser igual ao número de tarefas na listbox
    elif Download():
        countTasks = listbox.size()
        # atualizar o contador na caixa de texto
        entryPending.insert(0, str(countTasks))


# associar os botões às funções
buttonAdd.config(command=adicionar)
buttonRemove.config(command=Remove)
buttonClear.config(command=Clear)
buttonUpload.config(command=Upload)
buttonDownload.config(command=Download)
buttonSort.config(command=Ordenar)


numeroTarefasPendentes()
window.mainloop()