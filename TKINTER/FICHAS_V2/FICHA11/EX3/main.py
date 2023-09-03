import tkinter as tk
from tkinter import * 


Window = tk.Tk()
Window.title("EX3")
Window.geometry("1200x600")



containerList = Frame(Window, bd=5, relief=SUNKEN)
containerList.place(x=10, y=10, width=400, height=580)

listTask = Listbox(containerList, width=50, height=32)
listTask.place(x=30, y=30)

containerTask =  Frame(Window, bd=5, relief=SUNKEN)
containerTask.place(x=420, y=10, width=770, height=180)

labelTask = Label(containerTask, text="Tarefa:", font=("Arial", 20), fg="blue")
labelTask.place(x=40, y=40)

entryTask = Entry(containerTask, width=30, font=("Arial", 20))  
entryTask.place(x=150, y=40)

btnAdd = Button(Window, text="Adicionar", width=20, height=2)
btnAdd.place(x=420, y=200)

btnRemove = Button(Window, text="Remove", width=20, height=2)
btnRemove.place(x=600, y=200)

btnClear = Button(Window, text="Clear", width=20, height=2)
btnClear.place(x=780, y=200)

btnUpload = Button(Window, text="Upload", width=20, height=2)
btnUpload.place(x=420, y=250)

btnDownload = Button(Window, text="Download", width=20, height=2)
btnDownload.place(x=600, y=250)

btnSort = Button(Window, text="Ordenar", width=20, height=2)
btnSort.place(x=780, y=250)

labelTotalTasks = Label(Window, text="Nº de Tarefas Pendentes:", font=("Arial", 13), fg="blue")
labelTotalTasks.place(x=420, y=500) 

entryTotalTasks = Entry(Window, width=5, font=("Arial", 13))
entryTotalTasks.place(x=620, y=500)


def adicionar():
    # add task to list
    listTask.insert(END, entryTask.get())
    # clear entry
    entryTask.delete(0, END)
    # update total tasks
    entryTotalTasks.delete(0, END)
    entryTotalTasks.insert(0, listTask.size())


def remove():
    # delete task from list
    listTask.delete(ANCHOR)
    # update total tasks
    entryTotalTasks.delete(0, END)
    entryTotalTasks.insert(0, listTask.size())

def clear():
    # clear list
    listTask.delete(0, END)
    # update total tasks
    entryTotalTasks.delete(0, END)
    entryTotalTasks.insert(0, listTask.size())


def download():
    # save the list in a file
    file = open("EX3/tarefas.txt", "w", encoding="utf-8")

    for item in listTask.get(0, END):
        file.write(item + "\n")

    file.close()


def upload():
    # read the file and add the tasks to the list
    file = open("EX3/tarefas.txt", "r", encoding="utf-8")

    for line in file:
        listTask.insert(END, line)

    file.close()

    # update total tasks
    entryTotalTasks.delete(0, END)
    entryTotalTasks.insert(0, listTask.size())


def sort():
    # sort the list in alphabetical order
    listTask.delete(0, END)
    tasks = []

    # get all tasks from the file
    file = open("EX3/tarefas.txt", "r", encoding="utf-8")

    for line in file:
        tasks.append(line)

    file.close()

    tasks.sort()

    # add the tasks to the list
    for task in tasks:
        listTask.insert(END, task)

    # update total tasks
    entryTotalTasks.delete(0, END)
    entryTotalTasks.insert(0, listTask.size())

    


btnAdd.config(command=adicionar)
btnRemove.config(command=remove)
btnClear.config(command=clear)
btnUpload.config(command=upload)
btnDownload.config(command=download)
btnSort.config(command=sort)


Window.mainloop()   