from tkinter import *



Window = Tk()
Window.title("Testing")
Window.geometry("500x500")


listData = Listbox(Window, width=50, height=20)
listData.place(x=10, y=10)

btnDelete = Button(Window, text="Delete", width=10, height=2)
btnDelete.place(x=10, y=400)

def readData():
    file = open("provas.txt", "r", encoding="utf-8")

    for line in file:
        listData.insert(END, line)

    file.close()


def deleteData():
    # listData.delete(ANCHOR)

    # remove the selected item from the file
    file = open("provas.txt", "r", encoding="utf-8")
    lines = file.readlines()

    file.close()

    file = open("provas.txt", "w+", encoding="utf-8")

    # change the index of the file to the index of the listbox
    index = listData.curselection()[0] 

    # remove the selected item from the listbox
    listData.delete(index)

    # remove the selected item from the file
    for line in lines:
        if line != lines[index]:
            file.write(line)

    file.close()


btnDelete.config(command=deleteData)
readData()
Window.mainloop()