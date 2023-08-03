import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
from tkinter import messagebox
# from PIL import Image, ImageTk

# window 1000x500 com titulo 'Filmes Dashboard'
window = tk.Tk()
window.title('Filmes Dashboard')
window.geometry('1000x500')

# label categorias
labelCategories = tk.Label(window, text='Categorias', font=('Helvetica', 11))
labelCategories.place(x=20, y=20)

# listbox das categorias dos filmes abaixo da label 'Categorias'
listboxCategories = tk.Listbox(
    window, width=30, height=20, relief='sunken', borderwidth=5)
listboxCategories.place(x=20, y=50, width=150, height=200)


# botão '>'
buttonAddCategory = tk.Button(
    window, text='>', width=5, height=2, relief='raised', borderwidth=5)
buttonAddCategory.place(x=180, y=120)

# treeview dos filmes 2x2
treeviewMovies = tk.ttk.Treeview(window, columns=(
    'Filme', 'Visualizações'), show='headings')
# definir o nome das colunas
treeviewMovies.heading('Filme', text='Filme')
treeviewMovies.heading('Visualizações', text='Visualizações')
# centrar o contéudo das visualizações
treeviewMovies.column('Visualizações', anchor=tk.CENTER)
# definir a largura das colunas
treeviewMovies.place(x=240, y=50, width=400, height=200)


# container para apresentação dos filmes
container = tk.Frame(window, relief='sunken', borderwidth=5)
container.place(x=20, y=270, width=620, height=170)

# botão Categoria | Ver +
buttonCategory = tk.Button(container, text='Categoria | Ver +',
                           width=15, height=3, relief='raised', borderwidth=5)
buttonCategory.place(x=10, y=20)

# label de número de filmes
labelMovies = tk.Label(container, text='Nº de Filmes')
labelMovies.place(x=150, y=20)

# input de número de filmes
entryMovies = tk.Entry(container, width=8, relief='sunken', borderwidth=2)
entryMovies.place(x=250, y=20)
# entryMovies.insert(0, 0)

# label de filme mais visto
labelMostViewed = tk.Label(container, text='Filme + visto')
labelMostViewed.place(x=150, y=60)

# input de filme mais visto
entryMostViewed = tk.Entry(container, width=30, relief='sunken', borderwidth=2)
entryMostViewed.place(x=250, y=60)

# container ao lado da treeview dos filmes
container2 = tk.Frame(window, relief='sunken', borderwidth=5)
container2.place(x=670, y=50, width=300, height=200)

# label 'Filme'
labelMovie = tk.Label(container2, text='Filme')
labelMovie.place(x=10, y=10)

# input de filme
entryMovie = tk.Entry(container2, width=30, relief='sunken', borderwidth=2)
entryMovie.place(x=60, y=8)

# label 'visualizações' abaixo da label 'Filme'
labelViews = tk.Label(container2, text='Visualizações')
labelViews.place(x=10, y=80)

# input de visualizações
entryViews = tk.Entry(container2, width=8, relief='sunken', borderwidth=2)
entryViews.place(x=100, y=80)

# botão 'Acrescentar Filme'
buttonAddMovie = tk.Button(container2, text='Acrescentar Filme',
                           width=15, height=2, relief='raised', borderwidth=5)
buttonAddMovie.place(x=10, y=120)

# botão 'refresh vista'
buttonRefresh = tk.Button(container2, text='refresh vista',
                          width=15, height=2, relief='raised', borderwidth=5)
buttonRefresh.place(x=160, y=120)

# canvas
canvas = tk.Canvas(window, relief='sunken', borderwidth=5)
canvas.place(x=670, y=270, width=300, height=170)

# botão 'Selecionar Imagem' abaixo da canvas
buttonSelectImage = tk.Button(
    window, text='Selecionar Imagem', width=15, height=1, relief='raised', borderwidth=5)
buttonSelectImage.place(x=670, y=450)

# colocar label 'Autor: by Pedro Teixeira'helvetica 10 ao lado do botão 'Selecionar Imagem'
labelAuthor = tk.Label(window, text='Autor: by Pedro Teixeira', font=('Helvetica', 10))   
labelAuthor.place(x=800, y=450)


# Função para o Passo 2
# função para carregar as categorias do ficheiro 'categorias.txt' para a listbox das categorias


def load_Categories():
    # carregar as categorias do ficheiro 'categorias.txt' para a listbox das categorias
    # com formatação correta retirando caracteres especiais
    with open('./ficheiros/categorias.txt', 'r', encoding='utf-8') as file:
        for line in file:
            listboxCategories.insert(tk.END, line.strip(' \n'))
    file.close()


# Função para o Passo 3
# função para carregar a mensagem de erro d enão existência de filmes
def load_Error():
    messagebox.showwarning(
        'filmes', 'Não existem filmes registados nesta categoria')

# Função para o Passo 3
def load_Movies():
 # buscar o valor selecionado na listbox das categorias
    category = listboxCategories.get(listboxCategories.curselection())
    # limpar a treeview dos filmes
    treeviewMovies.delete(*treeviewMovies.get_children())
    # ler o ficheiro 'filmes.txt' e carregar os filmes para a treeview dos filmes
    with open('./ficheiros/filmes.txt', 'r', encoding='utf-8') as file:
        # ciclo para percorrer o ficheiro 'filmes.txt'
        for line in file:
            # buscar o nome do filme
            movie = line.split(';')[0]
            # buscar o número de visualizações do filme
            views = line.split(';')[2]
            # se o filme tiver mais que uma categoria associada verificar se a categoria selecionada está associada ao filme

            if category in line.split(';')[1].split(','):
                # inserir o filme e o número de visualizações na treeview dos filmes
                treeviewMovies.insert('', tk.END, values=(movie, views))
            # se o filme não tiver mais que uma categoria associada verificar se a categoria selecionada está associada ao filme
            elif category == line.split(';')[2]:
                # inserir o filme e o número de visualizações na treeview dos filmes
                treeviewMovies.insert('', tk.END, values=(movie, views))
            # se o filme não tiver mais que uma categoria associada e a categoria selecionada não estiver associada ao filme
            # se não existirem filmes na categoria selecionada
            # else:
                # load_Error()

    file.close()


# função para o Passo 4
def show_movies():
    # ler o ficheiro 'filmes.txt' e contar o número de filmes existentes associados a categoria selecionada da listbox
    with open('./ficheiros/filmes.txt', 'r', encoding='utf-8') as file:

        category = listboxCategories.get(listboxCategories.curselection())
        # inicializar a variável de contagem de filmes
        count = 0
        # ciclo para percorrer o ficheiro 'filmes.txt'
        for line in file:
            # contar o número de filmes existentes associados a categoria selecionada da listbox
            if category in line.split(';')[1].split(','):
                count += 1
            elif category == line.split(';')[1]:
                count += 1
        # apresentar o número de filmes existentes associados a categoria selecionada da listbox
        entryMovies.insert(0, count)
        # atulizar o numero de filmes sempre que se seleciona uma outra categoria
        entryMovies.delete(0, tk.END)
        entryMovies.insert(0, count)
    file.close()

    # apresentar o filme mais visto na input de filme mais visto
    with open('./ficheiros/filmes.txt', 'r', encoding='utf-8') as file:
        # inicializar a variável de número de visualizações
        views = 0
        # inicializar a variável de nome do filme mais visto
        movie = ''
        # ciclo para percorrer o ficheiro 'filmes.txt'
        for line in file:
            # verificar o filme com mais visualizações da categoria selecionada
            if category in line.split(';')[1].split(','):
                if int(line.split(';')[2]) > views:
                    views = int(line.split(';')[2])
                    movie = line.split(';')[0]
            elif category == line.split(';')[1]:
                if int(line.split(';')[2]) > views:
                    views = int(line.split(';')[2])
                    movie = line.split(';')[0]
        # apresentar o filme mais visto na input de filme mais visto
        entryMostViewed.insert(0, movie)
        # atualizar o filme mais visto sempre que se seleciona uma outra categoria
        entryMostViewed.delete(0, tk.END)
        entryMostViewed.insert(0, movie)
    file.close()


def add_movie():
    # adicionar o novo filme ao ficheiro 'filmes.txt'
    with open('./ficheiros/filmes.txt', 'a', encoding='utf-8') as file:
        # inserir o novo filme no ficheiro 'filmes.txt'
        # nome do filme | categoria do filme | número de visualizações do filme
        # nome do filme do input | categoria selecionada da listbox | visualizações do filme = 0
        file.write(entryMovie.get() + ';' + listboxCategories.get(
            listboxCategories.curselection()) + ';' + '0' + '\n')
    file.close()


def refresh_view():
    # atualizar a treeview dos filmes
    treeviewMovies.delete(*treeviewMovies.get_children())
    # ler o ficheiro 'filmes.txt' e carregar os filmes para a treeview dos filmes
    with open('./ficheiros/filmes.txt', 'r', encoding='utf-8') as file:
        # ciclo para percorrer o ficheiro 'filmes.txt'
        for line in file:
            # buscar o nome do filme
            movie = line.split(';')[0]
            # buscar o número de visualizações do filme
            views = line.split(';')[2]
            # inserir o filme e o número de visualizações na treeview dos filmes
            treeviewMovies.insert('', tk.END, values=(movie, views))

    file.close()




# def select_image():
#     # abrir a janela de seleção de ficheiros na pasta 'ficheiros' para selecionar a imagem
#     filename = filedialog.askopenfilename(
#         initialdir='./ficheiros', title='Select file', filetypes=(('gif', '*.gif'), ('all files', '*.*')))

# # colocar a imagem selecionada no canvas 
#     image = Image.open(filename)
#     image = image.resize((200, 200), Image.ANTIALIAS)
#     image = ImageTk.PhotoImage(image)
#     canvasImage.create_image(0, 0, anchor=tk.NW, image=image)
#     canvasImage.image = image





# associar ao botao '>' a função load_Movies
buttonAddCategory.config(command=load_Movies)
# associar ao botao 'Categoria | Ver +' a função show_movies
buttonCategory.config(command=show_movies)
# associar ao botao 'Adicionar' a função add_movie
buttonAddMovie.config(command=add_movie)
# associar ao botao 'Atualizar' a função refresh_view
buttonRefresh.config(command=refresh_view)
# associar ao botao 'Selecionar' a função select_image
# buttonSelectImage.config(command=select_image)

load_Categories()
window.mainloop()