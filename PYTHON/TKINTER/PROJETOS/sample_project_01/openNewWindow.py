import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import Canvas


with open("test/TKINTER/users.txt", "r") as file:
        lines = file.readlines()
        user = lines[0].split(";")[0]
        image_file = lines[0].split(";")[1]


def switch_to_window1():
    window1.deiconify()
    window2.withdraw()

def switch_to_window2():
    userEntry.delete(0, "end")
    

    userEntry.insert(0, user)
    
    window2.deiconify()
    window1.withdraw()

def select_image():
    file_path = filedialog.askopenfilename(title = "Select file", initialdir = "test\TKINTER/images",
              filetypes = (("png files","*.png"),("gif files", "*.gif"), ("all files","*.*")))
    image = PhotoImage(master = userPicture, file=file_path)
    userPicture.create_image(50, 50, image=image)
    userPicture.itemconfig(userPicture, image=image)


def save_profile():
    new_user = userEntry.get()
    new_image_file = filedialog.askopenfilename().split("/")[-1]

    with open("test/TKINTER/users.txt", "r") as file:
        lines = file.readlines()

    with open("test/TKINTER/users.txt", "w") as file:
        for line in lines:
            if line.split(";")[0] == user:
                file.write(f"{new_user};{new_image_file}")
            else:
                file.write(line)

    new_image = PhotoImage(master=userPicture, file=f"test/TKINTER/images/{new_image_file}")
    userPicture.create_image(50, 50, image=new_image, anchor=NW, tags=new_image)
    userPicture.itemconfig(userPicture, image=new_image)

    

window1 = tk.Tk()
window1.title("Window 1")
window1.geometry("500x500")
switch_to_window2_button = tk.Button(window1, text="Switch to Window 2", command=switch_to_window2)
switch_to_window2_button.pack()

window2 = tk.Tk()
window2.title("Window 2")
window2.geometry("500x500")

labelUser = tk.Label(window2, text="User")
labelUser.pack()

userEntry = tk.Entry(window2)
userEntry.pack()

userPicture = Canvas(window2)

imageUser = PhotoImage(master = userPicture, file=f"test/TKINTER/images/{image_file}")
userPicture.create_image(50, 50, image=imageUser, anchor=NW) 
userPicture.pack()

chooseImage = Button(window2, text="Choose profile picture", command=select_image)
chooseImage.pack()

saveProfile = Button(window2, text="Save profile", command=save_profile)
saveProfile.pack()

switch_to_window1_button = tk.Button(window2, text="Switch to Window 1", command=switch_to_window1)

switch_to_window1_button.pack()

window2.withdraw()
window1.mainloop()
