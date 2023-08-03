import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def save_to_file(tree):
    with open('lines.txt', 'w') as file:
        for item in tree.get_children():
            values = [tree.item(item, 'values')]
            line = ','.join(str(x) for x in values[0])
            file.write(line + '\n')



def show_value_count(tree, column):
    # TAKES ALL THE VALUES OF THE TREEVIEW AND THE COLUMN PASSED BY THE BUTTON AND CREATES A DICTIONARY WITH THE VALUE AND THE AMOUNT OF TIMES IT OCURS
    value_counts = {}
    for item in tree.get_children():
        value = tree.item(item, "values")[column]
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1

    # CREATES A MESSAGE THAT WRITES IN A SHOWINFO THE AMOUNT OF EACH VALUE THAT EXISTS
    message = "Value Counts:\n\n"
    for value, count in value_counts.items():
        if count < 2:
            message += f"There is {count} of type {value} \n\n"
        else:
            message += f"There are {count} of type {value} \n\n"
    messagebox.showinfo("Value Count", message)


root = tk.Tk()
tree = ttk.Treeview(root, columns=('column1', 'column2'))
tree.pack()

tree.insert("", 0, text="Item 1", values=("Value 1.1", "Value 1.2"))
tree.insert("", 1, text="Item 2", values=("Value 2.1", "Value 2.2"))
tree.insert("", 2, text="Item 3", values=("Value 3.1", "Value 3.2"))
tree.insert("", 3, text="Item 4", values=("Value 3.1", "Value 3.2"))

save_button = ttk.Button(root, text="Save to file", command=lambda: save_to_file(tree))
save_button.pack()

value_count_button = ttk.Button(root, text="Show Value Count", command=lambda: show_value_count(tree, 1))
value_count_button.pack()

root.mainloop()
