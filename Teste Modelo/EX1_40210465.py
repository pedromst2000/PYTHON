# Numero : 40210465
# Nome : Pedro Miguel da Silva Teixeira

import tkinter as tk
from tkinter import ttk, messagebox


def insert_data(event: tk.Event, treeview: ttk.Treeview):
    """
    This function inserts the data from the file into the treeview.

    :param event: The event that triggers the function.
    :param treeview: The treeview that is going to be filled with data.
    """

    file = open("data.txt", "r", encoding="utf-8")

    lines = file.readlines()

    # ignoring the first line
    lines.pop(0)

    for line in lines:
        nome = line.split(";")[0]
        data_emprestimo = line.split(";")[1]
        tipo_emprestimo = int(line.split(";")[2])
        descricao = line.split(";")[3]
        estado = int(line.split(";")[4].strip())

        if tipo_emprestimo == 0:
            tipo_emprestimo = "Emprestei"
        else:
            tipo_emprestimo = "Emprestaram-me"

        if estado == 0:
            estado = "Por Devolver"
        else:
            estado = "Devolvido"

        treeview.insert(
            "",
            "end",
            text=nome,
            values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
        )

    file.close()


def insert_loan_types(event: tk.Event, combobox: ttk.Combobox):
    """
    This function inserts the loan types into the combobox.

    :param event: The event that triggers the function.
    :param combobox: The combobox that is going to be filled with data.
    """

    combobox["values"] = ["Emprestei", "Emprestaram-me"]
    combobox["state"] = "readonly"


def insert_loan_states(event: tk.Event, combobox: ttk.Combobox):
    """
    This function inserts the loan states into the combobox.

    :param event: The event that triggers the function.
    :param combobox: The combobox that is going to be filled with data.
    """

    combobox["values"] = ["Por Devolver", "Devolvido"]
    combobox["state"] = "readonly"


def add_loan(
    treeview: ttk.Treeview,
    dialogBox: messagebox,
    date: ttk.Entry,
    name: ttk.Entry,
    type: ttk.Combobox,
    description: ttk.Entry,
    state: ttk.Combobox,
):
    """
    This function adds a loan to the treeview.

    :param treeview: The treeview that is going to be filled with data.
    :param dialogBox: The messagebox that is going to be used to show the error messages.
    :param date: The entry that contains the date.
    :param name: The entry that contains the name.
    :param type: The combobox that contains the type.
    :param description: The entry that contains the description.
    :param state: The combobox that contains the state
    """

    POSSIBLE_FIELDS = ["Data", "Nome", "Tipo", "Descrição", "Estado"]

    for field in POSSIBLE_FIELDS:
        if field == "Data":
            if date.get() == "":
                dialogBox.showerror("Erro", "O campo Data está vazio")
                return
        elif field == "Nome":
            if name.get() == "":
                dialogBox.showerror("Erro", "O campo Nome está vazio")
                return
        elif field == "Tipo":
            if type.get() == "":
                dialogBox.showerror("Erro", "O campo Tipo está vazio")
                return
        elif field == "Descrição":
            if description.get() == "":
                dialogBox.showerror("Erro", "O campo Descrição está vazio")
                return
        elif field == "Estado":
            if state.get() == "":
                dialogBox.showerror("Erro", "O campo Estado está vazio")
                return

    else:
        file = open("data.txt", "a", encoding="utf-8")

        if type.get() == "Emprestei":
            type = 0

        else:
            type = 1

        if state.get() == "Por Devolver":
            state = 0
        else:
            state = 1

        file.write(f"\n{name.get()};{date.get()};{type};{description.get()};{state}")

        file.close()

        if type == 0:
            type = "Emprestei"

        else:
            type = "Emprestaram-me"

        if state == 0:
            state = "Por Devolver"
        else:
            state = "Devolvido"

        treeview.insert(
            "",
            "end",
            text=name.get(),
            values=(
                name.get(),
                date.get(),
                type,
                description.get(),
                state,
            ),
        )

        return messagebox.showinfo("Sucesso", "O empréstimo foi adicionado com sucesso")


def update_loan(
    treeview: ttk.Treeview,
    dialogBox: messagebox,
    date: ttk.Entry,
    name: ttk.Entry,
    type: ttk.Combobox,
    description: ttk.Entry,
    state: ttk.Combobox,
):
    """
    This function updates the selected loan on the treeview.

    :param treeview: The treeview that is going to be filled with data.
    :param dialogBox: The messagebox that is going to be used to show the error messages.
    :param date: The entry that contains the date.
    :param name: The entry that contains the name.
    :param type: The combobox that contains the type.
    :param description: The entry that contains the description.
    :param state: The combobox that contains the state
    """

    POSSIBLE_FIELDS = ["Data", "Nome", "Tipo", "Descrição", "Estado"]

    for field in POSSIBLE_FIELDS:
        if field == "Data":
            if date.get() == "":
                dialogBox.showerror("Erro", "O campo Data está vazio")
                return
        elif field == "Nome":
            if name.get() == "":
                dialogBox.showerror("Erro", "O campo Nome está vazio")
                return
        elif field == "Tipo":
            if type.get() == "":
                dialogBox.showerror("Erro", "O campo Tipo está vazio")
                return
        elif field == "Descrição":
            if description.get() == "":
                dialogBox.showerror("Erro", "O campo Descrição está vazio")
                return
        elif field == "Estado":
            if state.get() == "":
                dialogBox.showerror("Erro", "O campo Estado está vazio")
                return

    else:
        selected = treeview.selection()[0]

        values = treeview.item(selected)["values"]

        date = date.get()
        name = name.get()
        type = type.get()
        description = description.get()
        state = state.get()

        # 40210465 - Checking if the type is "Emprestei" or "Emprestaram-me"
        if type == "Emprestei":
            type = 0
        else:
            type = 1

        # 40210465 - Checking if the state is "Por Devolver" or "Devolvido"
        if state == "Por Devolver":
            state = 0
        else:
            state = 1

        file = open("data.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        file = open("data.txt", "w+", encoding="utf-8")

        for line in lines:
            if values[0] in line:
                file.write(f"{name};{date};{type};{description};{state}\n")
            else:
                file.write(line)

        file.close()

        # 40210465 - Checking if the type is "Emprestei" or "Emprestaram-me"
        if type == 0:
            type = "Emprestei"
        else:
            type = "Emprestaram-me"

        # 40210465 - Checking if the state is "Por Devolver" or "Devolvido"
        if state == 0:
            state = "Por Devolver"
        else:
            state = "Devolvido"

        treeview.item(
            selected, text=name, values=(name, date, type, description, state)
        )

        return messagebox.showinfo("Sucesso", "O empréstimo foi atualizado com sucesso")


def cancel_button(event: tk.Event, *entries):
    """
    This function allows to cancel the add loan and clean the entries.

    :param event: The event that triggers the function.
    :param entries: The entries that are going to be cleaned.
    """

    for entry in entries:
        if isinstance(entry, ttk.Combobox):
            entry.set("")
        else:
            entry.delete(0, tk.END)


def delete_loan(event: tk.Event, treeview: ttk.Treeview, dialogBox: messagebox):
    """
    This function deletes the selected loan on the treeview.

    :param event: The event that triggers the function.
    :param treeview: The treeview that is going to be filled with data.
    """

    if not treeview.selection():
        return dialogBox.showerror("Erro", "Selecione um empréstimo")

    confirm = dialogBox.askyesno(
        "Confirmação", "Tem a certeza que quer eliminar o empréstimo?"
    )

    if confirm:
        selected = treeview.selection()[0]

        values = treeview.item(selected)["values"]

        file = open("data.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        file = open("data.txt", "w+", encoding="utf-8")

        for line in lines:
            if values[0] not in line:
                file.write(line)

        file.close()

        treeview.delete(selected)

        return dialogBox.showinfo("Sucesso", "O empréstimo foi eliminado com sucesso")


def insert_mouths(event: tk.Event, combobox: ttk.Combobox):
    """
    This function inserts the mouths into the combobox.

    :param event: The event that triggers the function.
    :param combobox: The combobox that is going to be filled with data.
    """

    combobox["values"] = [
        "",
        "Janeiro",
        "Fevereiro",
        "Março",
        "Abril",
        "Maio",
        "Junho",
        "Julho",
        "Agosto",
        "Setembro",
        "Outubro",
        "Novembro",
        "Dezembro",
    ]
    combobox["state"] = "readonly"


def insert_filtered_loans_by_type(loan_type: str):
    """
    This function allows to get the loans by type.
    """

    file = open("data.txt", "r", encoding="utf-8")

    lines = file.readlines()

    # ignoring the first line
    lines.pop(0)

    loans = []

    for line in lines:
        if loan_type == "Emprestei":
            if line.split(";")[2] == "0":
                loans.append(line)
        else:
            if line.split(";")[2] == "1":
                loans.append(line)

    file.close()

    return loans


def insert_filtered_loans_by_state(loan_state: str):
    """
    This function allows to get the loans by state.
    """

    file = open("data.txt", "r", encoding="utf-8")

    lines = file.readlines()

    # ignoring the first line
    lines.pop(0)

    loans = []

    for line in lines:
        if loan_state == "Por Devolver":
            if line.split(";")[4].strip() == "0":
                loans.append(line)
        else:
            if line.split(";")[4].strip() == "1":
                loans.append(line)

    file.close()

    return loans


def insert_filtered_loans(
    event: tk.Event,
    treeview: ttk.Treeview,
    mouth: ttk.Combobox,
    loan_type: tk.Radiobutton,
    loan_state: tk.Radiobutton,
):
    """
    This function inserts the filtered loans into the treeview.

    :param event: The event that triggers the function.
    :param treeview: The treeview that is going to be filled with data.
    :param mouth: The combobox that contains the mouth.
    :param loan_type: The radiobutton that contains the loan type.
    :param loan_state: The radiobutton that contains the loan state.
    """

    mouth = mouth.get()
    loan_type = loan_type.get()
    loan_state = loan_state.get()
    # cleaning the treeview
    treeview.delete(*treeview.get_children())

    file = open("data.txt", "r", encoding="utf-8")

    lines = file.readlines()

    # ignoring the first line
    lines.pop(0)

    for line in lines:
        # slicing the date to get only the mouth
        mouth_file = line.split(";")[1][3:5]
        loan_type_file = line.split(";")[2]
        loan_state_file = line.split(";")[4].strip()

        if (
            mouth == "Janeiro"
            and loan_type == "Emprestei"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "01" and loan_type_file == "0" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

                if tipo_emprestimo == 0:
                    tipo_emprestimo = "Emprestei"
                else:
                    tipo_emprestimo = "Emprestaram-me"

                if estado == 0:
                    estado = "Por Devolver"
                else:
                    estado = "Devolvido"

                treeview.insert(
                    "",
                    "end",
                    text=nome,
                    values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
                )

        if (
            mouth == "Janeiro"
            and loan_type == "Emprestaram-me"
            and loan_state == "Devolvido"
        ):
            if mouth_file == "01" and loan_type_file == "1" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

                if tipo_emprestimo == 0:
                    tipo_emprestimo = "Emprestei"
                else:
                    tipo_emprestimo = "Emprestaram-me"

                if estado == 0:
                    estado = "Por Devolver"
                else:
                    estado = "Devolvido"

                treeview.insert(
                    "",
                    "end",
                    text=nome,
                    values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
                )

        if (
            mouth == "Janeiro"
            and loan_type == "Emprestaram-me"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "01" and loan_type_file == "1" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

                if tipo_emprestimo == 0:
                    tipo_emprestimo = "Emprestei"
                else:
                    tipo_emprestimo = "Emprestaram-me"

                if estado == 0:
                    estado = "Por Devolver"
                else:
                    estado = "Devolvido"

                treeview.insert(
                    "",
                    "end",
                    text=nome,
                    values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
                )

        if (
            mouth == "Janeiro"
            and loan_type == "Emprestei"
            and loan_state == "Devolvido"
        ):
            if mouth_file == "01" and loan_type_file == "0" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

                if tipo_emprestimo == 0:
                    tipo_emprestimo = "Emprestei"
                else:
                    tipo_emprestimo = "Emprestaram-me"

                if estado == 0:
                    estado = "Por Devolver"
                else:
                    estado = "Devolvido"

                treeview.insert(
                    "",
                    "end",
                    text=nome,
                    values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
                )

        if (
            mouth == "Fevereiro"
            and loan_type == "Emprestei"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "02" and loan_type_file == "0" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

                if tipo_emprestimo == 0:
                    tipo_emprestimo = "Emprestei"
                else:
                    tipo_emprestimo = "Emprestaram-me"

                if estado == 0:
                    estado = "Por Devolver"
                else:
                    estado = "Devolvido"

                treeview.insert(
                    "",
                    "end",
                    text=nome,
                    values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
                )

        if (
            mouth == "Fevereiro"
            and loan_type == "Emprestaram-me"
            and loan_state == "Devolvido"
        ):
            if mouth_file == "02" and loan_type_file == "1" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

                if tipo_emprestimo == 0:
                    tipo_emprestimo = "Emprestei"
                else:
                    tipo_emprestimo = "Emprestaram-me"

                if estado == 0:
                    estado = "Por Devolver"
                else:
                    estado = "Devolvido"

                treeview.insert(
                    "",
                    "end",
                    text=nome,
                    values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
                )

        if (
            mouth == "Fevereiro"
            and loan_type == "Emprestaram-me"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "02" and loan_type_file == "1" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

                if tipo_emprestimo == 0:
                    tipo_emprestimo = "Emprestei"
                else:
                    tipo_emprestimo = "Emprestaram-me"

                if estado == 0:
                    estado = "Por Devolver"
                else:
                    estado = "Devolvido"

                treeview.insert(
                    "",
                    "end",
                    text=nome,
                    values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
                )

        if (
            mouth == "Fevereiro"
            and loan_type == "Emprestei"
            and loan_state == "Devolvido"
        ):
            if mouth_file == "02" and loan_type_file == "0" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

                if tipo_emprestimo == 0:
                    tipo_emprestimo = "Emprestei"
                else:
                    tipo_emprestimo = "Emprestaram-me"

                if estado == 0:
                    estado = "Por Devolver"
                else:
                    estado = "Devolvido"

                treeview.insert(
                    "",
                    "end",
                    text=nome,
                    values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
                )

        if (
            mouth == "Março"
            and loan_type == "Emprestei"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "03" and loan_type_file == "0" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = line.split(";")[2]
                descricao = line.split(";")[3]
                estado = line.split(";")[4].strip()

                if tipo_emprestimo == "0":
                    tipo_emprestimo = "Emprestei"
                else:
                    tipo_emprestimo = "Emprestaram-me"

                if estado == "0":
                    estado = "Por Devolver"
                else:
                    estado = "Devolvido"

                treeview.insert(
                    "",
                    "end",
                    text=nome,
                    values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
                )

        if (
            mouth == "Março"
            and loan_type == "Emprestaram-me"
            and loan_state == "Devolvido"
        ):
            if mouth_file == "03" and loan_type_file == "1" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = line.split(";")[2]
                descricao = line.split(";")[3]
                estado = line.split(";")[4].strip()

                if tipo_emprestimo == "0":
                    tipo_emprestimo = "Emprestei"
                else:
                    tipo_emprestimo = "Emprestaram-me"

                if estado == "0":
                    estado = "Por Devolver"
                else:
                    estado = "Devolvido"

                treeview.insert(
                    "",
                    "end",
                    text=nome,
                    values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
                )

        if (
            mouth == "Março"
            and loan_type == "Emprestaram-me"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "03" and loan_type_file == "1" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = line.split(";")[2]
                descricao = line.split(";")[3]
                estado = line.split(";")[4].strip()

                if tipo_emprestimo == "0":
                    tipo_emprestimo = "Emprestei"
                else:
                    tipo_emprestimo = "Emprestaram-me"

                if estado == "0":
                    estado = "Por Devolver"
                else:
                    estado = "Devolvido"

                treeview.insert(
                    "",
                    "end",
                    text=nome,
                    values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
                )

        if mouth == "Março" and loan_type == "Emprestei" and loan_state == "Devolvido":
            if mouth_file == "03" and loan_type_file == "0" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = line.split(";")[2]
                descricao = line.split(";")[3]
                estado = line.split(";")[4].strip()

                if tipo_emprestimo == "0":
                    tipo_emprestimo = "Emprestei"
                else:
                    tipo_emprestimo = "Emprestaram-me"

                if estado == "0":
                    estado = "Por Devolver"
                else:
                    estado = "Devolvido"

                treeview.insert(
                    "",
                    "end",
                    text=nome,
                    values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
                )
        if (
            mouth == "Abril"
            and loan_type == "Emprestei"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "04" and loan_type_file == "0" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = line.split(";")[2]
                descricao = line.split(";")[3]
                estado = line.split(";")[4].strip()

                if tipo_emprestimo == "0":
                    tipo_emprestimo = "Emprestei"
                else:
                    tipo_emprestimo = "Emprestaram-me"

                if estado == "0":
                    estado = "Por Devolver"
                else:
                    estado = "Devolvido"

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )
        if (
            mouth == "Abril"
            and loan_type == "Emprestaram-me"
            and loan_state == "Devolvido"
        ):
            if mouth_file == "04" and loan_type_file == "1" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = line.split(";")[2]
                descricao = line.split(";")[3]
                estado = line.split(";")[4].strip()

                if tipo_emprestimo == "0":
                    tipo_emprestimo = "Emprestei"
                else:
                    tipo_emprestimo = "Emprestaram-me"

                if estado == "0":
                    estado = "Por Devolver"
                else:
                    estado = "Devolvido"

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )

        if (
            mouth == "Abril"
            and loan_type == "Emprestaram-me"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "04" and loan_type_file == "1" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = line.split(";")[2]
                descricao = line.split(";")[3]
                estado = line.split(";")[4].strip()

                if tipo_emprestimo == "0":
                    tipo_emprestimo = "Emprestei"
                else:
                    tipo_emprestimo = "Emprestaram-me"

                if estado == "0":
                    estado = "Por Devolver"
                else:
                    estado = "Devolvido"

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )

        if mouth == "Abril" and loan_type == "Emprestei" and loan_state == "Devolvido":
            if mouth_file == "04" and loan_type_file == "0" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = line.split(";")[2]
                descricao = line.split(";")[3]
                estado = line.split(";")[4].strip()

                if tipo_emprestimo == "0":
                    tipo_emprestimo = "Emprestei"
                else:
                    tipo_emprestimo = "Emprestaram-me"

                if estado == "0":
                    estado = "Por Devolver"
                else:
                    estado = "Devolvido"

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )
        if (
            mouth == "Maio"
            and loan_type == "Emprestei"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "05" and loan_type_file == "0" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = line.split(";")[2]
                descricao = line.split(";")[3]
                estado = line.split(";")[4].strip()

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )
        if (
            mouth == "Maio"
            and loan_type == "Emprestaram-me"
            and loan_state == "Devolvido"
        ):
            if mouth_file == "05" and loan_type_file == "1" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = line.split(";")[2]
                descricao = line.split(";")[3]
                estado = line.split(";")[4].strip()

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )
        if (
            mouth == "Maio"
            and loan_type == "Emprestaram-me"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "05" and loan_type_file == "1" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = line.split(";")[2]
                descricao = line.split(";")[3]
                estado = line.split(";")[4].strip()

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )

        if mouth == "Maio" and loan_type == "Emprestei" and loan_state == "Devolvido":
            if mouth_file == "05" and loan_type_file == "0" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = line.split(";")[2]
                descricao = line.split(";")[3]
                estado = line.split(";")[4].strip()

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )
        if (
            mouth == "Junho"
            and loan_type == "Emprestei"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "06" and loan_type_file == "0" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )
        if (
            mouth == "Junho"
            and loan_type == "Emprestaram-me"
            and loan_state == "Devolvido"
        ):
            if mouth_file == "06" and loan_type_file == "1" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )
        if (
            mouth == "Junho"
            and loan_type == "Emprestaram-me"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "06" and loan_type_file == "1" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )
        if mouth == "Junho" and loan_type == "Emprestei" and loan_state == "Devolvido":
            if mouth_file == "06" and loan_type_file == "0" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )
        if (
            mouth == "Julho"
            and loan_type == "Emprestei"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "07" and loan_type_file == "0" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )

        if (
            mouth == "Julho"
            and loan_type == "Emprestaram-me"
            and loan_state == "Devolvido"
        ):
            if mouth_file == "07" and loan_type_file == "1" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )

        if (
            mouth == "Julho"
            and loan_type == "Emprestaram-me"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "07" and loan_type_file == "1" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )

        if mouth == "Julho" and loan_type == "Emprestei" and loan_state == "Devolvido":
            if mouth_file == "07" and loan_type_file == "0" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )

        if (
            mouth == "Agosto"
            and loan_type == "Emprestei"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "08" and loan_type_file == "0" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )

        if (
            mouth == "Agosto"
            and loan_type == "Emprestaram-me"
            and loan_state == "Devolvido"
        ):
            if mouth_file == "08" and loan_type_file == "1" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )

        if (
            mouth == "Agosto"
            and loan_type == "Emprestaram-me"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "08" and loan_type_file == "1" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )

        if mouth == "Agosto" and loan_type == "Emprestei" and loan_state == "Devolvido":
            if mouth_file == "08" and loan_type_file == "0" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )

        if (
            mouth == "Setembro"
            and loan_type == "Emprestei"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "09" and loan_type_file == "0" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = line.split(";")[2]
                descricao = line.split(";")[3]
                estado = line.split(";")[4].strip()

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )

        if (
            mouth == "Setembro"
            and loan_type == "Emprestaram-me"
            and loan_state == "Devolvido"
        ):
            if mouth_file == "09" and loan_type_file == "1" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = line.split(";")[2]
                descricao = line.split(";")[3]
                estado = line.split(";")[4].strip()

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )

        if (
            mouth == "Setembro"
            and loan_type == "Emprestaram-me"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "09" and loan_type_file == "1" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = line.split(";")[2]
                descricao = line.split(";")[3]
                estado = line.split(";")[4].strip()

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )

        if (
            mouth == "Setembro"
            and loan_type == "Emprestei"
            and loan_state == "Devolvido"
        ):
            if mouth_file == "09" and loan_type_file == "0" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = line.split(";")[2]
                descricao = line.split(";")[3]
                estado = line.split(";")[4].strip()

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )

        if (
            mouth == "Outubro"
            and loan_type == "Emprestei"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "10" and loan_type_file == "0" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = line.split(";")[2]
                descricao = line.split(";")[3]
                estado = line.split(";")[4].strip()

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )

        if (
            mouth == "Outubro"
            and loan_type == "Emprestaram-me"
            and loan_state == "Devolvido"
        ):
            if mouth_file == "10" and loan_type_file == "1" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = line.split(";")[2]
                descricao = line.split(";")[3]
                estado = line.split(";")[4].strip()

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )

        if (
            mouth == "Outubro"
            and loan_type == "Emprestaram-me"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "10" and loan_type_file == "1" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = line.split(";")[2]
                descricao = line.split(";")[3]
                estado = line.split(";")[4].strip()

            treeview.insert(
                "",
                "end",
                text=nome,
                values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
            )

        if (
            mouth == "Outubro"
            and loan_type == "Emprestei"
            and loan_state == "Devolvido"
        ):
            if mouth_file == "10" and loan_type_file == "0" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = line.split(";")[2]
                descricao = line.split(";")[3]
                estado = line.split(";")[4].strip()

                treeview.insert(
                    "",
                    "end",
                    text=nome,
                    values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
                )

        if (
            mouth == "Novembro"
            and loan_type == "Emprestei"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "11" and loan_type_file == "0" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

                treeview.insert(
                    "",
                    "end",
                    text=nome,
                    values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
                )

        if (
            mouth == "Novembro"
            and loan_type == "Emprestaram-me"
            and loan_state == "Devolvido"
        ):
            if mouth_file == "11" and loan_type_file == "1" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

                treeview.insert(
                    "",
                    "end",
                    text=nome,
                    values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
                )

        if (
            mouth == "Novembro"
            and loan_type == "Emprestaram-me"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "11" and loan_type_file == "1" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

                treeview.insert(
                    "",
                    "end",
                    text=nome,
                    values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
                )

        if (
            mouth == "Novembro"
            and loan_type == "Emprestei"
            and loan_state == "Devolvido"
        ):
            if mouth_file == "11" and loan_type_file == "0" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

                treeview.insert(
                    "",
                    "end",
                    text=nome,
                    values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
                )

        if (
            mouth == "Dezembro"
            and loan_type == "Emprestei"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "12" and loan_type_file == "0" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

                treeview.insert(
                    "",
                    "end",
                    text=nome,
                    values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
                )

        if (
            mouth == "Dezembro"
            and loan_type == "Emprestaram-me"
            and loan_state == "Devolvido"
        ):
            if mouth_file == "12" and loan_type_file == "1" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

                treeview.insert(
                    "",
                    "end",
                    text=nome,
                    values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
                )

        if (
            mouth == "Dezembro"
            and loan_type == "Emprestaram-me"
            and loan_state == "Por Devolver"
        ):
            if mouth_file == "12" and loan_type_file == "1" and loan_state_file == "0":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

                treeview.insert(
                    "",
                    "end",
                    text=nome,
                    values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
                )

        if (
            mouth == "Dezembro"
            and loan_type == "Emprestei"
            and loan_state == "Devolvido"
        ):
            if mouth_file == "12" and loan_type_file == "0" and loan_state_file == "1":

                nome = line.split(";")[0]
                data_emprestimo = line.split(";")[1]
                tipo_emprestimo = int(line.split(";")[2])
                descricao = line.split(";")[3]
                estado = int(line.split(";")[4].strip())

                treeview.insert(
                    "",
                    "end",
                    text=nome,
                    values=(nome, data_emprestimo, tipo_emprestimo, descricao, estado),
                )

    file.close()
