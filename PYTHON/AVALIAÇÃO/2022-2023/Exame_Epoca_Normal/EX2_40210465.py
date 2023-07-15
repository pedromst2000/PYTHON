# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import ttk          # treeview
from tkinter import filedialog   # filedialog boxes

from tkinter import messagebox   #  messagebox





# ---------------Main-------------------------------------------
#----------------------------------------------------------------
window = Tk()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 1000                             # tamanho (pixeis) da window a criar 900 / 500
appHeight = 500 
x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
window.title('Músics Playlist')


# Bandas 
lbBandas = Label(window, text = "Bandas", font = ("Helvetica", "11"))
lbBandas.place(x=27, y=40)

lstboxBandas = Listbox(window, width=20, height = 11, bd = 4, relief = "sunken")
lstboxBandas.place (x=20, y=70)


# Buttton para mostrar musicas da banda
btn1 = Button(window, text = ">", width = 6, height = 2)
btn1.place(x=160, y=130)

# TreeView para mostrar as musicas da banda selecionada
tree = ttk.Treeview(window, columns = ("Música", "Visualizações"), show = "headings", height = 8, selectmode = "browse")
tree.column("Música", width = 220, anchor = "w")
tree.column("Visualizações", width = 130, anchor = "c")
tree.heading("Música", text = "Música")
tree.heading("Visualizações", text = "Visualizações")
tree.place(x=230, y=70)


#PAINEL  ADICIONAR MUSICA DA BANDA ATIVA
panel1 = PanedWindow(window, width = 310, height = 180, bd = "3", relief = "sunken" )
panel1.place(x=630, y=70)

lbMusica = Label(panel1, text = "Música", font = ("Helvetica", "10"))
lbVisual = Label(panel1, text = "Visualizações", font = ("Helvetica", "10"))
lbMusica.place(x=10, y=20)
lbVisual.place(x=10, y=70)

# Entrys para adicionar nova musica e nº de visualizações
txtMusica = Entry(panel1, width=25)
txtVisualizacoes = Entry(panel1, width=15)
txtMusica.place(x=130, y=20)
txtVisualizacoes.place(x=130, y=70)

# Button Adiciona ao ficheiro de musicas
btnAdicionar= Button(panel1, width=90, height=60, text = "Adicionar Música", relief = "raised", bd=3)
btnAdicionar.place(x=10, y=100)

# adiciona a imagem 'adiocionar.png' ao button 'btnAdicionar'
imgAdicionar = PhotoImage(file = "images/adicionar.png")
btnAdicionar.config(image = imgAdicionar, compound = TOP)

# Button para refresh na TreeView
btnRefresh= Button(panel1, width=90, height=65,  text = "Refresh vista", relief = "raised", bd=3)
btnRefresh.place(x=200, y=100)

# adiciona a imagem 'refresh.png' ao button 'btnRefresh'
imgRefresh = PhotoImage(file = "images/refresh.png")
btnRefresh.config(image = imgRefresh, compound = TOP)


# PAINEL MAIS INFO
panel2 = PanedWindow(window, width = 550, height = 150, bd = "3", relief = "sunken" )
panel2.place(x=20, y=300)

btnVerMais = Button(panel2, width=90, height=70, text = "ver mais" ,  relief = "raised", bd=3)
btnVerMais.place(x=10, y=20)

# adiciona a imagem 'btn+.png' ao button 'btnVerMais'
imgVerMais = PhotoImage(file = "images/btn+.png")
btnVerMais.config(image = imgVerMais, compound = TOP)

# ----- PAINEL MAIS INFORMAÇÃO
lb3 = Label(panel2, text = "Nº de músicas",  font = ("Helvetica", "10"))
lb4 = Label(panel2, text = "Música +  vista", font = ("Helvetica", "10"))
lb5 = Label(panel2, text = "Link:", font = ("Helvetica", "10"))
lb3.place(x=170, y=30)
lb4.place(x=170, y=70)
lb5.place(x=170, y=110)


txtNumFilmes = Entry(panel2, width=10)
txtMaisVisto = Entry(panel2, width=30 )
txtLink = Entry(panel2, width=30)

txtNumFilmes.place(x=270, y=30)
txtMaisVisto.place(x=270, y=70)
txtLink.place(x=270, y=110)


# container Canvas, usado para aplicações de desenho: imagens e formas geométricas
canvas = Canvas(window, width = 300, height = 150, bd = 4, relief = "sunken")
canvas.place(x=630, y=300)

# Button para selecionar Imagem a renderizar no canvas
btnSelecionarImg = Button(window, width=18, height = 2, text = "Selecionar Imagem", relief = "raised", bd=1)
btnSelecionarImg.place(x=630, y=465)


def lerBandas():
    ficheiro = open("files/bandas.txt", "r", encoding="utf-8")
    for linha in ficheiro:
        lstboxBandas.insert(END, linha)
    ficheiro.close()


def lerMusicas():
    # apresenta na treeview as musicas da banda dos COLDPLAY
    tree.delete(*tree.get_children())  # apaga todas as linhas da treeview
    # obtem a banda selecionada na listbox
    banda = str(lstboxBandas.get(ANCHOR)).split("-")[0].strip()
    ficheiro = open("files/musicas.txt", "r", encoding="utf-8")
    for linha in ficheiro:
        if linha.split(";")[0] == banda:
            tree.insert("", END, values=(linha.split(";")[1], linha.split(";")[2]))
    ficheiro.close()
    # apresentar uma mensagem de erro se não existir uma banda selecionada	
    if lstboxBandas.get(ANCHOR) == "":
        messagebox.showerror("Erro", "Selecione uma banda")
    # apresentar uma mensagem de erro se não existirem musicas para a banda selecionada
    elif tree.get_children() == ():
        messagebox.showerror("Erro", "Não existem musicas para a banda selecionada")

def adicionaMusica():
    musica = txtMusica.get()
    visualizacoes = txtVisualizacoes.get()

    # apresentar uma mensagem de erro se não existir uma banda selecionada
    if lstboxBandas.get(ANCHOR) == "":
        messagebox.showerror(
            "Erro", "Selecione uma banda no qual pretende adicionar a música")
    # apresentar uma mensagem de erro se os campos estiverem vazios
    elif txtMusica.get() == "" or txtVisualizacoes.get() == "":
        messagebox.showerror(
            "Erro", "Preencha todos os campos para adicionar a música")
    # se tiver musica mas não tiver visualizações, apresenta uma mensagem de erro
    elif txtMusica.get() != "" and txtVisualizacoes.get() == "":
        messagebox.showerror(
            "Erro", "Preencha todos os campos para adicionar a música")
    # se tiver visualizações mas não tiver musica, apresenta uma mensagem de erro
    elif txtMusica.get() == "" and txtVisualizacoes.get() != "":
        messagebox.showerror(
    "Erro", "Preencha todos os campos para adicionar a música")
            
  # adiciona uma nova linha ao ficheiro de musicas banda;musica;visualizacoes; substituir o link do youtube por um espaço
    ficheiro = open("files/musicas.txt", "a", encoding="utf-8")
    # adicionar a nova linha ao ficheiro de musicas
    ficheiro.write(lstboxBandas.get(ANCHOR).split("-")[0].strip() + ";" + musica + ";" + visualizacoes + ";" + " " + "\n")
    ficheiro.close()


def refresh():
    #  atualiza a treeview com a musica adicionada ao ficheiro de musicas
    tree.delete(*tree.get_children())  # apaga todas as linhas da treeview
    # obtem a banda selecionada na listbox
    banda = str(lstboxBandas.get(ANCHOR)).split("-")[0].strip()
    ficheiro = open("files/musicas.txt", "r", encoding="utf-8")
    for linha in ficheiro:
        if linha.split(";")[0] == banda:
            tree.insert("", END, values=(linha.split(";")[1], linha.split(";")[2]))
    ficheiro.close()


def maisInfo():
    # campos 
    txtNumFilmes.delete(0, END)
    txtMaisVisto.delete(0, END)
    txtLink.delete(0, END)
    # obtem a banda selecionada na listbox
    banda = str(lstboxBandas.get(ANCHOR)).split("-")[0].strip()
    # obtem o numero de musicas da banda
    ficheiro = open("files/musicas.txt", "r", encoding="utf-8")
    numMusicas = 0
    for linha in ficheiro:
        if linha.split(";")[0] == banda:
            numMusicas += 1
    ficheiro.close()
    txtNumFilmes.insert(0, numMusicas)
    # obtem a musica mais vista da banda
    ficheiro = open("files/musicas.txt", "r", encoding="utf-8")
    maisVisto = 0
    for linha in ficheiro:
        if linha.split(";")[0] == banda:
            # para comparar o numero de visualizacoes 
            if linha.split(";")[2].endswith("M"):
                if float(linha.split(";")[2][:-1]) > maisVisto:
                    maisVisto = float(linha.split(";")[2][:-1])
                    musica = linha.split(";")[1]
            elif linha.split(";")[2].endswith("m"):
                if float(linha.split(";")[2][:-1]) > maisVisto:
                    maisVisto = float(linha.split(";")[2][:-1])
                    musica = linha.split(";")[1]
    ficheiro.close()
    txtMaisVisto.insert(0, musica)
    # obtem o link da musica mais vista da banda
    ficheiro = open("files/musicas.txt", "r", encoding="utf-8")
    for linha in ficheiro:
        if linha.split(";")[0] == banda:
            if linha.split(";")[1] == musica:
                txtLink.insert(0, linha.split(";")[3])
    ficheiro.close()

    # desativa os campos de texto 
    txtNumFilmes.configure(state="disabled")
    txtMaisVisto.configure(state="disabled")
    txtLink.configure(state="disabled")


def SelecionarImg():
# abrir um filedialog no caminho 'images' para selecionar uma imagem .png ouf .gif
    ficheiro = filedialog.askopenfilename(initialdir="images", title="Selecionar Imagem", filetypes=(("png files", "*.png"), ("gif files", "*.gif")))
    # renderizar a imagem selecionada no canvas
    canvas.image = PhotoImage(file=ficheiro)
    canvas.create_image(0, 0, anchor=NW, image=canvas.image)
    # ocupar o espaço do canvas com a imagem selecionada
    canvas.configure(width=canvas.image.width(), height=canvas.image.height())

# associa a função lerBandas() ao evento de click do botão '>'
btn1.configure(command=lerMusicas)
# associa a função adicionaMusica() ao evento de click do botão 'Adicionar Música'
btnAdicionar.configure(command=adicionaMusica)
# associa a função refresh() ao evento de click do botão 'Refresh vista'
btnRefresh.configure(command=refresh)
# associa a função maisInfo() ao evento de click do botão 'ver mais'
btnVerMais.configure(command=maisInfo)
# associa a função SelecionarImg() ao evento de click do botão 'Selecionar Imagem'
btnSelecionarImg.configure(command=SelecionarImg)

lerBandas()  # chama a função lerBandas() para carregar a listbox com as bandas
window.mainloop()   # event listening loop by calling the mainloop()