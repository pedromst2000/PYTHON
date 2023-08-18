from tkinter import *



Window = Tk()
Window.title("Testing")
Window.geometry("500x500")


listData = Listbox(Window, width=50, height=20)
listData.place(x=10, y=10)


btnReadVal = Button(Window, text="Get Values", width=10, height=2)
btnReadVal.place(x=10, y=400)


def readData():
    file = open("provas.txt", "r", encoding="utf-8")

    for line in file:
        listData.insert(END, line)

    file.close()


def getValues():


    for item in listData.curselection():
        # add to the list with split 
        listData.get(item).split(";")
        # get the value of the list
        print(listData.get(item).split(";")[0])

btnReadVal.config(command=getValues)
readData()
Window.mainloop()   