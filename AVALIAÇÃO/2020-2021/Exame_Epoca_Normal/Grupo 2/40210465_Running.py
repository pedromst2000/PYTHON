import tkinter as tk
from tkinter import ttk

Window = tk.Tk()
Window.title("Running Tool Management")
Window.geometry("900x500")

# label 'Atividades'
label_atividades = tk.Label(Window, text="Atividades", font=("Arial", 10))
label_atividades.place(x=10, y=10)

# listbox abaixo do label 'Atividades'
listbox_atividades = tk.Listbox(Window, width=20, height=10)
listbox_atividades.place(x=10, y=30)


# botão '>'
button_atividades = tk.Button(Window, text=">", width=5, height=2, relief="groove")
button_atividades.place(x=150, y=70)

# botão '+'
button_add = tk.Button(Window, text="+", width=5, height=2, relief="groove")
button_add.place(x=150, y=120)

# treeview com colunas 'Data''Prova' 'Tempo'
treeview = ttk.Treeview(Window, columns=("Data", "Prova", "Tempo"), show="headings")
treeview.heading("Data", text="Data", anchor=tk.W)
treeview.heading("Prova", text="Prova", anchor=tk.W)
treeview.heading("Tempo", text="Tempo", anchor=tk.W)
treeview.place(x=230, y=30)

container = tk.Frame(Window, relief="groove", width=600, height=80, bd=3)
container.place(x=230, y=280)

# label 'Número de provas'
label_numero_provas = tk.Label(container, text="Número de provas:", font=("Arial", 10))
label_numero_provas.place(x=10, y=10)

entry_numero_provas = tk.Entry(container, width=7)
entry_numero_provas.place(x=150, y=10)

# por defeito a entry_numero_provas tem 0 
entry_numero_provas.insert(tk.END, 0)

label_melhor_tempo = tk.Label(
    container, text="Melhor Tempo:", font=("Arial", 10))
label_melhor_tempo.place(x=360, y=10)

entry_melhor_tempo = tk.Entry(container, width=7)
entry_melhor_tempo.place(x=460, y=10)

# por defeito a entry_melhor_tempo tem 0
entry_melhor_tempo.insert(tk.END, 0)

# label 'Filtrar'
label_filtrar = tk.Label(Window, text="Filtrar", font=("Arial", 10))
label_filtrar.place(x=230, y=370)

container_filtrar = tk.Frame(Window, relief="groove", width=600, height=80, bd=3)
container_filtrar.place(x=230, y=390)

label_prova = tk.Label(container_filtrar, text="Prova:", font=("Arial", 10))
label_prova.place(x=10, y=10)

entry_prova = tk.Entry(container_filtrar, width=26)
entry_prova.place(x=70, y=10)

button_filtrar = tk.Button(container_filtrar, text="Filtrar", width=5, height=1, relief="groove")
button_filtrar.place(x=350, y=10)

# canvas
canvas = tk.Canvas(Window, width=200, height=200, bg="white")
canvas.place(x=10, y=280)

# apresentar no canvas a imagem 'maratona.png' da pasta images
image = tk.PhotoImage(file="images/maratona.png")
canvas.create_image(0, 0, anchor=tk.NW, image=image)
# colocar com as dimensoes do canvas
canvas.image = image


# apresenta as atividades na listbox
def atividades_view():
    # limpa a listbox
    listbox_atividades.delete(0, tk.END)
    # ler o ficheiro atividades.txt da pasta data files
    file = open("files/atividades.txt", "r", encoding="utf-8")
    # ler o ficheiro linha a linha
    for line in file:
        # adicionar a linha à listbox
        listbox_atividades.insert(tk.END, line)
    # fechar o ficheiro
    file.close()

# apresenta as provas da atividade selecionada na treeview
def provas_view():
    # limpar a treeview
    treeview.delete(*treeview.get_children())
    # ler o valor selecionado da listbox ler como string
    atividade = listbox_atividades.get(tk.ACTIVE)
    # apresentar as provas na treeview da atividade selecionada
    file = open("files/tempos.txt", "r", encoding="utf-8")
    # apresenta as provas na treeview
    for line in file:
        data = line.split(";")[0]
        prova = line.split(";")[1]
        tempo = line.split(";")[2]
        atividade_ = line.split(";")[3]
        if atividade == atividade_:
            treeview.insert("", tk.END, values=(data, prova, tempo))

    # fechar o ficheiro
    file.close()

   
# apresenta o numero de provas e o melhor tempo da treeview
def estatisca_provas():
    numProvas = 0
    melhorTempo = 0

    atividade = listbox_atividades.get(tk.ACTIVE)
    # ler o numero de provas da treeview
    for child in treeview.get_children():
        numProvas += 1
    
    entry_numero_provas.delete(0, tk.END)
    # apresentar o numero de provas na entry_numero_provas
    entry_numero_provas.insert(tk.END, numProvas)

    # ler o melhor tempo do ficheiro tempos.txt da atividade selecionada
    file = open("files/tempos.txt", "r", encoding="utf-8")
    # atenção que o tempo é uma string e tem que ser convertido para float
    for line in file:
        data = line.split(";")[0]
        prova = line.split(";")[1]
        tempo = line.split(";")[2]
        atividade_ = line.split(";")[3]
        if atividade == atividade_:
            if float(tempo) > melhorTempo:
                melhorTempo = float(tempo)
            #apresentar o melhor tempo na entry_melhor_tempo
            entry_melhor_tempo.delete(0, tk.END)
            entry_melhor_tempo.insert(tk.END, melhorTempo)
    # fechar o ficheiro
    file.close()


def filtrar_prova():
    # limpar a treeview
    treeview.delete(*treeview.get_children())
    # pesquisar o nome da prova na entry_prova
    prova = entry_prova.get()
    # procurar a prova no ficheiro tempos.txt
    file = open("files/tempos.txt", "r", encoding="utf-8")
    # apresentar as provas na treeview
    for line in file:
        data = line.split(";")[0]
        prova_ = line.split(";")[1]
        tempo = line.split(";")[2]
        atividade = line.split(";")[3]
        if prova == prova_:
            treeview.insert("", tk.END, values=(data, prova, tempo, atividade))

    # fechar o ficheiro
    file.close()

button_atividades.configure(command=provas_view)
button_add.configure(command=estatisca_provas)
button_filtrar.configure(command=filtrar_prova)
atividades_view()
Window.mainloop()