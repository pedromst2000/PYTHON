#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

# 40210465 - Importing the messagebox for the dialogbox for the warning message
from tkinter import (
    messagebox,
    StringVar,
)  # 40210465 - Importing the StringVar for the combobox widget
from modificar import ModificarWidget

# 40210465 - Importing the logic functions
from EX1_40210465 import insert_data, delete_loan, insert_mouths, insert_filtered_loans


class GuiApp:
    def __init__(self, master=None):
        # build ui
        self.window = tk.Tk(master)
        self.window.configure(height=500, width=600)
        self.window.title("Gestor de Empréstimos")
        frame1 = ttk.Frame(self.window)
        frame1.configure(height=200, relief="sunken", width=200)
        frame2 = ttk.Frame(frame1)
        frame2.configure(height=200, width=200)
        self.load_button = ttk.Button(frame2, name="load_button")
        self.load_button.configure(text="Carregar")
        self.load_button.grid(column=0, padx=10, pady=30, row=0, sticky="nsew")

        # 40210465 - Global variable to store the value of the combobox selected
        loan_type = StringVar()
        loan_type.set("Emprestei")
        loan_state = StringVar()
        loan_state.set("Por Devolver")

        # 40210465 - Binding the load button to the insert data into the treeview
        self.load_button.bind(
            "<Button-1>", lambda event: insert_data(event, self.data_treeview)
        )

        # --------------------------------------------------------------------------------

        self.add_button = ttk.Button(frame2, name="add_button")
        self.add_button.configure(text="Adicionar")
        self.add_button.grid(column=0, padx=10, row=1, sticky="nsew")

        # 40210465 - Binding the add button to the open the modify window

        self.add_button.bind(
            "<Button-1>", lambda event: ModificarWidget(self.data_treeview, self.window)
        )

        # --------------------------------------------------------------------------------

        self.modify_button = ttk.Button(frame2, name="modify_button")
        self.modify_button.configure(text="Modificar")
        self.modify_button.grid(column=0, padx=10, pady=10, row=2, sticky="nsew")

        # 40210465 - Binding the modify button to the open the modify window
        self.modify_button.bind(
            "<Button-1>", lambda event: ModificarWidget(self.data_treeview, self.window)
        )

        # --------------------------------------------------------------------------------

        self.delete_button = ttk.Button(frame2, name="delete_button")
        self.delete_button.configure(text="Eliminar")
        self.delete_button.grid(column=0, padx=10, row=3, sticky="nsew")

        # 40210465 - Binding the delete button to the delete_loan function

        self.delete_button.bind(
            "<Button-1>",
            lambda event: delete_loan(event, self.data_treeview, messagebox),
        )

        # --------------------------------------------------------------------------------

        frame2.grid(column=0, padx=10, pady=10, row=0, sticky="nsew")
        frame3 = ttk.Frame(frame1)
        frame3.configure(height=200, width=200)
        self.filter_frame = ttk.Labelframe(frame3, name="filter_frame")
        self.filter_frame.configure(height=200, text="Filtrar", width=200)
        frame4 = ttk.Frame(self.filter_frame)
        frame4.configure(height=200, width=200)
        self.month_label = ttk.Label(frame4, name="month_label")
        self.month_label.configure(text="Mês")
        self.month_label.grid(column=0, row=0, sticky="nsew")
        self.month_combobox = ttk.Combobox(frame4, name="month_combobox")
        self.month_combobox.grid(column=1, padx=10, pady=10, row=0, sticky="nsew")

        # 40210465 - Binding the month_combobox to the insert_mouths function

        self.month_combobox.bind(
            "<Button-1>", lambda event: insert_mouths(event, self.month_combobox)
        )

        frame4.grid(column=0, columnspan=2, padx=10, row=0)
        labelframe5 = ttk.Labelframe(self.filter_frame)
        labelframe5.configure(height=200, text="Tipo", width=200)
        self.loaned_radiobutton = ttk.Radiobutton(
            labelframe5, name="loaned_radiobutton"
        )
        self.loaned_radiobutton.configure(text="Emprestei")
        self.loaned_radiobutton.grid(column=0, padx=10, pady=5, row=0, sticky="nsew")
        self.received_radiobutton = ttk.Radiobutton(
            labelframe5, name="received_radiobutton"
        )
        self.received_radiobutton.configure(text="Emprestaram-me")
        self.received_radiobutton.grid(column=0, padx=10, pady=5, row=1, sticky="nsew")
        labelframe5.grid(column=0, padx=10, pady=10, row=1, sticky="ew")
        labelframe6 = ttk.Labelframe(self.filter_frame)
        labelframe6.configure(height=200, text="Estado", width=200)
        self.radiobutton1 = ttk.Radiobutton(labelframe6, name="radiobutton1")
        self.radiobutton1.configure(text="Por Devolver")
        self.radiobutton1.grid(column=0, padx=10, pady=5, row=0, sticky="nsew")
        self.radiobutton2 = ttk.Radiobutton(labelframe6, name="radiobutton2")
        self.radiobutton2.configure(text="Devolvido")
        self.radiobutton2.grid(column=0, padx=10, pady=5, row=1, sticky="nsew")
        labelframe6.grid(column=1, padx=10, pady=10, row=1, sticky="ew")
        self.apply_button = ttk.Button(self.filter_frame, name="apply_button")
        self.apply_button.configure(text="Aplicar")
        self.apply_button.grid(
            column=0, columnspan=2, padx=40, pady=10, row=2, sticky="nsew"
        )

        self.filter_frame.grid(column=0, padx=10, pady=10, row=0, sticky="nsew")
        frame3.grid(column=1, padx=10, pady=10, row=0, sticky="nsew")
        frame1.grid(column=0, padx=10, pady=10, row=0, sticky="nsew")

        # 40210465 - Allowing to select only one radiobutton at a time
        self.loaned_radiobutton.configure(variable=loan_type, value="Emprestei")
        self.received_radiobutton.configure(variable=loan_type, value="Emprestaram-me")

        self.radiobutton1.configure(variable=loan_state, value="Por Devolver")
        self.radiobutton2.configure(variable=loan_state, value="Devolvido")

        frame5 = ttk.Frame(self.window)
        frame5.configure(height=200, padding=5, relief="sunken", width=200)
        self.data_treeview = ttk.Treeview(frame5, name="data_treeview")
        self.data_treeview.configure(selectmode="browse")
        self.data_treeview.grid(column=0, row=0, sticky="nsew")
        # --------------------------------------------------------------------------------

        # 40210465 - Binding the apply button to the filter_loans function
        self.apply_button.bind(
            "<Button-1>",
            lambda event: insert_filtered_loans(
                event,
                self.data_treeview,
                self.month_combobox,
                loan_type,
                loan_state,
            ),
        )

        # 40210465 - Adding the columns to the treeview (Nome, Data Empréstimo, Tipo Empréstimo, Descrição, Estado)

        self.data_treeview["columns"] = (
            "Nome",
            "Data Empréstimo",
            "Tipo Empréstimo",
            "Descrição",
            "Estado",
        )

        # 40210465 - Setting the columns' width
        self.data_treeview.column("#0", width=0, stretch=tk.NO)
        self.data_treeview.column("Nome", width=200, stretch=tk.NO)
        self.data_treeview.column("Data Empréstimo", width=200, stretch=tk.NO)
        self.data_treeview.column("Tipo Empréstimo", width=200, stretch=tk.NO)
        self.data_treeview.column("Descrição", width=200, stretch=tk.NO)
        self.data_treeview.column("Estado", width=200, stretch=tk.NO)

        # 40210465 - Setting the columns' headings
        self.data_treeview.heading("#0", text="", anchor=tk.CENTER)
        self.data_treeview.heading("Nome", text="Nome", anchor=tk.CENTER)
        self.data_treeview.heading(
            "Data Empréstimo", text="Data Empréstimo", anchor=tk.CENTER
        )
        self.data_treeview.heading(
            "Tipo Empréstimo", text="Tipo Empréstimo", anchor=tk.CENTER
        )
        self.data_treeview.heading("Descrição", text="Descrição", anchor=tk.CENTER)
        self.data_treeview.heading("Estado", text="Estado", anchor=tk.CENTER)

        # --------------------------------------------------------------------------------

        self.horizontal_scrollbar = ttk.Scrollbar(frame5, name="horizontal_scrollbar")
        self.horizontal_scrollbar.configure(orient="horizontal")
        self.horizontal_scrollbar.grid(column=0, padx=30, pady=10, row=0, sticky="sew")
        self.vertical_scrollbar = ttk.Scrollbar(frame5, name="vertical_scrollbar")
        self.vertical_scrollbar.configure(orient="vertical")
        self.vertical_scrollbar.grid(column=0, padx=10, pady=30, row=0, sticky="nse")
        frame5.grid(column=0, ipadx=0, padx=20, pady=10, row=1, sticky="nsew")
        frame5.columnconfigure(0, weight=1)
        self.mainwindow = self.window

    def center(self, event):
        wm_min = self.mainwindow.wm_minsize()
        wm_max = self.mainwindow.wm_maxsize()
        screen_w = self.mainwindow.winfo_screenwidth()
        screen_h = self.mainwindow.winfo_screenheight()
        """ `winfo_width` / `winfo_height` at this point return `geometry` size if set. """
        x_min = min(
            screen_w,
            wm_max[0],
            max(
                self.main_w,
                wm_min[0],
                self.mainwindow.winfo_width(),
                self.mainwindow.winfo_reqwidth(),
            ),
        )
        y_min = min(
            screen_h,
            wm_max[1],
            max(
                self.main_h,
                wm_min[1],
                self.mainwindow.winfo_height(),
                self.mainwindow.winfo_reqheight(),
            ),
        )
        x = screen_w - x_min
        y = screen_h - y_min
        self.mainwindow.geometry(f"{x_min}x{y_min}+{x // 2}+{y // 2}")
        self.mainwindow.unbind("<Map>", self.center_map)

    def run(self, center=False):
        if center:
            """If `width` and `height` are set for the main widget,
            this is the only time TK returns them."""
            self.main_w = self.mainwindow.winfo_reqwidth()
            self.main_h = self.mainwindow.winfo_reqheight()
            self.center_map = self.mainwindow.bind("<Map>", self.center)
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = GuiApp()
    app.run(center=True)
