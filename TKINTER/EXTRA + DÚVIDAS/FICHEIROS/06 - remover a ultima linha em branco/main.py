import tkinter as tk
from tkinter import ttk


Window = tk.Tk()
Window.title("Remove the last line")
Window.geometry("500x500")

# treeview with columns country and capital
tree = ttk.Treeview(Window, columns=("country", "capital"),
                    height=10, show="headings")

# heading for columns
tree.heading("country", text="Country")
tree.heading("capital", text="Capital")

tree.place(x=0, y=0)

btnDelete = tk.Button(Window, text="Delete",
                      command=lambda: delete_data(), width=10, height=2)
btnDelete.place(x=120, y=300)


labelCountry = tk.Label(Window, text="Country", font=("Arial", 12))
labelCountry.place(x=120, y=400)

entryCountry = tk.Entry(Window, font=("Arial", 12), width=10)
entryCountry.place(x=200, y=400)

labelCapital = tk.Label(Window, text="Capital", font=("Arial", 12))
labelCapital.place(x=120, y=450)

entryCapital = tk.Entry(Window, font=("Arial", 12), width=10)
entryCapital.place(x=200, y=450)

btnAdd = tk.Button(Window, text="Add",
                   command=lambda: add_data(), width=10, height=2)
btnAdd.place(x=320, y=300)


def show_data():
    file = open("countries.txt", "r", encoding="utf-8")

    lines = file.readlines()

    for line in lines:
        line = line.strip()
        country, capital = line.split(";")
        tree.insert("", tk.END, values=(country, capital))

    file.close()



def add_data():
    country = entryCountry.get()
    capital = entryCapital.get()

    file = open("countries.txt", "a", encoding="utf-8")
    file.write( country + ";" + capital + "\n")
    file.close()

    entryCountry.delete(0, tk.END)
    entryCapital.delete(0, tk.END)

    tree.insert("", tk.END, values=(country, capital))


def delete_data():

    file = open("countries.txt", "r", encoding="utf-8")

    lines = file.readlines()

    values = tree.item(tree.selection())["values"]
    
    file.close()

    file = open("countries.txt", "w+", encoding="utf-8")


    for line in lines:
        line = line.strip()
        country, capital = line.split(";")
        if country != values[0] and capital != values[1]:
            file.write(line + "\n")

    file.close()

    tree.delete(tree.selection())


show_data()
Window.mainloop()
