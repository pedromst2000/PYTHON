import tkinter as tk
from tkinter import filedialog, messagebox
import tkinter.ttk as ttk
import random


# Tkinter app setup
app = tk.Tk()
app.title("Adivinha o País")
app.geometry("1200x900")

# Load the images
europa_img = tk.PhotoImage(file="testeTk\Europa.png")
america_img = tk.PhotoImage(file="testeTk\America.png")
asia_img = tk.PhotoImage(file="testeTk\Asia.png")

images = [europa_img, america_img, asia_img]
current_img = 0


# Tab Control
tab_control = tk.ttk.Notebook(app)
tab_control.pack(fill=tk.BOTH, expand=1)

# Temas tab
temas_tab = tk.Frame(tab_control)
AdivinhaPalavraTab = tk.Frame(tab_control)
tab_control.add(temas_tab, text="Temas")
tab_control.add(AdivinhaPalavraTab, text="Adivinha Palavra")

# Canvas for images
canvas = tk.Canvas(temas_tab, width=200, height=200)
canvas.place(x=100, y=100)

currentFile = ""
# File dialog button
def open_file_dialog():
    global file_path, currentFile
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")], title="Selecione Ficheiro de Texto", initialdir="testeTk")
    filename = file_path.split("/")[-1].split(".")[0]
    file_label.config(text=filename)
    currentFile = file_path
    

def injectCountries():
    if currentFile == "":
        messagebox.showerror("Error", "You did not select a file yet!")
        return
    with open(currentFile, "r") as file:
        content = file.read().split("\n")
        for item in content:
            if item not in listbox.get(0, tk.END):
                listbox.insert(tk.END, item)
            else:
                messagebox.showerror("Erro", "País já existe na lista")


def adicionarPais():
    if novoPaisEntry.get() == "":
        messagebox.showerror("Error", "A entry está vazia!")
        return
    
    for pais in listbox.get(0, tk.END):
        if novoPaisEntry.get() == pais:
            messagebox.showerror("Error", "O pais ja existe na listbox")
            return
    
    listbox.insert(tk.END, novoPaisEntry.get())

            

file_dialog_button = tk.Button(temas_tab, text="Selecionar Ficheiro", command=open_file_dialog)
file_dialog_button.place(x=100, y=300)

temaLabel = tk.Label(temas_tab, text="Tema")
temaLabel.place(x=100, y=400)

file_label = tk.Label(temas_tab, relief="sunken", bg="white", width=20)
file_label.place(x=140, y=400)

injectCountries = tk.Button(temas_tab, text=">", width=5, height=15, bg="light gray", command=injectCountries)
injectCountries.place(x=450, y=280)

# Listbox for file content
listbox = tk.Listbox(temas_tab, height=15)
listbox.place(x=600, y=280)

nomePaisLabel = tk.Label(temas_tab, text="Nome de Pais")
nomePaisLabel.place(x=550, y=100)

novoPaisEntry = tk.Entry(temas_tab, width=15)
novoPaisEntry.place(x=650, y=100)

adicionarBtn = tk.Button(temas_tab, text="Adicionar", command=adicionarPais)
adicionarBtn.place(x=600, y=150)

# Image cycle
def update_image():
    global current_img
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=tk.NW, image=images[current_img])
    current_img = (current_img + 1) % 3
    temas_tab.after(3000, update_image)

update_image()


#Adivinha paises Tab
currentContinent = ""
currentCountry = ""
hiddenCountry = []
def getContinent(event):
    global currentContinent, currentCountry
    continent = comboBox.get()

    with open(f"{continent}.txt", "r") as file:
        countries = file.readlines()

        currentCountry = random.choice(countries).strip()
        


def randomCountry():
    global hiddenCountry  
    for i in range(len(currentCountry)):
        hiddenCountry.append(i)
        print(hiddenCountry)
        selectedCountryLabel.config(text=hiddenCountry)


def validate():
    
    guess = answerEntry.get()

    if guess in currentCountry:
        # ATRIBUI UM KEY VALUE OU SEJA (0:A), (1:B) 
        for i, letter in enumerate(currentCountry):
            if letter == guess:
                hiddenCountry[i] = letter
        selectedCountryLabel.config(text=hiddenCountry)
    answerEntry.delete(0, "end")
    win()
            
def win():
    # LOOKS THROUGH ALL THE ELEMENTS IN HIDDENCOUNTRY LIST IF THERE IS ANY DIGIT (INT) IT PASSES IF NOT THE WORD IS COMPLETED AND A MESSAGE IS SHOWN
    if any(char.isdigit() for char in hiddenCountry):
        return
    else:
        messagebox.showinfo("Congratulations", "You have guessed the country correctly")
        selectedCountryLabel.config(text="")


temaLabelGame = tk.Label(AdivinhaPalavraTab, text="Tema")
temaLabelGame.place(x=200, y=100)


Continent = tk.StringVar(AdivinhaPalavraTab, "Europa")
comboBox = ttk.Combobox(AdivinhaPalavraTab, textvariable=Continent)

comboBox["values"] = ("Europa", "America", "Asia")

comboBox.place(x=300, y=100)

randomCountry = tk.Button(AdivinhaPalavraTab, text="Sortear Pais", command=randomCountry)
randomCountry.place(x=450, y=100)

selectedCountryLabel = tk.Label(AdivinhaPalavraTab, width=15, relief="sunken", bg="white")
selectedCountryLabel.place(x=300, y=200)


answerLabel = tk.Label(AdivinhaPalavraTab, text="Letra pedida:")
answerLabel.place(x=200, y=300)

answerEntry = tk.Entry(AdivinhaPalavraTab, width=5)
answerEntry.place(x=300, y=300)

validateBtn = tk.Button(AdivinhaPalavraTab, text="Validar", command=validate)
validateBtn.place(x=400, y=300)

comboBox.bind('<<ComboboxSelected>>', getContinent)
app.mainloop()
