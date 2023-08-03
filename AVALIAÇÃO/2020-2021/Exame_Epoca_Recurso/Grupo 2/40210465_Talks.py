import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import StringVar
from tkinter import IntVar
from tkinter import filedialog

Window = tk.Tk()
Window.title("WebDev Tech Talks")
Window.geometry("1000x500")

# label 'Nome'
Nome = tk.Label(Window, text="Nome", fg="black", font=("Helvetica", 10))
Nome.place(x=10, y=10)

# caixa de texto 'Nome'
NomeEntry = tk.Entry(Window, width=30)
NomeEntry.place(x=60, y=10)

TipoInscricao = tk.LabelFrame(
    Window, text="Tipo Inscrição", relief='sunken', borderwidth=5)
TipoInscricao.place(x=30, y=60, width=200, height=300)

selected = StringVar()
selected.set("Docente")

# radiobutton 'Docente'
Docente = ttk.Radiobutton(TipoInscricao, text="Docente",
                          value="Docente", variable=selected)
Docente.place(x=10, y=10)

# radiobutton 'Estudante'
Estudante = ttk.Radiobutton(
    TipoInscricao, text="Estudante", value="Estudante", variable=selected)
Estudante.place(x=10, y=40)

# radiobutton 'Externo'
Externo = ttk.Radiobutton(TipoInscricao, text="Externo",
                          value="Externo", variable=selected)
Externo.place(x=10, y=70)

TipoInscricao2 = tk.LabelFrame(Window, relief='sunken', borderwidth=5)
TipoInscricao2.place(x=250, y=60, width=430, height=300)

# treeview com colunas 'Nome' 'Perfil'
tree = ttk.Treeview(TipoInscricao2, columns=(
    'Nome', 'Perfil'), show='headings')
tree.column('Nome', width=200, minwidth=200, stretch=tk.NO)
tree.column('Perfil', width=200, minwidth=200, stretch=tk.NO)
tree.heading('Nome', text='Nome')
tree.heading('Perfil', text='Perfil')
tree.place(x=10, y=10)

# adiciona um scroll ao treeview
tree_scroll = ttk.Scrollbar(
    TipoInscricao2, orient='vertical', command=tree.yview)
tree_scroll.place(x=410, y=10, height=280)

# botão 'Ler Ficheiro'
LerFicheiro = tk.Button(Window, text="Ler Ficheiro",
                        relief='raised', borderwidth=5, width=15, height=2)
LerFicheiro.place(x=30, y=370)

# botão 'Adicionar'
Adicionar = tk.Button(Window, text="Adicionar",
                      relief='raised', borderwidth=5, width=15, height=2)
Adicionar.place(x=180, y=370)

# botão 'Guardar'
Guardar = tk.Button(Window, text="Guardar", relief='raised',
                    borderwidth=5, width=15, height=2)
Guardar.place(x=330, y=370)

# label 'Nº Incrições'
NInscricoes = tk.Label(Window, text="Nº Inscrições",
                       fg="black", font=("Helvetica", 10))
NInscricoes.place(x=480, y=380)

# caixa de texto 'Nº Incrições'
NInscricoesEntry = tk.Entry(Window, width=12)
NInscricoesEntry.place(x=580, y=380)

# disable da caixa de texto 'Nº Incrições'
NInscricoesEntry.config(state='disabled')

# botão 'Selecionar Imagem'
SelecionarImagem = tk.Button(
    Window, text="Selecionar Imagem", relief='raised', borderwidth=5, width=15, height=2)
SelecionarImagem.place(x=700, y=70)

# canvas para a imagem
canvas = tk.Canvas(Window, width=240, height=200,
                   relief='sunken', borderwidth=5)
canvas.place(x=700, y=140)

# botão 'Consulta'
Consulta = tk.Button(Window, text="Consulta", relief='raised',
                     borderwidth=5, width=15, height=4)
Consulta.place(x=760, y=370)


def ler_ficheiro():
    # lê o ficheiro inscritos.txt da pasta files e adiciona a treeview
    tree.delete(*tree.get_children())
    docentes = 0
    estudantes = 0
    externos = 0
    ficheiro = open("files/inscricoes.txt", "r", encoding="utf-8")
    for linha in ficheiro:
        # rstrip() remove o \n do fim da linha
        linha = linha.rstrip()
        nome, perfil = linha.split(";")
        tree.insert("", tk.END, values=(nome, perfil))
    ficheiro.close()
    # apresentar numa mensagem com title 'Informação':
    for i in tree.get_children():
        if tree.item(i)['values'][1] == 'Docente':
            docentes += 1
        elif tree.item(i)['values'][1] == 'Estudante':
            estudantes += 1
        elif tree.item(i)['values'][1] == 'Externo':
            externos += 1
    messagebox.showinfo(
        "Informação", f"{docentes} Docentes, {estudantes} Estudantes e {externos} Externo")
    # apresentar o número de inscrições na caixa de texto 'Nº Incrições'
    NInscricoesEntry.config(state='normal')
    NInscricoesEntry.delete(0, tk.END)
    NInscricoesEntry.insert(0, len(tree.get_children()))


def adicionar():
    # ler o valor do nome
    nome = NomeEntry.get()
    # ler o tipo de inscrição selecionado
    perfil = selected.get()

    if nome == "":
        messagebox.showerror("Impossível adicionar Inscrição",
                             "Não inseriu nome da inscrição")

    else:
        # adicionar o nome e o perfil à treeview
        tree.insert("", tk.END, values=(nome, perfil))


def guardar():
    # guardar o conteudo da treeview no ficheiro inscricoes.txt
    ficheiro = open("files/inscricoes.txt", "w", encoding="utf-8")
    for i in tree.get_children():
        ficheiro.write(tree.item(i)['values'][0] +
                       ";" + tree.item(i)['values'][1] + "\n")
    ficheiro.close()


def selecionar_imagem():
    ficheiro = filedialog.askopenfilename(initialdir="images", title="Selecione a imagem",
                                          filetypes=(("png files", "*.png"), ("jpg files", "*.jpg")))

    # apresenta a imagem selecionada no canvas
    # se o ficheiro não for vazio
    if ficheiro != "":
        imagem = tk.PhotoImage(file=ficheiro)
        canvas.create_image(0, 0, anchor='nw', image=imagem)
        # apresenta com o tamanho do canvas
        canvas.image = imagem
        canvas.config(width=imagem.width(), height=imagem.height())


def consulta():
    # abre uma nova janela
    consulta = tk.Toplevel()
    consulta.title("WebDev Tech Talks - Consulta")
    consulta.geometry("1000x500")
    # desativa a janela principal
    consulta.grab_set()

    # container com title 'Tipo Inscrição'
    TipoInscricao = tk.LabelFrame(
        consulta, text="Tipo Inscrição", relief='sunken', borderwidth=5)
    TipoInscricao.place(x=30, y=60, width=200, height=300)

   # para os valores selecionados
    checkvar1 = IntVar()
    checkvar2 = IntVar()
    checkvar3 = IntVar()

    # checkbox 'Docente'
    Docente = tk.Checkbutton(TipoInscricao, text="Docente", variable=checkvar1)
    Docente.place(x=10, y=10)

    # por defeito o checkbox 'Docente' está selecionado
    Docente.select()

    # checkbox 'Estudante'
    Estudante = tk.Checkbutton(TipoInscricao, text="Estudante", variable=checkvar2)
    Estudante.place(x=10, y=40)

    # checkbox 'Externo'
    Externo = tk.Checkbutton(TipoInscricao, text="Externo", variable=checkvar3)
    Externo.place(x=10, y=70)

    TipoInscricao2 = tk.LabelFrame(
        consulta, relief='sunken', borderwidth=5)
    TipoInscricao2.place(x=250, y=60, width=430, height=300)

    # treeview com colunas 'Nome' 'Perfil'
    tree = ttk.Treeview(TipoInscricao2, columns=(
        'Nome', 'Perfil'), show='headings')
    tree.column('Nome', width=200, minwidth=200, stretch=tk.NO)

    tree.column('Perfil', width=200, minwidth=200, stretch=tk.NO)
    tree.heading('Nome', text='Nome')
    tree.heading('Perfil', text='Perfil')
    tree.place(x=10, y=10)

    # botão 'Consultar'
    Consultar = tk.Button(consulta, text="Consultar",
                          relief='raised', borderwidth=5, width=15, height=2)
    Consultar.place(x=30, y=370)

    def consultar():
        # ler o checkbox selecionado
        if checkvar1.get() == 1:
            # ler o ficheiro inscricoes.txt da pasta files
            # adiciona a treevie os valores com perfil 'Docente'
            tree.delete(*tree.get_children())
            ficheiro = open("files/inscricoes.txt", "r", encoding="utf-8")
            for linha in ficheiro:
                # rstrip() remove o \n do fim da linha
                linha = linha.rstrip()
                nome, perfil = linha.split(";")
                if perfil == 'Docente':
                    tree.insert("", tk.END, values=(nome, perfil))
            ficheiro.close()
        elif checkvar2.get() == 1:
            tree.delete(*tree.get_children())
            ficheiro = open("files/inscricoes.txt", "r", encoding="utf-8")
            for linha in ficheiro:
                linha = linha.rstrip()
                nome, perfil = linha.split(";")
                if perfil == 'Estudante':
                    tree.insert("", tk.END, values=(nome, perfil))
            ficheiro.close()
        elif checkvar3.get() == 1:
            tree.delete(*tree.get_children())
            ficheiro = open("files/inscricoes.txt", "r", encoding="utf-8")
            for linha in ficheiro:
                linha = linha.rstrip()
                nome, perfil = linha.split(";")
                if perfil == 'Externo':
                    tree.insert("", tk.END, values=(nome, perfil))
            ficheiro.close()
        # se tiver os 3 selecionados
        elif checkvar1.get() == 1 and checkvar2.get() == 1 and checkvar3.get() == 1:
            tree.delete(*tree.get_children())
            ficheiro = open("files/inscricoes.txt", "r", encoding="utf-8")
            for linha in ficheiro:
                linha = linha.rstrip()
                nome, perfil = linha.split(";")
                tree.insert("", tk.END, values=(nome, perfil))
            ficheiro.close()
        else:
            messagebox.showerror("Impossível consultar",
                                 "Não selecionou nenhum tipo de inscrição")

    # associar o botão 'Consultar' à função consultar
    Consultar.config(command=consultar)


# associar o botão 'Ler Ficheiro' à função ler_ficheiro
LerFicheiro.config(command=ler_ficheiro)
# associar o botão 'Adicionar' à função adicionar
Adicionar.config(command=adicionar)
# associar o botão 'Guardar' à função guardar
Guardar.config(command=guardar)
# associar o botão 'Selecionar Imagem' à função selecionar_imagem
SelecionarImagem.config(command=selecionar_imagem)
# associar o botão 'Consulta' à função consulta
Consulta.config(command=consulta)
Window.mainloop()
