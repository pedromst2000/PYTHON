#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

# 40210465 - Importing the messagebox for the dialogbox warning message
from tkinter import messagebox

# 40210465 - Importing the logic functions
from EX1_40210465 import (
    insert_loan_types,
    insert_loan_states,
    cancel_button,
    add_loan,
    update_loan,
)


class ModificarWidget(tk.Toplevel):
    def __init__(self, treeview, master=None, **kw):
        super().__init__(master, **kw)
        self.title("Criar/Modificar Empréstimo")
        frame5 = ttk.Frame(self)
        frame5.configure(height=200, relief="sunken", width=200)
        self.date_label = ttk.Label(frame5, name="date_label")
        self.date_label.configure(text="Data")
        self.date_label.grid(column=0, padx=10, pady=10, row=0, sticky="nsew")
        self.date_entry = ttk.Entry(frame5, name="date_entry")
        self.date_entry.grid(column=1, padx=10, pady=10, row=0, sticky="nsew")
        self.name_label = ttk.Label(frame5, name="nome_label")
        self.name_label.configure(text="Nome")
        self.name_label.grid(column=0, padx=10, pady=10, row=1, sticky="nsew")
        self.name_entry = ttk.Entry(frame5, name="name_entry")
        self.name_entry.grid(column=1, padx=10, pady=10, row=1, sticky="nsew")
        self.type_label = ttk.Label(frame5, name="tipo_label")
        self.type_label.configure(text="Tipo")
        self.type_label.grid(column=0, padx=10, pady=10, row=2, sticky="nsew")
        self.type_combobox = ttk.Combobox(frame5, name="type_combobox")
        self.type_combobox.grid(column=1, padx=10, pady=10, row=2, sticky="nsew")

        # 40210465 - Binding the type combobox to the insert_loan_types function

        self.type_combobox.bind(
            "<Button-1>", lambda event: insert_loan_types(event, self.type_combobox)
        )

        # --------------------------------------------------------------------------------

        self.description_label = ttk.Label(frame5, name="decricao_label")
        self.description_label.configure(text="Descrição")
        self.description_label.grid(column=0, padx=10, pady=10, row=3, sticky="nsew")
        self.description_entry = ttk.Entry(frame5, name="description_entry")
        self.description_entry.grid(column=1, padx=10, pady=10, row=3, sticky="nsew")
        self.state_label = ttk.Label(frame5, name="state_label")
        self.state_label.configure(text="Estado")
        self.state_label.grid(column=0, padx=10, pady=10, row=4, sticky="nsew")
        self.state_combobox = ttk.Combobox(frame5, name="state_combobox")
        self.state_combobox.grid(column=1, padx=10, pady=10, row=4, sticky="nsew")

        # 40210465 - Binding the state combobox to the insert_loan_states function

        self.state_combobox.bind(
            "<Button-1>", lambda event: insert_loan_states(event, self.state_combobox)
        )

        # --------------------------------------------------------------------------------

        frame5.grid(column=0, padx=10, pady=10, row=0, sticky="nsew")
        frame7 = ttk.Frame(self)
        frame7.configure(padding=10, width=200)
        self.ok_button = ttk.Button(frame7, name="ok_button")
        self.ok_button.configure(text="Ok")
        self.ok_button.grid(column=0, padx=10, pady=10, row=0, sticky="nsew")

        if treeview.selection():
            # 40210465 - Binding the ok button to the update_loan function
            self.ok_button.bind(
                "<Button-1>",
                lambda event: update_loan(
                    treeview,
                    messagebox,
                    self.date_entry,
                    self.name_entry,
                    self.type_combobox,
                    self.description_entry,
                    self.state_combobox,
                ),
            )

        else:
            # 40210465 - Binding the ok button to the add_loan function
            self.ok_button.bind(
                "<Button-1>",
                lambda event: add_loan(
                    treeview,
                    messagebox,
                    self.date_entry,
                    self.name_entry,
                    self.type_combobox,
                    self.description_entry,
                    self.state_combobox,
                ),
            )

        # --------------------------------------------------------------------------------

        self.cancel_button = ttk.Button(frame7, name="cancel_button")
        self.cancel_button.configure(text="Cancel")
        self.cancel_button.grid(column=0, padx=10, pady=10, row=1, sticky="nsew")

        # 40210465 - Binding the cancel button to the cancel_button function

        self.cancel_button.bind(
            "<Button-1>",
            lambda event: cancel_button(
                event,
                self.date_entry,
                self.name_entry,
                self.type_combobox,
                self.description_entry,
                self.state_combobox,
            ),
        )

        # --------------------------------------------------------------------------------

        frame7.grid(column=1, row=0)
        self.configure(height=200, width=200)


if __name__ == "__main__":
    root = tk.Tk()
    widget = ModificarWidget(root)
    root.mainloop()
