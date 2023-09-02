import tkinter as tk
from tkinter import filedialog

# window
window = tk.Tk()
window.title('Gestor de Fotos')
window.geometry('1000x500')

# colocar uma listbox no canto superior esquerdo
listbox = tk.Listbox(window, width=50, height=20)
listbox.grid(row=0, column=0)
listbox.place(x=10, y=10)


# colocar um botão 'Selecionar imagem' abaicxo da listbox com a mesma width
btn = tk.Button(window, text='Selecionar imagem', width=42, height=2)
#posicionar o botão abaixo da listbox
btn.place(x=10, y=350)

# colocar um botão 'Remover imagem' abaixo do botão 'Selecionar imagem' com a mesma width
btn2 = tk.Button(window, text='Remover imagem', width=42, height=2)
#posicionar o botão abaixo do botão 'Selecionar imagem'
btn2.place(x=10, y=400)

# colocar um outro container ao lado da listbox com a mesma height
container = tk.Frame(window, width=400, height=300, relief='sunken', borderwidth=5)
container.grid(row=0, column=1)
container.place(x=400, y=10)


# colocar um canvas dentro do container inferior com a mesma width e height
canvas = tk.Canvas(container, width=350, height=260, relief='sunken', borderwidth=5)
canvas.place(x=10, y=10)

# colocar quatro botões abaixo container de navegação
# botão com icone '<<' avança para a primeira imagem
btn3 = tk.Button(window, text='<<', width=10, height=2, relief='raised', borderwidth=5)
btn3.place(x=400, y=320)

# botão com icone '<' avança para a imagem anterior
btn4 = tk.Button(window, text='<', width=10, height=2, relief='raised', borderwidth=5)
btn4.place(x=500, y=320)

# botão com icone '>' avança para a próxima imagem
btn5 = tk.Button(window, text='>', width=10, height=2, relief='raised', borderwidth=5)
btn5.place(x=600, y=320)

# botão com icone '>>' avança para a última imagem
btn6 = tk.Button(window, text='>>', width=10, height=2, relief='raised', borderwidth=5)
btn6.place(x=700, y=320)

def select_image():
    # abre uma janela para selecionar uma imagem no caminho da pasta 'images'
    path = filedialog.askopenfilename(initialdir='images')
    # adiciona o caminho da imagem selecionada na listbox
    listbox.insert(tk.END, path)
    # adiciona a imagem selecionada no canvas
    canvas.image = tk.PhotoImage(file=path)
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')
    # imagem com mesmo tamanho do canvas
    canvas.config(width=canvas.image.width(), height=canvas.image.height())
    # centralizar a imagem no canvas
    canvas.place(x=(350-canvas.image.width())/2, y=(260-canvas.image.height())/2)
        


def view_image():
    #percorre a listbox e mostra a imagem selecionada
    for i in listbox.curselection():
        # adiciona a imagem selecionada no canvas
        canvas.image = tk.PhotoImage(file=listbox.get(i))
        canvas.create_image(0, 0, image=canvas.image, anchor='nw')
        # imagem com mesmo tamanho do canvas
        canvas.config(width=canvas.image.width(), height=canvas.image.height())
        # centralizar a imagem no canvas
        canvas.place(x=(350-canvas.image.width())/2, y=(260-canvas.image.height())/2)
    # se não houver imagem selecionada, mostra canvas vazio        
    if len(listbox.curselection()) == 0:
        canvas.image = tk.PhotoImage(file='')
        canvas.create_image(0, 0, image=canvas.image, anchor='nw')
        # imagem com mesmo tamanho do canvas
        canvas.config(width=canvas.image.width(), height=canvas.image.height())
        # centralizar a imagem no canvas
        canvas.place(x=(350-canvas.image.width())/2, y=(260-canvas.image.height())/2)


def remove_image():
    # remove a imagem selecionada na listbox
    listbox.delete(tk.ANCHOR)


def navigate_first():
    # navega para a primeira imagem
    listbox.selection_clear(0, tk.END)
    listbox.selection_set(0)
    view_image()


def navigate_previous():
    # navega para a imagem anterior
    if len(listbox.curselection()) > 0:
        listbox.selection_clear(0, tk.END)
        listbox.selection_set(listbox.curselection()[0]-1)
        view_image()

def navigate_next():
    # navega para a próxima imagem
    if len(listbox.curselection()) > 0:
        listbox.selection_clear(0, tk.END)
        listbox.selection_set(listbox.curselection()[0]+1)
        view_image()


def navigate_last():
    # navega para a última imagem
    listbox.selection_clear(0, tk.END)
    listbox.selection_set(tk.END)
    view_image()


# associar o botão 'Selecionar imagem' com a função select_image
btn.config(command=select_image)
# associar o botão 'Remover imagem' com a função remove_image
btn2.config(command=remove_image)
# associar a função view_image ao evento de selecionar uma imagem na listbox
listbox.bind('<<ListboxSelect>>', lambda x: view_image())
# associar a função navigate_first ao botão '<<'
btn3.config(command=navigate_first)
# associar a função navigate_previous ao botão '<'
btn4.config(command=navigate_previous)
# associar a função navigate_next ao botão '>'
btn5.config(command=navigate_next)
# associar a função navigate_last ao botão '>>'
btn6.config(command=navigate_last)

window.mainloop()