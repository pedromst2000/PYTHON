import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import datetime
from tkinter import messagebox

Window = tk.Tk()
Window.title("Filmes Dashboard")
Window.geometry("1160x400")


menu = tk.Menu(Window)
Window.config(menu=menu)

perfil_utilizador = tk.Menu(menu)


# treeview com colunas 'Categoria' e 'Filmes'
treeview = ttk.Treeview(Window, columns=('Categoria'), show='headings')

# define os nomes das colunas
treeview.heading('Categoria', text='Categoria')
treeview.place(x=10, y=10, width=200, height=170)

# botão '>' para o ponto 3
btnMoviesView = tk.Button(Window, text='>', width=5, height=2, relief='groove')
btnMoviesView.place(x=240, y=60)


# treeview com colunas 'Filme' 'Visualizações'
treeview2 = ttk.Treeview(Window, columns=(
    'Filme', 'Visualizações'), show='headings')
# define os nomes das colunas
treeview2.heading('Filme', text='Filme')
treeview2.heading('Visualizações', text='Visualizações')
treeview2.place(x=300, y=10, width=400, height=170)

# centrar o texto da coluna 'Visualizações'
treeview2.column('Visualizações', anchor='center')

# coloca um scroll na treeview2
scroll = ttk.Scrollbar(Window, orient='vertical', command=treeview2.yview)
scroll.place(x=700, y=10, width=20, height=170)

# botão '>' para o ponto 4
btnViewSelectedMovie = tk.Button(
    Window, text='>', width=5, height=2, relief='groove')
btnViewSelectedMovie.place(x=740, y=60)

container = tk.Frame(Window, relief='sunken', bd=2, width=310, height=170)
container.place(x=810, y=10)

# label 'Filme' e respetivo campo de texto
lblMovie = tk.Label(container, text='Filme')
lblMovie.place(x=10, y=40)

txtMovie = tk.Entry(container, width=38)
txtMovie.place(x=60, y=40)

# label 'Visualizações' e respetivo campo de texto
lblViews = tk.Label(container, text='Visualizações')
lblViews.place(x=10, y=80)

txtViews = tk.Entry(container, width=12)
txtViews.place(x=90, y=80)

container2 = tk.Frame(Window, relief='sunken', bd=2, width=310, height=170)
container2.place(x=810, y=200)

# botão 'Guardar' para o ponto 5
btnSave = tk.Button(container2, text='', width=50, height=50, relief='groove')
btnSave.place(x=90, y=60)
imgSave = tk.PhotoImage(file='images/guardar.png')

# reduz a imagem
imgSave = imgSave.subsample(2, 2)

btnSave.config(borderwidth=0, cursor='hand2')
btnSave.config(image=imgSave)

# botão 'Remover' para o ponto 6
btnRemove = tk.Button(container2, text='', width=50,
                      height=50, relief='groove')
btnRemove.place(x=170, y=60)

imgRemove = tk.PhotoImage(file='images/remover.png')

# reduz a imagem
imgRemove = imgRemove.subsample(2, 2)

btnRemove.config(borderwidth=0, cursor='hand2')
btnRemove.config(image=imgRemove)

container3 = tk.Frame(Window, relief='sunken', bd=2, width=700, height=170)
container3.place(x=10, y=200)

# botão 'Ver +'
btnViewMore = tk.Button(container3, text='Ver +',
                        width=15, height=5, relief='groove')
btnViewMore.place(x=10, y=30)

# label 'Nº de Filmes'
lblNumMovies = tk.Label(container3, text='Nº de Filmes')
lblNumMovies.place(x=350, y=30)

# entry 'Nº de Filmes'
txtNumMovies = tk.Entry(container3, width=6)
txtNumMovies.place(x=430, y=30)

# label 'Filme mais visto'
lblMostViewedMovie = tk.Label(container3, text='Filme mais visto')
lblMostViewedMovie.place(x=350, y=90)

# entry 'Filme mais visto'
txtMostViewedMovie = tk.Entry(container3, width=38)
txtMostViewedMovie.place(x=450, y=90)

# Função para o ponto 2
def categorias_view():
    # exibir as categorias na treeview

    categorias = []
    file = open("files/Categorias.txt", "r", encoding="utf-8")

    lines = file.readlines()

    for line in lines:
        categorias.append(line.strip())

    for categoria in categorias:
        treeview.insert('', 'end', values=(categoria))

    file.close()

# Função para o ponto 3
def filmes_View():
    # apresenta os filmes da categoria selecionada na treeview
    # limpar a treeview2
    treeview2.delete(*treeview2.get_children())

    # ler a categoria selecionada na treeview
    categoria = treeview.item(treeview.selection())['values'][0]

    # ler os filmes da categoria selecionada
    file = open("files/filmes.txt", "r", encoding="utf-8")

    lines = file.readlines()

    for line in lines:
        filme = line.split(";")[0]
        visualizacoes = line.split(";")[2]

        if categoria == line.split(";")[1]:
            treeview2.insert('', 'end', values=(filme, visualizacoes))

    file.close()

# Função para o ponto 4
def viewSelectedMovie():
    # função que permite apresentar o nome e as visualizações do filme selecionado da treeview
    # nos respetivos campos
    # limpar os campos de texto
    txtMovie.delete(0, 'end')
    txtViews.delete(0, 'end')

    # ler o filme selecionado na treeview2
    filme = treeview2.item(treeview2.selection())['values'][0]
    visualizacoes = treeview2.item(treeview2.selection())['values'][1]

    # apresentar o filme e as visualizações nos respetivos campos de texto
    txtMovie.insert(0, filme)
    txtViews.insert(0, visualizacoes)


# Função para o ponto 5
def guardar_filme():
    # atualizar no ficheiro o titulo e as visualizações do filme selecionado

    # ler o filme selecionado na treeview2
    filme = treeview2.item(treeview2.selection())['values'][0]
    visualizacoes = treeview2.item(treeview2.selection())['values'][1]

    # ler o titulo e as visualizações dos campos de texto
    titulo = txtMovie.get()
    views = txtViews.get()

    # abrir o ficheiro filmes.txt
    file = open("files/filmes.txt", "r", encoding="utf-8")

    lines = file.readlines()

    file.close()

    # abrir o ficheiro filmes.txt em modo de escrita e leitura
    file = open("files/filmes.txt", "w+", encoding="utf-8")

    # percorre o ficheiro e atualiza o titulo e as visualizações do filme selecionado
    for line in lines:
        if filme == line.split(";")[0]:
            file.write("\n" + titulo + ";" + line.split(";")[1] + ";" + views)
        else:
            file.write(line)

    file.close()

    # atualizar a treeview2
    filmes_View()


# Função para o ponto 6
def remover_filme():
    # remove o filme apresentado nos campos de texto
    filme = txtMovie.get()
    visualizacoes = txtViews.get()

    # abrir o ficheiro filmes.txt
    file = open("files/filmes.txt", "r", encoding="utf-8")

    lines = file.readlines()

    file.close()

    # abrir o ficheiro filmes.txt em modo de escrita e leitura
    file = open("files/filmes.txt", "w+", encoding="utf-8")

    for line in lines:
        # replace do filme selecionado por uma string vazia
        if filme == line.split(";")[0]:
            line = line.replace(line, "")
        file.write(line)

    file.close()

    # atualizar a treeview2
    filmes_View()

# função para o ponto 7
def ver_mais():
    # apresenta o número de filmes e o filme mais visto
    # limpar os campos de texto
    txtNumMovies.delete(0, 'end')
    txtMostViewedMovie.delete(0, 'end')

    # abrir o ficheiro filmes.txt
    file = open("files/filmes.txt", "r", encoding="utf-8")

    # contar o número de filmes pela categoria selecionada
    num_filmes = 0

    lines = file.readlines()

    for line in lines:

        if treeview.item(treeview.selection())['values'][0] == line.split(";")[1]:
            num_filmes += 1

    file.close()

    # apresentar o filme mais visto pela categoria selecionada
    # abrir o ficheiro filmes.txt
    file = open("files/filmes.txt", "r", encoding="utf-8")

    lines = file.readlines()

    # variáveis para guardar o filme mais visto e o número de visualizações
    filme_mais_visto = ""
    num_visualizacoes = 0

    for line in lines:
        if treeview.item(treeview.selection())['values'][0] == line.split(";")[1]:
            if int(line.split(";")[2]) > num_visualizacoes:
                num_visualizacoes = int(line.split(";")[2])
                filme_mais_visto = line.split(";")[0]

    file.close()

    # apresentar os resultados nos respetivos campos de texto
    txtNumMovies.insert(0, num_filmes)
    txtMostViewedMovie.insert(0, filme_mais_visto)

# função para o ponto 8
def rodape_data():
    
    lblFooter = tk.Label(Window, text='', bd=1, relief='sunken', anchor='w')
    # apresentar a data e hora atualizada no rodapé e nome do utilizador
    # nome do utilizador do ficheiro perfil.txt
    file = open("files/perfil.txt", "r", encoding="utf-8")

    lines = file.readlines()

    nome_utilizador = lines[0].split(";")[0]

    file.close()

    # apresentar a data e hora atualizada no rodapé e nome do utilizador
    lblFooter.config(text=datetime.datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S") + "   " + f'bem-vindo {nome_utilizador}')

    lblFooter.pack(side='bottom', fill='x')


# função para a opção do menu 'Perfil utilizador'
def perfil_utilizador():
    window = tk.Toplevel(Window)
    window.title("Perfil")
    window.geometry("600x500")

    # label 'Nome'
    lblNome = tk.Label(window, text='Nome')
    lblNome.place(x=50, y=50)
    
    # entry 'Nome'
    txtNome = tk.Entry(window, width=30)
    txtNome.place(x=100, y=50)

    # canvas para a imagem de perfil
    canvas = tk.Canvas(window, width=250, height=180, bg='white', bd=0, highlightthickness=0)
    canvas.place(x=320, y=20)

    # botão 'Selecionar imagem de perfil'
    btnSelectImage = tk.Button(window, text='Selecionar imagem de perfil', width=30, height=2, relief='groove')
    btnSelectImage.place(x=60, y=100)   

    # botão 'Guardar Perfil'
    btnSaveProfile = tk.Button(window, text='Guardar Perfil', width=30, height=2, relief='groove')
    btnSaveProfile.place(x=60, y=190) 

    file = open("files/perfil.txt", "r", encoding="utf-8")

    lines = file.readlines()

    nome = lines[0].split(";")[0]
    imagem = lines[0].split(";")[1]

    file.close()

    txtNome.insert(0, nome)
    # # apresentar a imagem de perfil
    img = tk.PhotoImage(file=imagem)
    canvas.create_image(0, 0, anchor='nw', image=img)
    canvas.image = img

    def selecionar_imagem():
        # abrir na pasta images
        filename = filedialog.askopenfilename(initialdir="images", title="Selecione uma imagem", filetypes=(
            ("png files", "*.png"), ("jpg files", "*.jpg"), ("jpeg files", "*.jpeg")))
        
        # apresentar a imagem de perfil
        img = tk.PhotoImage(file=filename)
        canvas.create_image(0, 0, anchor='nw', image=img)
        canvas.image = img

    

    def guardar_perfil():
        # substituir o nome e a imagem de perfil no ficheiro perfil.txt
        nome = txtNome.get()
        imagem = canvas.image

        # abrir o ficheiro perfil.txt
        file = open("files/perfil.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        # abrir o ficheiro perfil.txt em modo de escrita e leitura
        file = open("files/perfil.txt", "w+", encoding="utf-8")

        # percorre o ficheiro e atualiza o nome e a imagem de perfil
        for line in lines:
            # escrever a photoimage como string
            file.write(nome + ";" + str(imagem) + "\n")
        file.close()

    btnSelectImage.config(command=selecionar_imagem)
    btnSaveProfile.config(command=guardar_perfil)

# opção do menu 'Sair'
def sair():
    if messagebox.askokcancel("Sair", "Tem a certeza que pretende sair?"):
        Window.destroy()


menu.add_command(label="Perfil utilizador", command=perfil_utilizador)
menu.add_command(label="Gráfico")
menu.add_command(label="Sair", command=sair)

# associar a função filmes_View ao botão '>'
btnMoviesView.config(command=filmes_View)
# associar a função viewSelectedMovie ao botão '>'
btnViewSelectedMovie.config(command=viewSelectedMovie)
# associar a função guardar_filme ao botão 'Guardar'
btnSave.config(command=guardar_filme)
# associar a função remover_filme ao botão 'Remover'
btnRemove.config(command=remover_filme)
# associar a função ver_mais ao botão 'Ver +'
btnViewMore.config(command=ver_mais)

rodape_data()
categorias_view()
Window.mainloop()