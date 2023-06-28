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
btnAdicionar= Button(panel1, width=17, height=3, text = "Adicionar Música", relief = "raised", bd=3)
btnAdicionar.place(x=10, y=100)

# Button para refresh na TreeView
btnRefresh= Button(panel1, width=17, height=3,  text = "Refresh vista", relief = "raised", bd=3)
btnRefresh.place(x=200, y=100)



# PAINEL MAIS INFO
panel2 = PanedWindow(window, width = 550, height = 150, bd = "3", relief = "sunken" )
panel2.place(x=20, y=300)

btnVerMais = Button(panel2, width=18, height=3, text = "ver mais" ,  relief = "raised", bd=3)
btnVerMais.place(x=10, y=20)


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

window.mainloop()   # event listening loop by calling the mainloop()