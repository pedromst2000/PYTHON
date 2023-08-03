import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import datetime

Window = tk.Tk()
Window.title("Filmes Dashboard")
Window.geometry("1200x380")


menu = tk.Menu(Window)
Window.config(menu=menu)

opcoes_menu = tk.Menu(menu)


# treeview com coluna 'Categoria'
tree = ttk.Treeview(Window, columns=('Categoria'), show='headings', height=7)

# definir o nome da coluna
tree.heading('Categoria', text='Categoria')
tree.place(x=10, y=10)

# botão '>' ao lado da treeview
btn = tk.Button(Window, text='>', width=5, height=2, relief='groove')
btn.place(x=250, y=70)


# treeview com colunas 'Filme' 'Visualizações'
tree2 = ttk.Treeview(Window, columns=('Filme', 'Visualizações'), show='headings', height=7)

# definir o nome das colunas
tree2.heading('Filme', text='Filme')
tree2.heading('Visualizações', text='Visualizações')
tree2.place(x=325, y=10)

# largura da coluna visualizações
tree2.column('Visualizações', width=100)
tree2.column('Filme', width=300)


container = tk.Frame(Window, width=720, height=130, relief='sunken', bd=4)
container.place(x=10, y=220)    


# botão 'Ver +'
btn2 = tk.Button(container, text='Ver +', width=15, height=3, relief='groove')
btn2.place(x=10, y=10)

# label 'Nº de Filmes'
nFilmes = tk.Label(container, text='Nº de Filmes', font=('Arial', 10))
nFilmes.place(x=320, y=10)

entryNFilmes = tk.Entry(container, width=7)
entryNFilmes.place(x=420, y=10)

# label 'Filme mais visto'
filmeMaisVisto = tk.Label(container, text='Filme mais visto', font=('Arial', 10))
filmeMaisVisto.place(x=320, y=60)

entryFilmeMaisVisto = tk.Entry(container, width=42)
entryFilmeMaisVisto.place(x=440, y=60)


# botão '>'
btn3 = tk.Button(Window, text='>', width=5, height=2, relief='groove')
btn3.place(x=750, y=60)

container2 = tk.Frame(Window, width=360, height=230, relief='sunken', bd=4)
container2.place(x=820, y=10)

# label 'Filme'
filme = tk.Label(container2, text='Filme', font=('Arial', 10))
filme.place(x=10, y=10)

entryFilme = tk.Entry(container2, width=45)
entryFilme.place(x=55, y=10)

# label 'Visualizações'
visualizacoes = tk.Label(container2, text='Visualizações', font=('Arial', 10))
visualizacoes.place(x=10, y=60)

entryVisualizacoes = tk.Entry(container2, width=9)
entryVisualizacoes.place(x=110, y=60)

# botão 'Atualizar'
btnAtualizar = tk.Button(container2, text='Atualizar', width=15, height=3, relief='groove')
btnAtualizar.place(x=90, y=110)


# rodapé da janela
rodape = tk.Frame(Window, width=1200, height=30, relief='groove')
rodape.place(x=0, y=350)

# apresentar a data e hora atual no rodapé e o nome do utilizador
# eg: 2021-01-01 00:00:00 bem vindo Pedro Teixeira
data = datetime.datetime.now()
data = data.strftime('%Y-%m-%d %H:%M:%S')
labelData = tk.Label(rodape, text=data, font=('Arial', 10))
labelData.place(x=10, y=5)

file = open('files/perfil.txt', 'r', encoding='utf-8')

lines = file.readlines()

for line in lines:
    # apresentar o nome do utilizador no rodapé
    labelUtilizador = tk.Label(rodape, text='bem vindo ' + line.split(';')[0], font=('Arial', 10))
    labelUtilizador.place(x=150, y=5)

file.close()


# apresenta o filme selecionado e as suas visualizações no container2
def selecionar_filme(): # função para o Botão 3
    # ler o filme selecionado na treeview
    filme = tree2.item(tree2.selection())['values'][0]
    visualizacoes = tree2.item(tree2.selection())['values'][1]

    # apresentar o filme e as visualizações no container2
    entryFilme.delete(0, 'end')
    entryFilme.insert(0, filme)
    entryVisualizacoes.delete(0, 'end')
    entryVisualizacoes.insert(0, visualizacoes)


# para atualizar o titulo e numero de visualizações do filme selecionado
def atualizar_filme(): # função para o botão 4
    # ler os campos do container2
    filme = entryFilme.get()
    visualizacoes = entryVisualizacoes.get()
    print(filme, visualizacoes)

    # atualizar no ficheiro filmes.txt o titulo e numero de visualizações do filme selecionado
    file = open('files/filmes.txt', 'r', encoding='utf-8')

    lines = file.readlines()

    file = open('files/filmes.txt', 'w+', encoding='utf-8')

    for line in lines:
        if filme in line:
            print(line)
            line = line.replace(line.split(';')[0], filme)
            line = line.replace(line.split(';')[2], visualizacoes)
        file.write(line)

    file.close()

   
    # atualizar a treeview
    filmes_View()


# apresenta a estatistica dos filmes da categoria selecionada
def estatistica_View(): # função para Botão 'Ver +'

# ler a categoria selecionada na treeview
    categoria = tree.item(tree.selection())['values'][0]

    # contar o número de filmes da categoria selecionada
    file = open('files/filmes.txt', 'r', encoding='utf-8')

    lines = file.readlines()

    nFilmes = 0

    for line in lines:
        if categoria in line:
            nFilmes += 1
    
    # encontrar o filme mais visto da categoria selecionada
    file = open('files/filmes.txt', 'r', encoding='utf-8')
        
    lines = file.readlines()

    visualizacoes = 0

    for line in lines:
        if categoria in line:
            if int(line.split(';')[2]) > visualizacoes:
                visualizacoes = int(line.split(';')[2])
                filmeMaisVisto = line.split(';')[0]

    # apresentar os resultados
    entryFilmeMaisVisto.delete(0, 'end')
    entryFilmeMaisVisto.insert(0, filmeMaisVisto)
    entryNFilmes.delete(0, 'end')
    entryNFilmes.insert(0, nFilmes)

    file.close()

# apresenta os filmes da categoria selecionada
def filmes_View():
    # ler a categoria selecionada na treeview
    categoria = tree.item(tree.selection())['values'][0]

    # limpar a treeview
    tree2.delete(*tree2.get_children())

    # apresentar os filmes na treeview
    file = open('files/filmes.txt', 'r', encoding='utf-8')

    lines = file.readlines()

    for line in lines:
        if categoria in line:
            filme = line.split(';')[0]
            visualizacoes = line.split(';')[2]
            tree2.insert('', 'end', values=(filme, visualizacoes))
            
    file.close()

  # apresentar as categorias na treeview
def categorias_View():
    file = open('files/categorias.txt', 'r', encoding='utf-8')

    lines = file.readlines()

    for line in lines:
        tree.insert('', 'end', values=line)

    file.close()

# para abrir a janela de perfil na opção do menu 'perfil utilizador'
def abrir_perfil():
    # abrir a janela de perfil
    perfil = tk.Toplevel()
    perfil.title("Perfil")
    perfil.geometry("600x500")

    # label 'Nome'
    nome = tk.Label(perfil, text='Nome', font=('Arial', 10))
    nome.place(x=10, y=10)

    entryNome = tk.Entry(perfil, width=45)
    entryNome.place(x=55, y=10)

    # botão 'Selecionar imagem de perfil'
    btnSelecionar = tk.Button(perfil, text='Selecionar imagem de perfil', width=25, height=2, relief='groove')
    btnSelecionar.place(x=10, y=60)

    # botão 'Guardar perfil'
    btnGuardar = tk.Button(perfil, text='Guardar perfil', width=15, height=2, relief='groove')
    btnGuardar.place(x=10, y=110)

    # canvas ao lado do botão 'Selecionar imagem de perfil'
    canvas = tk.Canvas(perfil, width=200, height=200, relief='groove', bg='white')
    canvas.place(x=370, y=20)

    def selecionar_imagem():
        ficheiro = filedialog.askopenfilename(initialdir='images', title='Selecionar imagem', filetypes=(('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*')))
        # apresentar a imagem no canvas
        img = tk.PhotoImage(file=ficheiro)
        canvas.create_image(0, 0, anchor='nw', image=img)
        canvas.image = img

    def guardar_perfil():
        # valor do campo nome
        nome = entryNome.get()

        # valor da imagem selecionada
        imagem = canvas.image

        # guardar o nome e a imagem no ficheiro perfil.txt
        file = open('files/perfil.txt', 'w+', encoding='utf-8')

        file.write(nome + ';' + imagem)

        file.close()
        

    btnSelecionar.config(command=selecionar_imagem)
    btnGuardar.config(command=guardar_perfil)

def sair():
    if messagebox.askyesno('Sair', 'Tem a certeza que quer sair?'):
        Window.destroy()
    

menu.add_command(label="Perfil utilizador", command=abrir_perfil)
menu.add_command(label="Sair", command=sair)
# associar a função filmes_View ao botão '>'
btn.config(command=filmes_View)
# associar a função estatistica_View ao botão 'Ver +'
btn2.config(command=estatistica_View)
# associar a função atualizar_filme ao botão 'Atualizar'
btnAtualizar.config(command=atualizar_filme)
# associar a função selecionar_filme ao botão '>'
btn3.config(command=selecionar_filme)

categorias_View()

Window.mainloop()