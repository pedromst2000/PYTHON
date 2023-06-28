import tkinter as tk
import random
import time
from tkinter import ttk

# Global variables to keep track of score and answers
score = 0
answers = []

# Read the theme files and store the questions
europe_questions = []
with open("example/europa.txt") as f:
    europe_questions = [line.strip().split(";") for line in f.readlines()]

america_questions = []
with open("example/america.txt") as f:
    america_questions = [line.strip().split(";") for line in f.readlines()]

asia_questions = []
with open("example/asia.txt") as f:
    asia_questions = [line.strip().split(";") for line in f.readlines()]

# Function to handle the New Question button
def new_question():
    global current_question
    if theme.get() == "Europe":
        current_question = random.choice(europe_questions)
    elif theme.get() == "America":
        current_question = random.choice(america_questions)
    else:
        current_question = random.choice(asia_questions)

    capital_label.config(text=current_question[0])
    option1.config(text=current_question[1])
    option2.config(text=current_question[2])
    option3.config(text=current_question[3])
    option4.config(text=current_question[4])

# Function to handle the Answer button
def answer():
    global score
    selected = "None"
    if option_var.get() == "1":
        selected = option1["text"]
    elif option_var.get() == "2":
        selected = option2["text"]
    elif option_var.get() == "3":
        selected = option3["text"]
    elif option_var.get() == "4":
        selected = option4["text"]

    if selected == current_question[5]:
        result_label.config(text="Correct!!")
        score += 1
        answers.append((current_question[0], "Correct"))
        tree.insert("", "end", values=(current_question[0], "Correct"))
    else:
        result_label.config(text="Incorrect!!")
        answers.append((current_question[0], "Incorrect"))
        tree.insert("", "end", values=(current_question[0], "Incorrect"))
    
    score_label.config(text=f"Score: {score}")
    wrong_answers_label.config(text=f"Wrong answers: {len(answers) - score}")


# FUNCTION TO UPDATE TIME AND DATE
def update_label():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    labelTime.config(text=current_time)
    labelTime.after(1000, update_label)

# Create the main window
root = tk.Tk()
root.title("Quizz Capitals")
root.geometry("1200x800")

# Create the widgets
title_label = tk.Label(root, text="Quizz Capitals of Countries", font=("TkDefaultFont", 16))
title_label.pack()

# radio buttons
theme = tk.StringVar(root, "Europe")
europe_radio = tk.Radiobutton(root, text="Europe", variable=theme, value="Europe")
europe_radio.place(x=1050, y=0)

america_radio = tk.Radiobutton(root, text="America", variable=theme, value="America")
america_radio.place(x=1050, y=50)

asia_radio = tk.Radiobutton(root, text="Asia", variable=theme, value="Asia")
asia_radio.place(x=1050, y=100)

new_question = tk.Button(root, text="New question", command=new_question)
new_question.place(x=1050, y=150)

answer = tk.Button(root, text="Answer", command=answer)
answer.place(x=1050, y=200)
# quizz

capital_label = tk.Label(root, text="question", relief="sunken", background="white", width=15)
capital_label.pack(pady=(10,0))

quizzLabel = tk.Label(root, text="É a capital de:")
quizzLabel.pack(pady=(10,0))

#options
option_var = tk.StringVar(root, "1")

option1 = tk.Radiobutton(root, text="", variable=option_var, value="1")
option1.place(x=450, y=150)

option2 = tk.Radiobutton(root, text="", variable=option_var, value="2")
option2.place(x=750, y=150)

option3 = tk.Radiobutton(root, text="", variable=option_var, value="3")
option3.place(x=450, y=250)

option4 = tk.Radiobutton(root, text="", variable=option_var, value="4")
option4.place(x=750, y=250)

result_label = tk.Label(root, text="", font="arial 18 bold")
result_label.pack(pady=(200,0))

# Create the Treeview
tree = ttk.Treeview(root, columns=("Capital", "Status"), height=5)
tree.pack(pady=(10,0))
tree.column("#0", width=50, minwidth=0, stretch=tk.NO)
# Configure the columns
tree.column("Capital", width=250, anchor='w')
tree.column("Status", width=250, anchor='w')
tree.heading("Capital", text="Capital", anchor='w')
tree.heading("Status", text="Status", anchor='w')

score_label = tk.Label(root, text=f"Score: {score}")
score_label.place(x=100, y=350)

wrong_answers_label = tk.Label(root, text=f"Wrong answers: {len(answers) - score}")
wrong_answers_label.place(x=100, y=450)

labelTime = tk.Label(root, font=("Arial", 7))
labelTime.place(x=100, y=550)


update_label()
root.mainloop()
