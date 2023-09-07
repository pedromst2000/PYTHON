import tkinter as tk
from tkinter import filedialog, Listbox, Button
from PIL import ImageTk, Image


Window = tk.Tk()
Window.title("Gestor de Fotos")

Window.geometry("800x600")
Window.resizable(False, False)

listPhotos = Listbox(Window, width=50 , height=20)
listPhotos.place(x=10, y=10)


buttonSelectImage = Button(Window, text="Selecionar Imagem", width=42, height=2)
buttonSelectImage.place(x=10, y=360)

buttonDeleteImage = Button(Window, text="Remover Imagem", width=42, height=2)
buttonDeleteImage.place(x=10, y=420)

buttonSaveImage = Button(Window, text="Salvar Imagem", width=42, height=2)
buttonSaveImage.place(x=10, y=480)

containerCanvas = tk.Frame(Window, width=380, height=280, relief="sunken", bd=2)
containerCanvas.place(x=380, y=10)

containerImage = tk.Canvas(containerCanvas, width=340, height=240, relief="sunken", bd=2, bg="white")
containerImage.place(x=10, y=10)

# navigation section
# <<
btnNavFirstImage = Button(Window, text="<<", width=12, height=2)
btnNavFirstImage.place(x=380, y=300)
# <
btnNavLastImage  = Button(Window, text="<", width=12, height=2)
btnNavLastImage.place(x=480, y=300)
# >
btnNavPreviousImage = Button(Window, text=">", width=12, height=2)
btnNavPreviousImage.place(x=580, y=300)
# >>
btnNavNextImage = Button(Window, text=">>", width=12, height=2)
btnNavNextImage.place(x=680, y=300)

def SelectImage():

    filename = filedialog.askopenfilename(initialdir="./images", title="Select a File", filetypes=(("png files", "*.png"), ("gif files", "*.gif*")))

    # get the selected image 
    image = Image.open(filename)

    # insert image to listbox
    listPhotos.insert(tk.END, filename)


def showImage():
    # get the selected image 
    image = Image.open(listPhotos.get(listPhotos.curselection()))

    # resize image
    image = image.resize((346, 246))

    # insert image to canvas
    containerImage.image = ImageTk.PhotoImage(image)
    containerImage.create_image(0, 0, image=containerImage.image, anchor="nw")

def saveImage():
    # get the selected image
    image = Image.open(listPhotos.get(listPhotos.curselection()))

    file = open("files/images.txt", "r", encoding="utf-8")

    lines = file.readlines()

    file.close()

    file = open("files/images.txt", "a", encoding="utf-8")

    for line in lines:
        # get the image name
        imageName = line.split("/")[2].split(".")[0]

        # get the selected image name
        selectedImageName = listPhotos.get(listPhotos.curselection()).split("/")[2].split(".")[0]

        if imageName != selectedImageName:
            file.write(line)

    file.write(listPhotos.get(listPhotos.curselection()) + "\n")


def showImages():
    file = open("files/images.txt", "r", encoding="utf-8")

    lines = file.readlines()
   
    for line in lines:
        # insert without \n
        listPhotos.insert(tk.END, line[:-1])


    file.close() 


def navigationImages():

    images = []

    file = open("files/images.txt", "r", encoding="utf-8")

    lines = file.readlines()

    for line in lines:

        images.append(line[:-1])

    file.close()

    return images


def firstImage():
    images = navigationImages()

    image = Image.open(images[0])

    # resize image
    image = image.resize((346, 246))

    # insert image to canvas
    containerImage.image = ImageTk.PhotoImage(image)
    containerImage.create_image(0, 0, image=containerImage.image, anchor="nw") 

    # navigate listbox
    listPhotos.selection_clear(0, tk.END)
    listPhotos.selection_set(0)


def lastImage():
    images = navigationImages()

    image = Image.open(images[-1])

    # resize image
    image = image.resize((346, 246))

    # insert image to canvas
    containerImage.image = ImageTk.PhotoImage(image)
    containerImage.create_image(0, 0, image=containerImage.image, anchor="nw")

    # navigate listbox
    listPhotos.selection_clear(0, tk.END)
    listPhotos.selection_set(len(images) - 1)

def previousImage():
    images = navigationImages()

    image = Image.open(images[listPhotos.curselection()[0] - 1])

    # resize image
    image = image.resize((346, 246))

    # insert image to canvas
    containerImage.image = ImageTk.PhotoImage(image)
    containerImage.create_image(0, 0, image=containerImage.image, anchor="nw")

    # navigate listbox
    listPhotos.selection_clear(0, tk.END)
    listPhotos.select_set(images.index(images[listPhotos.curselection()[0] - 1]))


def nextImage():
    images = navigationImages()

    image = Image.open(images[listPhotos.curselection()[0] + 1])

    # resize image
    image = image.resize((346, 246))

    # insert image to canvas
    containerImage.image = ImageTk.PhotoImage(image)
    containerImage.create_image(0, 0, image=containerImage.image, anchor="nw")

    # navigate listbox
    listPhotos.selection_clear(0, tk.END)
    listPhotos.select_set(images.index(images[listPhotos.curselection()[0] + 1]))



navigationImages()
buttonSelectImage.config(command=SelectImage)
buttonSaveImage.config(command=saveImage)
listPhotos.bind("<<ListboxSelect>>", lambda x: showImage())
showImages()
btnNavFirstImage.config(command=firstImage)
btnNavLastImage.config(command=lastImage)
btnNavPreviousImage.config(command=previousImage)
btnNavNextImage.config(command=nextImage)
Window.mainloop()