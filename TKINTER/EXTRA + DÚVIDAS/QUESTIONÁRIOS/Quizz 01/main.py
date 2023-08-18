import tkinter as tk
from tkinter import ttk
import time


Window = tk.Tk()
Window.title("Countries Quizz")
Window.geometry("1000x500")

rightAwnsers = 0
wrongAwnsers = 0
score = 0

containerQuizz = tk.Frame(Window, width=980, height=300,
                          relief="sunken", borderwidth=4)
containerQuizz.place(x=10, y=10)

containerResults = tk.Frame(
    Window, width=220, height=150, relief="sunken", borderwidth=4)
containerResults.place(x=10, y=320)

labelRight = tk.Label(containerResults, text="Right answers:")
labelRight.place(x=10, y=10)

entryRight = tk.Entry(containerResults, width=9)
entryRight.place(x=100, y=10)

labelWrong = tk.Label(containerResults, text="Wrong answers:")
labelWrong.place(x=10, y=40)

entryWrong = tk.Entry(containerResults, width=9)
entryWrong.place(x=100, y=40)

labelScore = tk.Label(containerResults, text="Score:")
labelScore.place(x=10, y=70)

entryScore = tk.Entry(containerResults, width=9)
entryScore.place(x=100, y=70)

entryRight.insert(0, rightAwnsers)
entryWrong.insert(0, wrongAwnsers)
entryScore.insert(0, score)

tree = ttk.Treeview(Window, columns=("Country", "Status"),
                    show="headings", height=5)
tree.heading("Country", text="Country")
tree.heading("Status", text="Status")

tree.column("Country", width=200)
tree.column("Status", width=200)

tree.place(x=250, y=330)

scrollbar = ttk.Scrollbar(Window, orient="vertical", command=tree.yview)
scrollbar.place(x=650, y=330, height=130)

# button 'Next Question'
buttonNext = tk.Button(Window, text="Next Question",
                       width=15, height=5, relief="raised", borderwidth=4)
buttonNext.place(x=710, y=350)

# button 'Check Answer'
buttonCheck = tk.Button(Window, text="Check Answer",
                        width=15, height=5, relief="raised", borderwidth=4)
buttonCheck.place(x=860, y=350)

label = tk.Label(containerQuizz, text="Quizz Countries",
                 font=("Arial", 20, "bold"))
label.place(x=350, y=10)

buttonStart = tk.Button(containerQuizz, text="Start",
                        width=15, height=5, relief="raised", borderwidth=4)
buttonStart.place(x=400, y=150)

# ------------------ Functions ----------------------------------------------------------------------

def Quizz_view():
    global rightAwnsers
    global wrongAwnsers
    global score

    buttonStart.destroy()

    labelCount = tk.Label(
        containerQuizz, text="The Quizz will start in", font=("Arial", 15))
    labelCount.place(x=350, y=100)

    # countdown between 5 and 1
    for i in range(5, 0, -1):
        labelCount["text"] = "The Quizz will start in " + str(i)
        Window.update()
        time.sleep(1)
        # when countdown is finished, the label is destroyed
        if i == 1:
            labelCount.destroy()
            label = tk.Label(containerQuizz, text="Good Luck :)",
                             font=("Arial", 20, "bold"))
            label.place(x=400, y=100)
            # destroy the label after 3 seconds
            Window.after(3000, label.destroy)

            # show the label before the label is destroyed
            Window.after(3000, Quizz)


def Quizz(i=0):
    global selected

    selected = tk.StringVar()  # Define selected as a global variable inside Quizz function
    selected.set(0)

    file = open("countries.txt", "r", encoding="utf-8")

    lines = file.readlines()

    line = lines[i].split(";")

    print(line)

    labelQuestion = tk.Label(
        containerQuizz, text=f"{line[0]} is the capital of which country?", font=("Arial", 15))
    labelQuestion.place(x=350, y=100)

    radioOption1 = tk.Radiobutton(
        containerQuizz, text=line[1], variable=selected, value=line[1])
    radioOption1.place(x=350, y=150)

    radioOption2 = tk.Radiobutton(
        containerQuizz, text=line[2], variable=selected, value=line[2])
    radioOption2.place(x=350, y=180)

    radioOption3 = tk.Radiobutton(
        containerQuizz, text=line[3], variable=selected, value=line[3])
    radioOption3.place(x=350, y=210)

    radioOption4 = tk.Radiobutton(
        containerQuizz, text=line[4], variable=selected, value=line[4])
    radioOption4.place(x=350, y=240)

    def check_Awnser():
        global rightAwnsers
        global wrongAwnsers
        global score

        print(f'{selected.get()} - {line[5]}')

        if selected.get() == line[5].strip():
            rightAwnsers += 1
            score += 10
            entryRight.delete(0, tk.END)
            entryScore.delete(0, tk.END)
            entryRight.insert(0, rightAwnsers)
            entryScore.insert(0, score)
            tree.insert("", "end", values=(selected.get(), "Right"))

        else:
            wrongAwnsers += 1
            # remove the 0 from the entry and insert the new value
            entryWrong.delete(0, tk.END)
            entryWrong.insert(0, wrongAwnsers)
            tree.insert("", "end", values=(selected.get(), "Wrong"))

    buttonCheck.config(command=check_Awnser)

    file.close()

    def next_Question():
        global rightAwnsers
        global wrongAwnsers
        global score

        if i < len(lines) - 1:
            Quizz(i + 1)

            selected.set(0)

            # remove the selection of each radio button
            radioOption1.deselect()
            radioOption2.deselect()
            radioOption3.deselect()
            radioOption4.deselect()
            # destroy the radio buttons
            radioOption1.destroy()
            radioOption2.destroy()
            radioOption3.destroy()
            radioOption4.destroy()
            # destroy the label
            labelQuestion.destroy()

        else:
            # destroy the radio buttons
            radioOption1.destroy()
            radioOption2.destroy()
            radioOption3.destroy()
            radioOption4.destroy()
            # destroy the label
            labelQuestion.destroy()

            label = tk.Label(containerQuizz, text="End of Quizz",
                             font=("Arial", 20, "bold"))
            label.place(x=400, y=100)

            labelScore = tk.Label(containerQuizz, text="Your score was: " + str(score),
                                  font=("Arial", 15))

            labelScore.place(x=400, y=150)

            buttonRestart = tk.Button(containerQuizz, text="Restart",
                                      width=15, height=5, relief="raised", borderwidth=4)
            buttonRestart.place(x=400, y=200)

            def Restart():
                # clear the values of the entries
                entryRight.delete(0, "end")
                entryWrong.delete(0, "end")
                entryScore.delete(0, "end")
                # insert the value 0 in the entries
                entryRight.insert(0, 0)
                entryWrong.insert(0, 0)
                entryScore.insert(0, 0)
                # clear the treeview
                tree.delete(*tree.get_children())
                # update the values of the variables
                global rightAwnsers, wrongAwnsers, score
                rightAwnsers = 0
                wrongAwnsers = 0
                score = 0

                # destroy the widgets
                label.destroy()
                labelScore.destroy()
                buttonRestart.destroy()

                Quizz_view()

            buttonRestart.config(command=Restart)

    buttonNext.config(command=next_Question)


buttonStart.config(command=Quizz_view)
Window.mainloop()
