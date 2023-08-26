import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import os

Window = tk.Tk()
Window.title("File Explorer")
Window.geometry("700x700")

image = ""
photo_image = None  # Store the PhotoImage instance separately

Canvas = tk.Canvas(Window, width=500, height=500, background="white")
Canvas.place(x=20, y=20)

buttonSelect = tk.Button(Window, text="Change Image")
buttonSave = tk.Button(Window, text="Save Image")

image = Image.open("./images/placeholder.jpg")
image = image.resize((500, 500))
photo_image = ImageTk.PhotoImage(image)  # Initialize the PhotoImage instance
Canvas.create_image(0, 0, anchor=tk.NW, image=photo_image)


def View():
    global image

    buttonSave.place(x=20, y=600)
    buttonSelect.place(x=20, y=550)

    def selectImage():
        global image
        global photo_image  # Declare it as a global variable to modify it

        # open the file dialog on the current directory
        file = filedialog.askopenfilename(
            initialdir="./images", title="Select an image", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))

        # get the name of the image selected
        image_path = file  # Store the full path here

        # open the image
        image = Image.open(file)

        # resize the image
        image = image.resize((500, 500))

        # convert the image to a tkinter image
        # Update the PhotoImage instance
        photo_image = ImageTk.PhotoImage(image)

        # show the image on the canvas
        Canvas.create_image(0, 0, anchor=tk.NW, image=photo_image)

        buttonSave.config(command=lambda: saveImage(image_path))

    buttonSelect.config(command=selectImage)

    showImage()


def saveImage(imagePath):
    image = os.path.basename(imagePath)
    # add ./images/ to the image name
    imagePath = f"./images/{image}"
    # save the image
    file = open("pictures.txt", "w", encoding="utf-8")
    file.write(imagePath)
    file.close()


def showImage():

    # show on the canvas the image from the file
    file = open("pictures.txt", "r", encoding="utf-8")

    lines = file.readlines()

    for line in lines:
        # convert the image to a tkinter image
        photo_image = ImageTk.PhotoImage(Image.open(line.strip()).resize(
            (500, 500)))     # Update the PhotoImage instance

        # delete the previous image
        Canvas.delete("all")

        # show the image on the canvas
        Canvas.image = photo_image
        Canvas.create_image(0, 0, anchor=tk.NW, image=photo_image)

    file.close()


View()
Window.mainloop()