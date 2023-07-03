# libraries
import tkinter as tk
import os
from tkinter import messagebox

# implementar uma pequena aplicação que inclua um componente de texto e três botões
window = tk.Tk()

# tamanho da janela
window.geometry("700x600")
window.title("Form1")

#Botão Guardar Ficheiro
btnSaveFile = tk.Button(window, text="Guardar Ficheiro", fg="blue", relief="raised", borderwidth=5)
btnSaveFile.place(x=20, y=40, width=200, height=50)

#Botão Limpar
btnClean = tk.Button(window, text="Limpar", fg="blue", relief="raised", borderwidth=5)
# tamanho do botão canto superior esquerdo da janela abaixo 5cm num retangulo perfeio
btnClean.place(x=20, y=180, width=200, height=50)

# Botão Ler Ficheiro
btnReadFile = tk.Button(window, text="Ler ficheiro", fg="blue",                     relief="raised", borderwidth=5)
# tamanho do botão canto superior esquerdo da janela abaixo 5cm num retangulo perfeio
btnReadFile.place(x=20, y=320, width=200, height=50)

# definir uma caixa de texto ao lado dos botões centrado
txt = tk.Text(window, width=50, height=20)
txt.place(x=250, y=40, width=400, height=500)

# Botão para fechar a janela
btnClose = tk.Button(window, text="Fechar", fg="blue", relief="raised", borderwidth=5)
# tamanho do botão canto superior esquerdo da janela abaixo 5cm num retangulo perfeio
btnClose.place(x=20, y=460, width=200, height=50)

# DEFINIÇÃO DAS FUNÇÕES PARA OS BOTÕES
# função para o botão guardar ficheiro
def save_file():
    # verificar se o ficheiro existe
    if os.path.isfile("ficheiro.txt"):
        # se existir, abrir o ficheiro em modo de escrita
        f = open("ficheiro.txt", "w")
        # escrever o conteúdo da caixa de texto no ficheiro
        f.write(txt.get("1.0", "end"))
        # fechar o ficheiro
        f.close()
    # se não existir, criar o ficheiro e escrever o conteúdo da caixa de texto
    else:
        f = open("ficheiro.txt", "x")
        f.write(txt.get("1.0", "end"))
        f.close()
    

# função para limpar a caixa de texto
def clean():
    txt.delete("1.0", "end")

# função para ler o ficheiro e mostrar o seu conteúdo na caixa de texto
def read_file():
    # verificar se o ficheiro existe
    if os.path.isfile("ficheiro.txt"):
        # se existir, abrir o ficheiro em modo de leitura
        f = open("ficheiro.txt", "r")
        # ler o conteúdo do ficheiro
        txt.insert("1.0", f.read())
        # fechar o ficheiro
        f.close()
    # se não existir, mostrar uma mensagem de erro
    else:
        txt.insert("1.0", "Ficheiro não existe!")


# função para fechar a janela
def close_window():
    # mostrar uma mensagem de confirmação
    if messagebox.askokcancel("Fechar", "Tem a certeza que pretende fechar a janela?"):
        # fechar a janela
        window.destroy()
    else:
        # não fechar a janela
        pass

# no clique do botão guardar ficheiro, chamar a função save_file
btnSaveFile.configure(command=save_file)
# no clique do botão limpar, chamar a função clean
btnClean.configure(command=clean)
# no clique do botão ler ficheiro, chamar a função read_file
btnReadFile.configure(command=read_file)
# no clique do botão fechar, chamar a função close_window
btnClose.configure(command=close_window)

window.mainloop()