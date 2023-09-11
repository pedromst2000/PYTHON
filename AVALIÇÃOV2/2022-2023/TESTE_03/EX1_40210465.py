# Numero:40210465
# Nome: Pedro Miguel da Silva Teixeira

import tkinter as tk
from tkinter import  PhotoImage, LEFT, SUNKEN, StringVar, messagebox
# combobox
from tkinter.ttk import Combobox, Label, Treeview

Window = tk.Tk()
Window.title("Despesas App")
Window.geometry("500x600")
Window.resizable(0,0)

tipoDespesa = StringVar()
numDespesas = 0
valorTotal  = 0


#panedwindow do Ponto 1
pw1 = tk.PanedWindow(Window, width=480, height=170, relief=SUNKEN)
pw1.place(x=10, y=10)

#panedwindow do Ponto 2
pw2 = tk.PanedWindow(Window, width=480, height=400, relief=SUNKEN)
pw2.place(x=10, y=200)

# label 'Mês de Consulta de Despesas:'
label1 = Label(pw1, text="Mês de Consulta de Despesas:")
label1.place(x=10, y=10)

# combobox do ponto 3
combo = Combobox(pw1, width=22)
combo.place(x=250, y=10)
combo.state(['readonly'])

# labelframe do ponto 4
lf = tk.LabelFrame(pw1, text="Tipo de despesas", width=200, height=110)
lf.place(x=25, y=50)

# radio buttons do ponto 4
rb1 = tk.Radiobutton(lf, text="Dinheiro", variable=tipoDespesa, value="Dinheiro")
rb1.place(x=10, y=5)

rb2 = tk.Radiobutton(lf, text="Credito", variable=tipoDespesa, value="Credito")
rb2.place(x=10, y=35)

rb3 = tk.Radiobutton(lf, text="Todas", variable=tipoDespesa, value="Todas")
rb3.place(x=10, y=65)

# por default o radio button 3 'Todas' fica selecionado
rb3.select()

# button do ponto 5
btnSearch = tk.Button(pw1, text="Consultar", width=180, height=85)
btnSearch.place(x=250, y=60)

# incluir a image da pasta 'images' 'pesquisar.png'
img = PhotoImage(file="images/pesquisar.png")
btnSearch.config(image=img, compound=LEFT)

# treeview do ponto 6
tree = Treeview(pw2, columns=("Descrição", "Valor", "Estado"), show="headings", height=15) 
tree.place(x=10, y=10)

# primeira coluna com width de 220 com texto alinhado a esquerda
tree.column("Descrição", width=220, anchor="w")
tree.heading("Descrição", text="Descrição")

# restantes colunas com width de 120 com texto centrado
tree.column("Valor", width=120, anchor="center")
tree.heading("Valor", text="Valor")
tree.column("Estado", width=120, anchor="center")
tree.heading("Estado", text="Estado")


# labels do ponto 7

# label "Nº de Despesas:"	
label2 = Label(pw2, text="Nº de Despesas:")
label2.place(x=10, y=350)

# label "Valor Total:"
label3 = Label(pw2, text="Valor Total:")
label3.place(x=220, y=350)



def readMouths():
    file = open("files/meses.txt", "r", encoding="utf-8")
    mouths = file.readlines()
    file.close()
    return mouths


def Consultar():
    global numDespesas
    global valorTotal

    tipoDespesaSelecionada = tipoDespesa.get()
    mesSelecionado = combo.get()

    if mesSelecionado == "Janeiro":
        file = open("files/Janeiro.txt", "r", encoding="utf-8")

        # limpar treeview
        tree.delete(*tree.get_children())

        # limpar labels
        label2["text"] = "Nº de Despesas:"
        label3["text"] = "Valor Total:"

        # limpar variaveis
        numDespesas = 0
        valorTotal = 0

        for line in file:
            line = line.strip()
            line = line.split(";")
            if tipoDespesaSelecionada == "Todas":
                tree.insert("", "end", values=(line[0], line[1], line[2]))
                numDespesas += 1
                valorTotal += float(line[1])
            elif tipoDespesaSelecionada == line[2]:
                tree.insert("", "end", values=(line[0], line[1], line[2]))
                numDespesas += 1
                valorTotal += float(line[1])
        file.close()

        # atualizar labels
        label2["text"] += " " + str(numDespesas)
        label3["text"] += " " + str(valorTotal) + "€"

    elif mesSelecionado == "Novembro":

        file = open("files/Novembro.txt", "r", encoding="utf-8")

        # limpar treeview
        tree.delete(*tree.get_children())

        # limpar labels
        label2["text"] = "Nº de Despesas:"
        label3["text"] = "Valor Total:"

        # limpar variaveis
        numDespesas = 0
        valorTotal = 0

        for line in file:
            line = line.strip()
            line = line.split(";")
            if tipoDespesaSelecionada == "Todas":
                tree.insert("", "end", values=(line[0], line[1], line[2]))
                numDespesas += 1
                valorTotal += float(line[1])
            elif tipoDespesaSelecionada == line[2]:
                tree.insert("", "end", values=(line[0], line[1], line[2]))
                numDespesas += 1
                valorTotal += float(line[1])

        file.close()

        # atualizar labels
        label2["text"] += " " + str(numDespesas)
        label3["text"] += " " + str(valorTotal) + "€"

    elif mesSelecionado == "Dezembro":

        file = open("files/Dezembro.txt", "r", encoding="utf-8")

        # limpar treeview
        tree.delete(*tree.get_children())

        # limpar labels
        label2["text"] = "Nº de Despesas:"
        label3["text"] = "Valor Total:"

        # limpar variaveis
        numDespesas = 0
        valorTotal = 0

        for line in file:
            line = line.strip()
            line = line.split(";")
            if tipoDespesaSelecionada == "Todas":
                tree.insert("", "end", values=(line[0], line[1], line[2]))
                numDespesas += 1
                valorTotal += float(line[1])
            elif tipoDespesaSelecionada == line[2]:
                tree.insert("", "end", values=(line[0], line[1], line[2]))
                numDespesas += 1
                valorTotal += float(line[1])

        file.close()

        # atualizar labels
        label2["text"] += " " + str(numDespesas)
        label3["text"] += " " + str(valorTotal) + "€"


    

 

combo["values"] = readMouths()
btnSearch.config(command=Consultar())
Window.mainloop()