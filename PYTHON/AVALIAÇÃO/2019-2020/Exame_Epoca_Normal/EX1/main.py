import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import StringVar

Window = tk.Tk()
Window.title("ESMAD| Plug-IN")
Window.geometry("1000x500")

# menu bar
menubar = tk.Menu(Window)
Window.config(menu=menubar)
# opção Plug-In: Empresas
menu_plug_in = tk.Menu(menubar)
menubar.add_cascade(label="Plug-In", menu=menu_plug_in)

# label 'Evento Plug-In'
label_evento = tk.Label(Window, text="Evento Plug-In", font=("Arial", 20))
label_evento.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# canvas
canvas = tk.Canvas(Window, width=500, height=300, relief='raised', bg='white')
canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

img1 = tk.PhotoImage(file="images/imagem3.png")
canvas.create_image(10, 190, anchor=tk.NW, image=img1)

img2 = tk.PhotoImage(file="images/imagem2.png")
canvas.create_image(20, 120, anchor=tk.NW, image=img2)

img3 = tk.PhotoImage(file="images/imagem1.png")
canvas.create_image(0, 0, anchor=tk.NW, image=img3)


def sair():
    if messagebox.askyesno("Plug-In", "Confirma saída?"):
        Window.destroy()


menubar.add_command(label="Sair", command=sair)

# selecionar a opção do menu Plug-In: Empresas
def menu_empresas():    
    # criar a janela Empresas
    janela_empresas = tk.Toplevel()
    janela_empresas.title("ESMAD| Plug-IN - Empresas")
    janela_empresas.geometry("1000x500")

    # label 'Empresas'
    label_empresas = tk.Label(janela_empresas, text="Empresa")
    label_empresas.place(x=10, y=10)

    entry_empresas = tk.Entry(janela_empresas, width=20)
    entry_empresas.place(x=70, y=10)

    # label 'Perfil'
    label_perfil = tk.Label(janela_empresas, text="Perfil")
    label_perfil.place(x=10, y=70)

    lista_perfis = []

    file = open("files/perfil.txt", "r", encoding="utf-8")

    lines = file.readlines()

    for line in lines:
        lista_perfis.append(line)
    
    file.close()

    # combobox 'Perfil'
    combo_perfil = ttk.Combobox(janela_empresas, width=22, height=130, values=lista_perfis)
    combo_perfil.place(x=70, y=70)

    # apresentar por defeito o primeiro perfil da lista
    combo_perfil.current(0)

    # container com title 'Cursos'
    container_cursos = tk.LabelFrame(janela_empresas, text="Cursos", width=300, height=150)
    container_cursos.place(x=10, y=130)

    selected = StringVar()
    selected.set("TSIW")

    # radiobutton 'TSIW'
    radio_tsiw = tk.Radiobutton(container_cursos, text="TSIW", value="TSIW", variable=selected)
    radio_tsiw.place(x=10, y=10)

    # radiobutton 'Design'
    radio_design = tk.Radiobutton(container_cursos, text="Design", value="Design", variable=selected)
    radio_design.place(x=10, y=40)

    # radiobutton 'Multimédia'
    radio_multimedia = tk.Radiobutton(container_cursos, text="Multimédia", value="Multimédia", variable=selected)
    radio_multimedia.place(x=10, y=70)

    # radiobutton 'TCAV'
    radio_tcav = tk.Radiobutton(container_cursos, text="TCAV", value="TCAV", variable=selected)
    radio_tcav.place(x=10, y=100)

    # selecionar a opção TSIW por defeito
    radio_tsiw.select()

    btn_add = tk.Button(janela_empresas, text="adicionar", width=15, height=2)
    btn_add.place(x=10, y=300)  

    # botão 'Remover'
    btn_remove = tk.Button(janela_empresas, text="remover", width=15, height=2)
    btn_remove.place(x=130, y=300)

    # botão 'Guardar'
    btn_save = tk.Button(janela_empresas, text="guardar", width=15, height=2)
    btn_save.place(x=250, y=300)

    # treeview com colunas 'Empresa' 'Perfil' 'Curso'
    treeview = ttk.Treeview(janela_empresas, columns=("Empresa", "Perfil", "Curso"), show="headings", height=10)
    treeview.place(x=400, y=10)

    treeview.heading("Empresa", text="Empresa")
    treeview.heading("Perfil", text="Perfil")
    treeview.heading("Curso", text="Curso")

    # definir o tamanho das colunas
    treeview.column("Empresa", width=180)
    treeview.column("Perfil", width=180)
    treeview.column("Curso", width=180)

    # apresenta o contéudo do ficheiro 'plug-in.txt' no treeview
    file = open("files/plug-in.txt", "r", encoding="utf-8")

    lines = file.readlines()

    for line in lines:
        line = line.strip()
        line = line.split(";")

        treeview.insert("", tk.END, values=line)

    file.close()


    scroll = ttk.Scrollbar(janela_empresas, orient="vertical", command=treeview.yview)
    scroll.place(x=950, y=10, height=200)

    treeview.configure(yscrollcommand=scroll.set)

    def adicionar():
        # obter os valores dos campos de texto
        empresa = entry_empresas.get()
        print(f'Empresa: {empresa}')
        perfil = combo_perfil.get()
        print(f'Perfil: {perfil}')
        curso = selected.get()
        print(f'Curso: {curso}')

        # validar se os campos de texto estão preenchidos
        if empresa == "" or perfil == "" or curso == "":
            return messagebox.showerror("Erro", "Preencha todos os campos!")
        
        # adicionar os valores dos campos de texto ao treeview
        treeview.insert("", tk.END, values=(empresa, perfil, curso))


        # limpar os campos de texto
        entry_empresas.delete(0, tk.END)
        combo_perfil.delete(0, tk.END)
        radio_tsiw.select()
        contar_empresas()
    
    btn_add.config(command=adicionar)


    def remover():
       
       if messagebox.askyesno("Plug-In", "Confirma eliminação?"):
        # remover o item selecionado no treeview
        item = treeview.selection()[0]
        treeview.delete(item)
        contar_empresas()

    btn_remove.config(command=remover)    
        

    def guardar():
       # guardar o conteúdo do treeview no ficheiro 'plug-in.txt'
        file = open("files/plug-in.txt", "w", encoding="utf-8")

        for item in treeview.get_children():
            empresa = treeview.item(item, "values")[0]
            perfil = treeview.item(item, "values")[1]
            curso = treeview.item(item, "values")[2]

            file.write("\n" + empresa + ";" + perfil + ";" + curso)

        file.close()

    
    btn_save.config(command=guardar)

    # label 'Nº de Empresas:'
    label_num_empresas = tk.Label(janela_empresas, text="Nº de Empresas:")
    label_num_empresas.place(x=400, y=300)
    
    def contar_empresas():
        # conta o número de empresas no treeview
        num_empresas = len(treeview.get_children())
        print(f'Nº de Empresas: {num_empresas}')

        # apresenta o número de empresas no label 'Nº de Empresas:'
        label_num_empresas["text"] = "Nº de Empresas: " + str(num_empresas)

    contar_empresas()
    

    # canvas
    canvas2 = tk.Canvas(janela_empresas, width=300, height=180, relief='raised', bg='white')
    canvas2.place(x=700, y=270)

    # label "Patricinadores" 
    label_patrocinadores = tk.Label(janela_empresas, text="Patrocinadores", font=("Arial", 12))
    label_patrocinadores.place(x=700, y=470)

    # colocar as imagens no canvas de forma aleatória a cada 3 segundos
    def imagens():

    # colocar a imagem 1 no canvas
        canvas2.create_image(10, 10, anchor=tk.NW, image=img1)

    # temporizadores para colocar as imagens no canvas
        canvas2.after(3000, lambda: canvas2.create_image(10, 10, anchor=tk.NW, image=img2))
        canvas2.after(6000, lambda: canvas2.create_image(10, 10, anchor=tk.NW, image=img3))

    # repetir a função imagens a cada 6 segundos
        canvas2.after(9000, imagens)


    imagens()

menu_plug_in.add_command(label="Empresas", command=menu_empresas)

# selecionar a opção do menu Plug-In: Perfis
def menu_perfis():
    # criar a janela Perfis
    janela_perfis = tk.Toplevel()
    janela_perfis.title("ESMAD| Plug-IN - Perfis")
    janela_perfis.geometry("1000x500")

    # label 'Perfil'
    label_perfil = tk.Label(janela_perfis, text="Perfil")
    label_perfil.place(x=10, y=10)

    # entry 'Perfil'
    entry_perfil = tk.Entry(janela_perfis, width=20)
    entry_perfil.place(x=70, y=10)


    # listbox com os perfis
    listbox = tk.Listbox(janela_perfis, width=32, height=15)
    listbox.place(x=70, y=70)

    # estrutura try catch para verificar se o ficheiro 'perfil.txt' existe para aplicação não crashar
    try:
        # apresentar o conteúdo do ficheiro 'perfil.txt' na listbox
        file = open("files/perfil.txt", "r", encoding="utf-8")

        lines = file.readlines()

        for line in lines:
            line = line.strip()
            listbox.insert(tk.END, line)
        
        file.close()
    except:
        # se o ficheiro 'perfil.txt' não existir apresenta uma mensagem de erro
        messagebox.showerror("Plug-In", "Não existem perfis!")
        
    # botão 'Adicionar'
    btn_add = tk.Button(janela_perfis, text="adicionar", width=15, height=2)
    btn_add.place(x=300, y=100)

    # botão 'Remover'
    btn_remove = tk.Button(janela_perfis, text="remover", width=15, height=2)
    btn_remove.place(x=300, y=150)

    # botão 'Guardar'
    btn_save = tk.Button(janela_perfis, text="guardar", width=15, height=2)
    btn_save.place(x=300, y=200)

    def adicionar():
        # obter o valor do campo de texto
            perfil = entry_perfil.get()
            print(f'Perfil: {perfil}')
        # se o perfil já existir na listbox apresenta uma mensagem de erro
            if perfil in listbox.get(0, tk.END):
                return messagebox.showerror("Plug-In", "Perfil já existe!")
        # se o perfil não existir na listbox adiciona o perfil à listbox
            listbox.insert(tk.END, perfil)
        # limpar o campo de texto
            entry_perfil.delete(0, tk.END)


    btn_add.config(command=adicionar)


    def remover():
        # obter o perfil selecionado na listbox
        perfil = listbox.get(tk.ACTIVE)
        print(f'Perfil: {perfil}')
        # remover o perfil selecionado na listbox
        listbox.delete(tk.ACTIVE)

    btn_remove.config(command=remover)

    def guardar():
        # guardar o conteúdo da listbox no ficheiro 'perfil.txt'
        file = open("files/perfil.txt", "w", encoding="utf-8")

        for perfil in listbox.get(0, tk.END):
            file.write(perfil + "\n")
        
        file.close()

    btn_save.config(command=guardar)

menu_plug_in.add_command(label="Perfis", command=menu_perfis)

Window.mainloop()
