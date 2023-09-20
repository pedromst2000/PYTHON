import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image 

Window = tk.Tk()
Window.title("Testing")

Window.geometry("500x500")

Canvas = tk.Canvas(Window, width=500, height=500, bg="white")
Canvas.place(x=0, y=0)

btn = tk.Button(Window, text="Click Me")
btn.place(x=0, y=0)

image = ImageTk.PhotoImage(Image.open("example1/imageTesting.png"))

Canvas.create_image(0, 0, image=image, anchor=NW)


label = Canvas.create_text(250, 250, text="Hello World", font=("Arial", 20), fill="#fff")


# add the label to the canvas
Canvas.itemconfig(label, text="Hello World")


Window.mainloop()