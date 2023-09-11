import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import StringVar
# png
# from PIL import ImageTk, Image

# header da interface
window = tk.Tk()
window.title("Despesas App")
# dimensões da janela
window.geometry("500x600")

# PanewdWindow com 480x170, estilo sunken
frame1 = tk.PanedWindow(window, width=480, height=170, relief=tk.SUNKEN)
# posição x=10 y=10
frame1.place(x=10, y=10)

# PanedWindow com 480x400, estilo sunken
frame2 = tk.PanedWindow(window, width=480, height=400, relief=tk.SUNKEN)
# posição x=10 y=200
frame2.place(x=10, y=200)

# label 'Mês de Consulta de Despesas:' no canto superior esquerdo do frame
label = tk.Label(frame1, text="Mês de Consulta de Despesas:")
label.place(x=10, y=10)

# Combobox com os meses do ano
mouths = ttk.Combobox(frame1, width=10, height=50)


# abrir o ficheiro 'meses.txt' e ler os meses para a combobox.
with open('./files/meses.txt', 'r') as file:
    # ler os meses do ficheiro
    mouths['values'] = file.read().splitlines()
    # colocar cada mês na combobox
    mouths.current(0)
    # apresentar por defeito a vazio na combobox
    mouths.set('')

# posição x=250 y=10
mouths.place(x=250, y=10)

# labelFrame 200x110 com título 'Tipo de Despesasa'
frame3 = tk.LabelFrame(frame1, width=200, height=110, text="Tipo de Despesa")
# posição x=25 y=50
frame3.place(x=25, y=50)

selected = StringVar()

# 3 radiobuttons com os tipos de despesa
# radiobutton 'Dinheiro'
radio1 = tk.Radiobutton(frame3, text="Dinheiro", variable=selected, value="Dinheiro")
radio1.place(x=10, y=5)
# radiobutton 'Credito'
radio2 = tk.Radiobutton(frame3, text="Credito", variable=selected, value="Credito")
radio2.place(x=10, y=35)
# radiobutton 'Todas'
radio3 = tk.Radiobutton(frame3, text="Todas", variable=selected, value="Todas")
# posição x=10 y=70
radio3.place(x=10, y=65)

# seleciona por defeito o radiobutton 'Todas'
selected.set("Todas")

# botão 'Consultar' com cor preta
button = tk.Button(frame1, text="Consultar", fg="black", width=7, height=5)
# posição x=350 y=50
button.place(x=250, y=50)

# treeview com colunas 'Descrição', 'Valor' e 'Estado'
tree = ttk.Treeview(frame2, columns=('Descrição', 'Valor', 'Estado'), show='headings')
# posição x=10 y=10
tree.place(x=10, y=10)

# header da coluna 'Descrição'
tree.heading('#1', text='Descrição')
# header da coluna 'Valor'
tree.heading('#2', text='Valor')
# header da coluna 'Estado'
tree.heading('#3', text='Estado')
# colocar o heading 'Estado' centrado
tree.column('#3', anchor=tk.CENTER)

# coluna 'Descrição' com comprimento de 220 om texto alinhado à esquerda
tree.column('#1', width=220, anchor=tk.W)
# restantes colunas com comprimento de 120 com texto centrado
tree.column('#2', width=120, anchor=tk.CENTER)

# altura da treeview de 15 linhas
tree['height'] = 15

# label 'Nº de Despesas:' abaixo da treeview no canto inferior esquerdo
labelDespesas = tk.Label(frame2, text="Nº de Despesas:")
# posição x=10 y=380
labelDespesas.place(x=10, y=380)

# label 'valor Total:' com texto preto abaixo da treeview
labelTotal = tk.Label(window, text="Valor Total:", fg="black")
# posição x=10 y=410
labelTotal.place(x=270, y=580)


def consultar():
    # buscar o mês selecionado na combobox
    mes = mouths.get()
    print(f'Mês selecionado: {mes}')
    # buscar o tipo de despesa selecionado nos radiobuttons
    tipo = selected.get()
    
    numDespesas = 0
    valorTotal = 0
    # limpar a treeview
    tree.delete(*tree.get_children())
    # se o mês selecionado for janeiro ler as depesas do ficheiro 'janeiro.txt'
    if mes == "Janeiro":
        with open('./files/Janeiro.txt', 'r', encoding="utf-8") as file:
            # ler as despesas do ficheiro
            for line in file:
                # separar a linha em 3 partes
                descricao, valor, estado = line.split(";")
                # se o tipo de despesa selecionado for 'Todas' ou se o tipo de despesa selecionado for igual ao estado da despesa
                if tipo == "Todas" or tipo == estado.strip():
                    # inserir na treeview a descrição, o valor e o estado da despesa
                    tree.insert('', 'end', values=(descricao, valor, estado.strip()))
                    # incrementar o número de despesas
                    numDespesas += 1
                    # incrementar o valor total
                    valorTotal += float(valor)
    elif mes == "Dezembro":
        with open('./files/Dezembro.txt', 'r', encoding="utf-8") as file:
            # ler as despesas do ficheiro
            for line in file:
                # separar a linha em 3 partes
                descricao, valor, estado = line.split(";")
                # se o tipo de despesa selecionado for 'Todas' ou se o tipo de despesa selecionado for igual ao estado da despesa
                if tipo == "Todas" or tipo == estado.strip():
                    # inserir na treeview a descrição, o valor e o estado da despesa
                    tree.insert('', 'end', values=(descricao, valor, estado.strip()))
                    # incrementar o número de despesas
                    numDespesas += 1
                    # incrementar o valor total
                    valorTotal += float(valor)
    elif mes == "Novembro":
        with open('./files/Novembro.txt', 'r', encoding="utf-8") as file:
            # ler as despesas do ficheiro
            for line in file:
                # separar a linha em 3 partes
                descricao, valor, estado = line.split(";")
                # se o tipo de despesa selecionado for 'Todas' ou se o tipo de despesa selecionado for igual ao estado da despesa
                if tipo == "Todas" or tipo == estado.strip():
                    # inserir na treeview a descrição, o valor e o estado da despesa
                    tree.insert('', 'end', values=(descricao, valor, estado.strip()))
                    # incrementar o número de despesas
                    numDespesas += 1
                    # incrementar o valor total
                    valorTotal += float(valor)    

    # atualizar o label 'Nº de Despesas:' com o número de despesas
    labelDespesas['text'] = "Nº de Despesas: " + str(numDespesas)
    # atualizar o label 'valor Total:' com o valor total
    labelTotal['text'] = "Valor Total: " + str(valorTotal) + "€"

    # se não tiver um mês selecionado
    if mes == '':
        # mostrar mensagem de erro
        messagebox.showerror("Erro", "Não selecionou um mês!")
        # atualizar o label 'Nº de Despesas:' com o número de despesas
        labelDespesas['text'] = "Nº de Despesas: " + str(numDespesas)
        # atualizar o label 'valor Total:' com o valor total
        labelTotal['text'] = "Valor Total: " + str(valorTotal) + "€"

    # se não existirem despesas
    elif numDespesas == 0:
        # mostrar mensagem de erro
        messagebox.showerror("Erro", "Não existem despesas para o mês selecionado!")
        # atualizar o label 'Nº de Despesas:' com o número de despesas
        labelDespesas['text'] = "Nº de Despesas: " + str(numDespesas)
        # atualizar o label 'valor Total:' com o valor total
        labelTotal['text'] = "Valor Total: " + str(valorTotal) + "€"

#  associar a função consultar() ao botão 'Consultar'
button.config(command=consultar)

window.mainloop()