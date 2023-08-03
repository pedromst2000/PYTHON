import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import StringVar
import os
from datetime import date
from datetime import datetime

# Aplicação para monitorizar as presenças numa sala de aula

# main window
root = tk.Tk()
root.title("Gestão de Presenças")
root.geometry("800x600")
root.resizable(False, False)

# menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# menu Movimentos
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Movimentos", menu=filemenu)

# menu Consulta
consultMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Consultas", menu=consultMenu)

# Menu Sair
exitMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Sair", menu=exitMenu)

# colocar um canvas no canto superior esquerdo
canvas = tk.Canvas(root, width=500, height=593, relief="sunken", borderwidth=1)
canvas.grid(row=0, column=0)

# colocar uma imagem no canvas através da pasta images
img = tk.PhotoImage(file="images/images.png")
# colocar a imagem no canvas
canvas.create_image(0, 0, anchor="nw", image=img)


# colocar um label ao lado do canvas centrado com texto a azul 'Gestão de Presenças'
label = tk.Label(root, text="Gestão de Presenças", font=("Arial", 20), fg="blue")
# posicionar o label centradamente ao lado do canvas
label.place(x=650, y=250, anchor="center")

# opção movimentos do menu
def movimentos():
    # window
    movimentos = tk.Toplevel()
    # manter window principal bloqueada
    movimentos.grab_set()
    movimentos.title("Entradas e Saidas")
    movimentos.geometry("800x400")
    movimentos.resizable(False, False)
    # label no canto superior esquerdo 'Número de Estudante' 
    labelMov = tk.Label(movimentos, text="Número de Estudante:", font=("Arial", 10))
    labelMov.grid(row=0, column=0, padx=10, pady=10)
    # entry ao lado do label
    entryMov = tk.Entry(movimentos, width=20)
    entryMov.grid(row=0, column=1, padx=10, pady=10)
    # container com título 'Movimentos' abaixo do label e entry
    containerMov = tk.LabelFrame(movimentos, relief='sunken', borderwidth=4, text="Movimentos", width=200, height=100)
    containerMov.config(fg="blue")
    containerMov.place(x=20, y=60)
    # variavel de seleção
    selectedMov = StringVar() 
    selectedMov.set("entrada")
    # radioButton 'entrada'
    radio1 = tk.Radiobutton(containerMov, text="Entrada", value="Entrada", variable=selectedMov)
    radio1.place(x=10, y=10)
    # radioButton 'saída'
    radio2 = tk.Radiobutton(containerMov, text="Saída", value="Saída", variable=selectedMov)
    radio2.place(x=10, y=40)
    # button Registar
    buttonRegister = tk.Button(movimentos, text="Registar", width=10, height=3)
    buttonRegister.place(x=250, y=80)
    # label 'Histórico de Movimentos'
    labelMovHist = tk.Label(movimentos, text="Histórico de Movimentos", font=("Arial", 10), fg="blue")
    labelMovHist.place(x=540, y=10)
    # container 'Histórico de Movimentos'
    containerMovHist = tk.Listbox(movimentos, relief='sunken', borderwidth=4, width=50, height=15)
    containerMovHist.config(fg="blue")
    containerMovHist.place(x=450, y=60)

    # apresentar na listbox os movimentos registados
    # se não existir o ficheiro acessos.txt, criar o ficheiro acessos.txt na pasta files 
    if not os.path.exists("files/acessos.txt"):
        file = open("files/acessos.txt", "w")
        file.close()
    # ler o ficheiro acessos.txt
    file = open("files/acessos.txt", "r", encoding="utf-8")
    # percorrer o ficheiro acessos.txt
    for line in file:
        # apresentar na listbox os movimentos registados com formato do ficheiro
        containerMovHist.insert(tk.END, line.strip('\n'))
        # apresentar em preto os movimentos registados
        containerMovHist.itemconfig(tk.END, fg="black")
        
    file.close()

    def register():
        # ler o valor da entry 'número de estudante'
        numEstudante = entryMov.get()
        # ler o valor do radioButton 'entrada' ou 'saída'
        movimento = selectedMov.get()
        # se o número de estudante for vazio
        if numEstudante == "":
            # apresentar a mensagem de erro na window movimentos
            msg.showerror("Erro", "Número de Estudante inválido!")
        # se o número de estudante não apresentar somente digitos
        elif not numEstudante.isdigit():
            msg.showerror("Erro", "Número de Estudante inválido!")
        # se o número de estudante for menor que 0
        elif int(numEstudante) < 0:
            msg.showerror("Erro", "Número de Estudante inválido!")
        # se o número de estudante for maior que 999999999
        elif int(numEstudante) > 999999999:
            msg.showerror("Erro", "Número de Estudante inválido!")
        else :
            file = open("files/acessos.txt", "r")
            for line in file:
                # verificar se o estudante já efetuou uma entrada 
                if numEstudante in line and movimento == "Entrada":
                    # apresentar a mensagem de erro na window movimentos
                    msg.showerror("Erro", "Estudante já efetuou uma entrada!")
                    # não adicionar ao ficheiro acessos.txt o número de estudante; data do sistema; hora do sistema; entrada ou saída
                    break
                # verificar se o estudante já efetuou uma saída
                elif numEstudante in line and movimento == "Saída":
                    # apresentar a mensagem de erro na window movimentos
                    msg.showerror("Erro", "Estudante já efetuou uma saída!")
                    break
               # verificar se o estudante pode efetuar uma saída sem ter efetuado uma entrada
                elif numEstudante not in line and movimento == "Saída":
                # apresentar a mensagem de erro na window movimentos
                    msg.showerror("Erro", "Estudante não efetuou uma entrada!")
                    break
            else:
                # adicionar ao ficheiro acessos.txt o número de estudante; data do sistema; hora do sistema; entrada ou saída
                file = open("files/acessos.txt", "a")
                file.write(numEstudante + ";" + str(date.today()) + ";" + str(datetime.now().strftime("%H:%M:%S")) + ";" + movimento + "\n")
                # apresentar na listbox os movimentos registados com formato do ficheiro
                containerMovHist.insert(tk.END, numEstudante + ";" + str(date.today()) + ";" + str(datetime.now().strftime("%H:%M:%S")) + ";" + movimento)
                # atribuir cor preta ao texto da listbox
                containerMovHist.config(fg="black")
                # se o movimento for entrada
                if movimento == "Entrada":
                    # atribuir cor verde ao texto da listbox
                    containerMovHist.itemconfig(tk.END, fg="green")
                # se o movimento for saída
                elif movimento == "Saida":
                    # atribuir cor vermelha ao texto da listbox
                    containerMovHist.itemconfig(tk.END, fg="red")

                file.close()
    
    # associar o button 'Registar' à função register
    buttonRegister.config(command=register)


# opção consultas do menu
def consultas():
    # window
    consultas = tk.Toplevel()
    consultas.title("Consultas")
    consultas.geometry("800x390")
    consultas.resizable(False, False)

    container = tk.Canvas(consultas, width=200, height=350, relief='sunken', borderwidth=4)
    container.place(x=0, y=0)

    # container com a label 'Tipo de Movimento'
    containerMov = tk.LabelFrame(consultas, text="Tipo de Movimento", width=180, height=120, fg="blue", relief='sunken', borderwidth=4)
    containerMov.place(x=10, y=30)

    selectedMov = tk.IntVar()
    selectedMov.set("Entrada")

    # checkbox 'Entrada' no containerMov
    checkboxEntrada = tk.Checkbutton(containerMov, text="Entrada", variable=selectedMov)
    checkboxEntrada.place(x=10, y=10)

    # checkbox 'Saída' no containerMov
    checkboxSaida = tk.Checkbutton(containerMov, text="Saída", variable=selectedMov)
    checkboxSaida.place(x=10, y=40)

    # container com a label 'Por Utilizador' com cor azul com a mesma largura e altura do container 'Tipo de Movimento'
    containerUser = tk.LabelFrame(consultas, text="Por Utilizador", width=180, height=120, fg="blue", relief='sunken', borderwidth=4)
    containerUser.place(x=10, y=160)

    # label dentro do containerUser com o texto 'Número :' com cor preta
    labelNum = tk.Label(containerUser, text="Número :", fg="black")
    labelNum.place(x=10, y=10)
    # input do número de estudante dentro do containerUser
    entryNum = tk.Entry(containerUser, width=20)
    entryNum.place(x=10, y=30)
    entryNum.insert(0, "0")

    # botão 'Consultar' 
    buttonConsult = tk.Button(consultas, text="Consultar", fg="black")
    buttonConsult.place(x=10, y=300, width=180, height=40)

    containerMovHist = tk.LabelFrame(consultas, width=550, height=360, fg="blue", relief='sunken', borderwidth=4)
    containerMovHist.place(x=220, y=0)

    # treeview 4x4 no containerMovHist
    # colunas 'Número', 'Data', 'Hora', 'Movimento'
    tree = ttk.Treeview(containerMovHist, columns=("Número", "Data", "Hora", "Movimento"), show="headings")
    # tamanho das colunas
    tree.column("Número", width=120, anchor='c')
    tree.column("Data", width=120, anchor='c')
    tree.column("Hora", width=100, anchor='c')
    tree.column("Movimento", width=200, anchor='c')
    # nome das colunas
    tree.heading("Número", text="Número")
    tree.heading("Data", text="Data")
    tree.heading("Hora", text="Hora")
    tree.heading("Movimento", text="Movimento")
    # posição da treeview
    tree.place(x=0, y=0)
    # altura da treeview
    tree.place(height=340)

    # função para consultar os movimentos
    def consult():
        # valor do checkbox selecionado
        movimento = str(selectedMov.get())
        # valor do número de estudante
        numEstudante = str(entryNum.get())
        # apresentar na treeview o tipo de movimento selecionado e o número de estudante
        tree.delete(*tree.get_children())
        # abrir o ficheiro acessos.txt
        file = open("files/acessos.txt", "r", encoding="utf-8")
        # ler o ficheiro acessos.txt
        for line in file:
            # verificar se o número de estudante está no ficheiro acessos.txt
            if numEstudante in line:
                # verificar se o movimento selecionado está no ficheiro acessos.txt
                if movimento in line:
                    # apresentar na treeview os movimentos registados com formato do ficheiro
                    tree.insert("", tk.END, values=(line.split(";")[0], line.split(";")[1], line.split(";")[2], line.split(";")[3]))
            # se não estiver nenhum número de estudante no ficheiro acessos.txt
            elif numEstudante == "":
                # apresentar na treeview os movimentos registados com formato do ficheiro
                tree.insert("", tk.END, values=(line.split(";")[0], line.split(";")[1], line.split(";")[2], line.split(";")[3]))

        file.close()

    # associar o button 'Consultar' à função consult
    buttonConsult.config(command=consult)

# opção sair do menu
def sair():
    if msg.askyesno("Sair", "Deseja sair?"):
        root.destroy()


filemenu.add_command(label="Entradas e Saidas", command=movimentos)
consultMenu.add_command(label="Abrir", command=consultas)
exitMenu.add_command(label="Sair", command=sair)

root.mainloop()