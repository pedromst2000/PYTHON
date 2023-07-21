from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import Canvas
from tkinter.messagebox import *

# THIS FUNCTION READS CHEKS IF THE CHECK BUTTONS ARE ACTIVATED IF THEY ARE IT READS THROUGH THE FILES OF THE ACTIVATED ONES AND INJECTS EACH LINE INTO THE TREEVIEW IT ALSO UPDATES THE ENTRY WITH THE TOTAL AMOUNT OF LINES IN THE TREEVIEW
def search():
    treeView.delete(*treeView.get_children())
    numProvasEntry.delete("1.0","end")
    favoriteList.delete(1,"end")
    if trailCurto.get():
       with open("test\TKINTER/trails.txt", "r") as file:
        trails = file.readlines()
        for trail in trails:
            linha = trail.split(";")
            treeView.insert('', tk.END, values=linha)

    if ultraTrail.get():
        with open("test\TKINTER/ultratrails.txt", "r") as file:
            trails = file.readlines()
            for trail in trails:
                linha = trail.split(";")
                treeView.insert('', tk.END, values=linha)
            
    numProvasEntry.insert("end", len(treeView.get_children()))

    with open("test\TKINTER/favorites.txt", "r") as file:
        favorites = file.readlines()
        for favorite in favorites:
            if favorite.split(";")[0] == favorite:
                pass
            else:
                favoriteList.insert("end", favorite.split(";")[0])

# THIS FUNCTION TAKES ALL THE ITEMS IN THE TREEVIEW AND SORTS THEM IN ASCENDING ORDER BASED ON A SPECIFIC COLUMN IN THIS CASE THE THIRD ONE (INDEX = 2)
def sort_ascending():
    treeView.delete(*treeView.get_children())
    numProvasEntry.delete("1.0","end")
    
    # sort the data and insert it into the treeview
    data = []
    if trailCurto.get():
        with open("test\TKINTER/trails.txt", "r") as file:
            trails = file.readlines()
            for trail in trails:
                linha = trail.split(";")
                data.append(linha)

    if ultraTrail.get():
        with open("test\TKINTER/ultratrails.txt", "r") as file:
            trails = file.readlines()
            for trail in trails:
                linha = trail.split(";")
                data.append(linha)
    data.sort(key=lambda x: x[2])
    for linha in data:
        treeView.insert('', tk.END, values=linha)

    numProvasEntry.insert("end", len(treeView.get_children()))


# THIS FUNCTION TAKES ALL THE ITEMS IN THE TREEVIEW AND SORTS THEM IN DESCENDING ORDER BASED ON A SPECIFIC COLUMN IN THIS CASE THE THIRD ONE (INDEX = 2)
def sort_descending():
    treeView.delete(*treeView.get_children())
    numProvasEntry.delete("1.0","end")
    
    # sort the data and insert it into the treeview
    data = []
    if trailCurto.get():
        with open("test\TKINTER/trails.txt", "r") as file:
            trails = file.readlines()
            for trail in trails:
                linha = trail.split(";")
                data.append(linha)

    if ultraTrail.get():
        with open("test\TKINTER/ultratrails.txt", "r") as file:
            trails = file.readlines()
            for trail in trails:
                linha = trail.split(";")
                data.append(linha)
    data.sort(key=lambda x: x[2], reverse=True)
    for linha in data:
        treeView.insert('', tk.END, values=linha)

    numProvasEntry.insert("end", len(treeView.get_children()))


# THIS FUNCTION TAKES THE SELECTED TRAIL FROM THE TREEVIEW AND ADDS IT TO THE FAVORITE LIST BOX
def addFavorite():
    
    selection = treeView.selection()
    if len(selection) == 0:
        showinfo("Error", "Please select a trail first")
        return
    selected_item = treeView.item(selection[0])
    
    if selected_item["values"][0] not in favoriteList.get(0, tk.END):
        favoriteList.insert("end", selected_item["values"][0])
    else:
        showerror("Error", "That trail is already favorited!")

# THIS FUNCTION TAKES THE SELECTED ITEM IN THE TREEVIEW IF NOTHING IS SELECTED SHOWS AN ERROR IF SOMETHING IS SELECTED IT READS THE FILE AND WRITES ALL THE TRAILS THAT ARE NOT THE SELECTED ONE (REMOVES IT)
def removeFavorite():
    selection = favoriteList.curselection()
    if len(selection) == 0:
        showinfo("Error", "Please select a favorite trail first")
        return
    selected_item = favoriteList.get(selection[0])
    
    with open("test\TKINTER/favorites.txt", "r") as file:
        favorites = file.readlines()
        
    with open("test\TKINTER/favorites.txt", "w") as file:
        for favorite in favorites:
            if selected_item != favorite.split(";")[0]:
                file.write(favorite)
    
    favoriteList.delete(selection[0])


# THIS FUNCTION OPENS EXPLORER TO SELECT AN IMAGE AND INSERTS IT IN THE CANVAS
def select_image():
    file_path = filedialog.askopenfilename(title = "Select file", initialdir = "test\TKINTER/images",
              filetypes = (("png files","*.png"),("gif files", "*.gif"), ("all files","*.*")))
    image = PhotoImage(file=file_path)
    canvas.create_image(50, 50, image=image)
    canvas.itemconfig(canvas, image=image)


# THIS FUNCTION TAKES ITEMS FROM A LISTBOX AND SAVES THEM IN A FILE BUT ONLY IF THEY DON'T EXIST ALREADY
def saveFavorites():
    items = favoriteList.get(0, tk.END)
    existing_items = []
    with open("test\TKINTER/favorites.txt", "a+") as file:
        file.seek(0)
        existing_items = file.read().splitlines()
        for item in items:
            if item not in existing_items:
                file.write(item + "\n")

    
def show_value_count(tree, column):
    # TAKES ALL THE VALUES OF THE TREEVIEW AND THE COLUMN PASSED BY THE BUTTON AND CREATES A DICTIONARY WITH THE VALUE AND THE AMOUNT OF TIMES IT OCURS
    value_counts = {}
    for item in tree.get_children():
        value = tree.item(item, "values")[column]
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1

    # CREATES A MESSAGE THAT WRITES IN A SHOWINFO THE AMOUNT OF EACH VALUE THAT EXISTS
    message = "Value Counts:\n\n"
    for value, count in value_counts.items():
        if count < 2:
            message += f"There is {count} of type {value} \n\n"
        else:
            message += f"There are {count} of type {value} \n\n"
    showinfo("Value Count", message)

window = tk.Tk()
window.title("Trails App")
window.geometry("1000x500")


trailCurto = tk.IntVar()
ultraTrail = tk.IntVar()

checkButton1 = Checkbutton(window, text="Trail curto", variable=trailCurto)
checkButton1.select()
checkButton1.grid(row=0, column=0, pady=15)

checkButton2 = Checkbutton(window, text="Ultra trail", variable=ultraTrail)
checkButton2.grid(row=0, column=1, pady=15)

searchButton = Button(window, text="Search", command=search)
searchButton.grid(row=0, column=2)


treeView = ttk.Treeview(window, columns=("Prova", "Data", "Local"), show='headings')
treeView.grid(row=1, column=0, pady= 10)

numProvasLbl = Label(window, text="Nº de provas")
numProvasLbl.grid(row=2, column=0)

numProvasEntry = Text(window , width=5, height=1)
numProvasEntry.insert("end","0")
numProvasEntry.grid(row=2, column=1)

treeView.column("Prova", width= 150, anchor= "w")
treeView.column("Data", width= 100, anchor= "c")
treeView.column("Local", anchor= "c")
treeView.heading("Prova", text="Prova")
treeView.heading("Data", text="Data")
treeView.heading("Local", text="Local")


sortAscendingButton = Button(window, text="Sort Ascending", command=sort_ascending)
sortAscendingButton.grid(row=0, column=3)

sortDescendingButton = Button(window, text="Sort Descending", command=sort_descending)
sortDescendingButton.grid(row=0, column=4)

addFavoriteBtn = Button(window, text="Add Favorite", command=addFavorite)
addFavoriteBtn.grid(row=1, column=2)

removeFavoriteBtn = Button(window, text="Remove Favorite", command=removeFavorite)
removeFavoriteBtn.grid(row=2, column=2)

favoriteLbl = Label(window, text="Favorite")
favoriteLbl.grid(row=1, column=3)

favoriteList = Listbox(window)
favoriteList.grid(row=2, column=3)

saveButton = tk.Button(window, text="Save", command=saveFavorites)
saveButton.grid(row=2, column=4)

select_picture_button = ttk.Button(window, text="Select a picture", command=select_image)
select_picture_button.grid(row=3, column=0)

canvas = Canvas(window, height=200, width=200)
canvas.grid(row=3, column=1)

value_count_button = ttk.Button(window, text="Show Value Count", command=lambda: show_value_count(treeView, 2))
value_count_button.grid(row=4, column=1)

def itemSelected(event):
    global linha
    rowId = treeView.focus()
    linha = treeView.item(rowId)

treeView.bind('<<TreeviewSelect>>', itemSelected)

scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=treeView.yview)
treeView.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=1, sticky='ns')

window.mainloop()