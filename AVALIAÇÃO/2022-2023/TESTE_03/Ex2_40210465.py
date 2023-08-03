# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import ttk          # treeview
from tkinter import filedialog   # filedialog boxes
from tkinter import messagebox   #  messagebox
from datetime import datetime


# ---------------Main---------------------
#-----------------------------------------
window = Tk()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 500                             # tamanho (pixeis) da window a criar 900 / 500
appHeight = 600 
x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
window.title('Despesas App')




lblTitulo = Label(window, text = "Gere as tuas Despesas!", font = "calibri, 16", fg= "gray")
lblTitulo.place(x=220, y=30)

# data
lblData = Label(window, text = datetime.now().strftime("%Y-%m-%d"), font = "calibri, 12", fg= "gray")
lblData.place(x=220, y=60)


canvasImage = Canvas(window, width = 350, height = 200, bd = 2, relief = "sunken")
canvasImage.place(x=50, y=150)
imagem = PhotoImage(file = "images\\img1.png")
image_id = canvasImage.create_image(175, 100, image=imagem)

btnSelect = Button(window, text= "Selecionar Imagem", width=25, height=2)
btnSelect.place(x=220, y=400)

# abrir um filediagog com titulo 'Select file'
def selectFile():
    filename = filedialog.askopenfilename(initialdir='images', title = "Select file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    # abrir o ficheiro selecionado
    imagem = PhotoImage(file = filename)
    # atualizar a imagem no canvas
    canvasImage.itemconfig(image_id, image=imagem)
    # atualizar a imagem no canvas
    canvasImage.image = imagem


btnSelect.config(command=selectFile)

window.mainloop()   # event listening loop by calling the mainloop()