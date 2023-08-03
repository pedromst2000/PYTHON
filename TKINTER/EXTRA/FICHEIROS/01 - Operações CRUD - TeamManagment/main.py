import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import IntVar


Window = tk.Tk()
Window.title("Team Manager")
Window.geometry("1000x380")


labelPlayer = tk.Label(Window, text="Player:")
labelPlayer.place(x=10, y=10)

entryPlayer = tk.Entry(Window, width=30)
entryPlayer.place(x=60, y=10)


# container com title posição
container = tk.LabelFrame(Window, text="Position",
                          width=200, height=160, relief="sunken", bd=1)
container.place(x=50, y=50)

selectedPositionGK = IntVar()
selectedPositionDEF = IntVar()
selectedPositionMID = IntVar()
selectedPositionATT = IntVar()

# container com title 'Overview'
containerOverview = tk.LabelFrame(
    Window, text="Overview", width=200, height=150, relief="sunken", bd=1)
containerOverview.place(x=50, y=220)

# label GK
labelGK = tk.Label(containerOverview, text="GK")
labelGK.place(x=10, y=10)
# ENTRY GK
entryGK = tk.Entry(containerOverview, width=8)
entryGK.place(x=40, y=10)

# label DEF
labelDEF = tk.Label(containerOverview, text="DEF")
labelDEF.place(x=10, y=40)
# ENTRY DEF
entryDEF = tk.Entry(containerOverview, width=8)
entryDEF.place(x=40, y=40)

# label MID
labelMID = tk.Label(containerOverview, text="MID")
labelMID.place(x=10, y=70)
# ENTRY MID
entryMID = tk.Entry(containerOverview, width=8)
entryMID.place(x=40, y=70)

# label ATT
labelATT = tk.Label(containerOverview, text="ATT")
labelATT.place(x=10, y=100)
# ENTRY ATT
entryATT = tk.Entry(containerOverview, width=8)
entryATT.place(x=40, y=100)

# label 'All'
labelAll = tk.Label(containerOverview, text="All")
labelAll.place(x=100, y=10)
# ENTRY 'All'
entryAll = tk.Entry(containerOverview, width=8)
entryAll.place(x=130, y=10)

# bloquear os campos
entryGK.config(state="readonly")
entryDEF.config(state="readonly")
entryMID.config(state="readonly")
entryATT.config(state="readonly")
entryAll.config(state="readonly")


# check button 'GK'
checkGK = tk.Checkbutton(container, text="GK",
                         variable=selectedPositionGK)
checkGK.place(x=10, y=10)

# check button 'DEF'
checkDEF = tk.Checkbutton(container, text="DEF",
                          variable=selectedPositionDEF)
checkDEF.place(x=10, y=40)

# check button 'MID'
checkMID = tk.Checkbutton(container, text="MID",
                          variable=selectedPositionMID)
checkMID.place(x=10, y=70)

# check button 'ATT'
checkATT = tk.Checkbutton(container, text="ATT",
                          variable=selectedPositionATT)
checkATT.place(x=10, y=100)


labelTeam = tk.Label(Window, text="Team :")
labelTeam.place(x=320, y=10)

entryTeam = tk.Entry(Window, width=30)
entryTeam.place(x=370, y=10)

# colocar um treeview ao lado do container com title posição
# com colunas 'Player' 'Team' 'Position'
treeView = ttk.Treeview(Window, columns=(
    "Player", "Team", "Position"), show="headings", height=10)
treeView.place(x=320, y=50)

# definir o tamanho das colunas
treeView.column("Player", width=200)
treeView.column("Team", width=200)
treeView.column("Position", width=200)

# definir o nome das colunas
treeView.heading("Player", text="Player")
treeView.heading("Team", text="Team")
treeView.heading("Position", text="Position")

# colocar uma scrollbar vertical
scrollbar = ttk.Scrollbar(Window, orient="vertical", command=treeView.yview)
scrollbar.place(x=900, y=50, height=200)

# botão 'Pesquisar'
buttonSearch = tk.Button(Window, text="Search", width=10,
                         relief="raised", borderwidth=3)
buttonSearch.place(x=320, y=300)

# botão 'Adicionar'
buttonAdd = tk.Button(Window, text="Add", width=10,
                      relief="raised", borderwidth=3)
buttonAdd.place(x=420, y=300)

# botão 'Editar'
buttonEdit = tk.Button(Window, text="Edit", width=10,
                       relief="raised", borderwidth=3)
buttonEdit.place(x=520, y=300)

# botão 'Apagar'
buttonDelete = tk.Button(Window, text="Delete", width=10,
                         relief="raised", borderwidth=3)
buttonDelete.place(x=620, y=300)

# botão 'Reiniciar'
buttonReset = tk.Button(Window, text="Reset", width=10,
                        relief="raised", borderwidth=3)
buttonReset.place(x=720, y=300)


def resetView():
    # limpar o treeview
    treeView.delete(*treeView.get_children())
    # limpar os campos
    entryPlayer.delete(0, tk.END)
    entryTeam.delete(0, tk.END)
    # apresentar todos os jogadores
    allPLayersView()


def allPLayersView():
    # limpar o treeview
    treeView.delete(*treeView.get_children())
    # ler o ficheiro 'players.txt'
    file = open("players.txt", "r", encoding="utf-8")
    # ler todas as linhas do ficheiro
    lines = file.readlines()
    # percorrer todas as linhas
    for line in lines:
        # separar os campos por ';'
        fields = line.split(";")
        # inserir os campos no treeview
        treeView.insert("", "end", values=(fields[0], fields[1], fields[2]))
    # fechar o ficheiro
    file.close()


def searchPlayer():
    # ler os valores dos campos
    player = entryPlayer.get()
    team = entryTeam.get()
    # limpar o treeview
    treeView.delete(*treeView.get_children())

    # filtrar por equipa somente
    if player == "" and team != "":
        # aceitar letras maiusculas e minusculas
        team = team.lower()  # permite encontrar em qualquer posição da string
        # ler o ficheiro 'players.txt'
        file = open("players.txt", "r", encoding="utf-8")
        # ler todas as linhas do ficheiro
        lines = file.readlines()
        # percorrer todas as linhas
        for line in lines:
            # separar os campos por ';'
            fields = line.split(";")
            # aceitar letras maiusculas e minusculas
            teamFile = fields[1].lower()
            # verificar se a equipa existe
            if team in teamFile:
                # inserir os campos no treeview
                treeView.insert("", "end", values=(
                    fields[0], fields[1], fields[2]))
        # fechar o ficheiro
        file.close()

    # filtrar por jogador somente
    elif player != "" and team == "":
        player = player.lower()
        file = open("players.txt", "r", encoding="utf-8")
        lines = file.readlines()
        for line in lines:
            fields = line.split(";")
            playerFile = fields[0].lower()
            # verificar se o jogador existe
            if player in playerFile:
                treeView.insert("", "end", values=(
                    fields[0], fields[1], fields[2]))
        file.close()

    # filtrar por jogador e equipa
    elif player != "" and team != "":
        player = player.lower()
        team = team.lower()
        file = open("players.txt", "r", encoding="utf-8")
        lines = file.readlines()
        for line in lines:
            fields = line.split(";")
            playerFile = fields[0].lower()
            teamFile = fields[1].lower()
            # verificar se o jogador e a equipa existem
            if player in playerFile and team in teamFile:
                treeView.insert("", "end", values=(
                    fields[0], fields[1], fields[2]))
        file.close()

        # FILTRA POSIÇÕES ESPECÍFICAS
    # filtrar por posição somente (GK)
    elif selectedPositionGK.get() == 1 and selectedPositionDEF.get() == 0 and selectedPositionMID.get() == 0 and selectedPositionATT.get() == 0 and player == "" and team == "":
        # ler o ficheiro 'players.txt'
        file = open("players.txt", "r", encoding="utf-8")
        # ler todas as linhas do ficheiro
        lines = file.readlines()
        # percorrer todas as linhas
        for line in lines:
            # separar os campos por ';'
            fields = line.split(";")
            # verificar se a posição existe
            if "GK" in fields[2]:
                # inserir os campos no treeview
                treeView.insert("", "end", values=(
                    fields[0], fields[1], fields[2]))
        # fechar o ficheiro
        file.close()

    # filtrar por posição somente (DEF)
    elif selectedPositionGK.get() == 0 and selectedPositionDEF.get() == 1 and selectedPositionMID.get() == 0 and selectedPositionATT.get() == 0 and player == "" and team == "":
        file = open("players.txt", "r", encoding="utf-8")
        lines = file.readlines()
        for line in lines:
            fields = line.split(";")
            if "DEF" in fields[2]:
                treeView.insert("", "end", values=(
                    fields[0], fields[1], fields[2]))
        file.close()

    # filtrar por posição somente (MID)
    elif selectedPositionGK.get() == 0 and selectedPositionDEF.get() == 0 and selectedPositionMID.get() == 1 and selectedPositionATT.get() == 0 and player == "" and team == "":
        file = open("players.txt", "r", encoding="utf-8")
        lines = file.readlines()
        for line in lines:
            fields = line.split(";")
            if "MID" in fields[2]:
                treeView.insert("", "end", values=(
                    fields[0], fields[1], fields[2]))
        file.close()

    # filtrar por posição somente (ATT)
    elif selectedPositionGK.get() == 0 and selectedPositionDEF.get() == 0 and selectedPositionMID.get() == 0 and selectedPositionATT.get() == 1 and player == "" and team == "":
        # converter 1 para 'ATT'
        position = "ATT"
        file = open("players.txt", "r", encoding="utf-8")
        lines = file.readlines()
        for line in lines:
            fields = line.split(";")
            if position in fields[2]:
                treeView.insert("", "end", values=(
                    fields[0], fields[1], fields[2]))
        file.close()

        # FILTRAR MAIS QUE UMA POSIÇÃO
    # filtrar por posição somente (GK e DEF)
    elif selectedPositionGK.get() == 1 and selectedPositionDEF.get() == 1 and selectedPositionMID.get() == 0 and selectedPositionATT.get() == 0 and player == "" and team == "":
        file = open("players.txt", "r", encoding="utf-8")
        lines = file.readlines()
        for line in lines:
            fields = line.split(";")
            if "GK" in fields[2] or "DEF" in fields[2]:
                treeView.insert("", "end", values=(
                    fields[0], fields[1], fields[2]))
        file.close()

    # filtrar por posição somente (GK e MID)
    elif selectedPositionGK.get() == 1 and selectedPositionDEF.get() == 0 and selectedPositionMID.get() == 1 and selectedPositionATT.get() == 0 and player == "" and team == "":
        file = open("players.txt", "r", encoding="utf-8")
        lines = file.readlines()
        for line in lines:
            fields = line.split(";")
            if "GK" in fields[2] or "MID" in fields[2]:
                treeView.insert("", "end", values=(
                    fields[0], fields[1], fields[2]))
        file.close()

    # filtrar por posição somente (GK e ATT)
    elif selectedPositionGK.get() == 1 and selectedPositionDEF.get() == 0 and selectedPositionMID.get() == 0 and selectedPositionATT.get() == 1 and player == "" and team == "":
        file = open("players.txt", "r", encoding="utf-8")
        lines = file.readlines()
        for line in lines:
            fields = line.split(";")
            if "GK" in fields[2] or "ATT" in fields[2]:
                treeView.insert("", "end", values=(
                    fields[0], fields[1], fields[2]))
        file.close()

    # filtrar por posição somente (DEF e MID)
    elif selectedPositionGK.get() == 0 and selectedPositionDEF.get() == 1 and selectedPositionMID.get() == 1 and selectedPositionATT.get() == 0 and player == "" and team == "":
        file = open("players.txt", "r", encoding="utf-8")
        lines = file.readlines()
        for line in lines:
            fields = line.split(";")
            if "DEF" in fields[2] or "MID" in fields[2]:
                treeView.insert("", "end", values=(
                    fields[0], fields[1], fields[2]))
        file.close()

    # filtrar por posição somente (DEF e ATT)
    elif selectedPositionGK.get() == 0 and selectedPositionDEF.get() == 1 and selectedPositionMID.get() == 0 and selectedPositionATT.get() == 1 and player == "" and team == "":
        file = open("players.txt", "r", encoding="utf-8")
        lines = file.readlines()
        for line in lines:
            fields = line.split(";")
            if "DEF" in fields[2] or "ATT" in fields[2]:
                treeView.insert("", "end", values=(
                    fields[0], fields[1], fields[2]))
        file.close()

    # filtrar por posição somente (MID e ATT)
    elif selectedPositionGK.get() == 0 and selectedPositionDEF.get() == 0 and selectedPositionMID.get() == 1 and selectedPositionATT.get() == 1 and player == "" and team == "":
        file = open("players.txt", "r", encoding="utf-8")
        lines = file.readlines()
        for line in lines:
            fields = line.split(";")
            if "MID" in fields[2] or "ATT" in fields[2]:
                treeView.insert("", "end", values=(
                    fields[0], fields[1], fields[2]))
        file.close()

        # FILTRAR MAIS QUE DUAS POSIÇÕES
    # filtrar por posição somente (GK, DEF e MID)
    elif selectedPositionGK.get() == 1 and selectedPositionDEF.get() == 1 and selectedPositionMID.get() == 1 and selectedPositionATT.get() == 0 and player == "" and team == "":
        file = open("players.txt", "r", encoding="utf-8")
        lines = file.readlines()
        for line in lines:
            fields = line.split(";")
            if "GK" in fields[2] or "DEF" in fields[2] or "MID" in fields[2]:
                treeView.insert("", "end", values=(
                    fields[0], fields[1], fields[2]))
        file.close()
    # filtrar por posição somente (GK, DEF e ATT)
    elif selectedPositionGK.get() == 1 and selectedPositionDEF.get() == 1 and selectedPositionMID.get() == 0 and selectedPositionATT.get() == 1 and player == "" and team == "":
        file = open("players.txt", "r", encoding="utf-8")
        lines = file.readlines()
        for line in lines:
            fields = line.split(";")
            if "GK" in fields[2] or "DEF" in fields[2] or "ATT" in fields[2]:
                treeView.insert("", "end", values=(
                    fields[0], fields[1], fields[2]))
        file.close()
    # filtrar por posição somente (GK, MID e ATT)
    elif selectedPositionGK.get() == 1 and selectedPositionDEF.get() == 0 and selectedPositionMID.get() == 1 and selectedPositionATT.get() == 1 and player == "" and team == "":
        file = open("players.txt", "r", encoding="utf-8")
        lines = file.readlines()
        for line in lines:
            fields = line.split(";")
            if "GK" in fields[2] or "MID" in fields[2] or "ATT" in fields[2]:
                treeView.insert("", "end", values=(
                    fields[0], fields[1], fields[2]))
        file.close()
    # filtrar por posição somente (DEF, MID e ATT)
    elif selectedPositionGK.get() == 0 and selectedPositionDEF.get() == 1 and selectedPositionMID.get() == 1 and selectedPositionATT.get() == 1 and player == "" and team == "":
        file = open("players.txt", "r", encoding="utf-8")
        lines = file.readlines()
        for line in lines:
            fields = line.split(";")
            if "DEF" in fields[2] or "MID" in fields[2] or "ATT" in fields[2]:
                treeView.insert("", "end", values=(
                    fields[0], fields[1], fields[2]))
        file.close()

        # FILTRAR TODAS AS POSIÇÕES
    # filtrar por posição somente (GK, DEF, MID e ATT)
    elif selectedPositionGK.get() == 1 and selectedPositionDEF.get() == 1 and selectedPositionMID.get() == 1 and selectedPositionATT.get() == 1 and player == "" and team == "":
        file = open("players.txt", "r", encoding="utf-8")
        lines = file.readlines()
        for line in lines:
            treeView.insert("", "end", values=(line.split(";")))
        file.close()


def addPlayer():
    # abrir o ficheiro 'players.txt' em modo de escrita
    file = open("players.txt", "a", encoding="utf-8")
    # ler os valores dos campos
    player = entryPlayer.get()
    team = entryTeam.get()

    if player == "":
        return messagebox.showwarning("Error", "Player name is required")
    # se não tiver nenhuma posição selecionada
    elif selectedPositionGK.get() == 0 and selectedPositionDEF.get() == 0 and selectedPositionMID.get() == 0 and selectedPositionATT.get() == 0:
        return messagebox.showwarning("Error", "Position for the player is required")
    # se tiver mais que uma posição selecionada
    elif selectedPositionGK.get() == 1 and selectedPositionDEF.get() == 1 and selectedPositionMID.get() == 1 and selectedPositionATT.get() == 1:
        return messagebox.showwarning("Error", "Only one position is required")
    elif selectedPositionGK.get() == 1 and selectedPositionDEF.get() == 1 and selectedPositionMID.get() == 1 and selectedPositionATT.get() == 0:
        return messagebox.showwarning("Error", "Only one position is required")
    elif selectedPositionGK.get() == 1 and selectedPositionDEF.get() == 1 and selectedPositionMID.get() == 0 and selectedPositionATT.get() == 0:
        return messagebox.showwarning("Error", "Only one position is required")
    elif selectedPositionGK.get() == 1 and selectedPositionDEF.get() == 0 and selectedPositionMID.get() == 0 and selectedPositionATT.get() == 1:
        return messagebox.showwarning("Error", "Only one position is required")
    elif selectedPositionGK.get() == 1 and selectedPositionDEF.get() == 0 and selectedPositionMID.get() == 1 and selectedPositionATT.get() == 0:
        return messagebox.showwarning("Error", "Only one position is required")
    elif selectedPositionGK.get() == 0 and selectedPositionDEF.get() == 1 and selectedPositionMID.get() == 0 and selectedPositionATT.get() == 1:
        return messagebox.showwarning("Error", "Only one position is required")
    elif selectedPositionGK.get() == 0 and selectedPositionDEF.get() == 1 and selectedPositionMID.get() == 1 and selectedPositionATT.get() == 0:
        return messagebox.showwarning("Error", "Only one position is required")
    elif selectedPositionGK.get() == 1 and selectedPositionDEF.get() == 1 and selectedPositionMID.get() == 0 and selectedPositionATT.get() == 0:
        return messagebox.showwarning("Error", "Only one position is required")
    elif selectedPositionGK.get() == 0 and selectedPositionDEF.get() == 0 and selectedPositionMID.get() == 1 and selectedPositionATT.get() == 1:
        return messagebox.showwarning("Error", "Only one position is required")
    # se tiver o nome do jogador e a posição selecionada
    elif player != "" and selectedPositionGK.get() == 1:
        file = open("players.txt", "a", encoding="utf-8")
        # escrever no ficheiro
        file.write("\n" + player + ";" + "no team " + ";" + "GK")
        file.close()
        messagebox.showinfo("Success", "Player added successfully")
        # limpar os campos
        entryPlayer.delete(0, tk.END)
        entryTeam.delete(0, tk.END)
        # apresentar todos os jogadores
        allPLayersView()
        count_players()
    elif player != "" and selectedPositionDEF.get() == 1:
        file = open("players.txt", "a", encoding="utf-8")
        # escrever no ficheiro
        file.write("\n" + player + ";" + "no team " + ";" + "DEF")
        file.close()
        messagebox.showinfo("Success", "Player added successfully")
        # limpar os campos
        entryPlayer.delete(0, tk.END)
        entryTeam.delete(0, tk.END)
        # apresentar todos os jogadores
        allPLayersView()
        count_players()
    elif player != "" and selectedPositionMID.get() == 1:
        file = open("players.txt", "a", encoding="utf-8")
        # escrever no ficheiro
        file.write("\n" + player + ";" + "no team " + ";" + "MID")
        file.close()
        messagebox.showinfo("Success", "Player added successfully")
        # limpar os campos
        entryPlayer.delete(0, tk.END)
        entryTeam.delete(0, tk.END)
        # apresentar todos os jogadores
        allPLayersView()
        count_players()
    elif player != "" and selectedPositionATT.get() == 1:
        file = open("players.txt", "a", encoding="utf-8")
        # escrever no ficheiro
        file.write("\n" + player + ";" + "no team " + ";" + "ATT")
        file.close()
        messagebox.showinfo("Success", "Player added successfully")
        # limpar os campos
        entryPlayer.delete(0, tk.END)
        entryTeam.delete(0, tk.END)
        # apresentar todos os jogadores
        allPLayersView()
        count_players()

# atualizar a equipa do jogador selecionado no treeview


def updatePlayer():
    # ler o a linha selecionada no treeview
    selected = treeView.selection()[0]
    # ler os valores da linha selecionada
    values = treeView.item(selected, "values")  # values[1] = nome da equipa
    # ler o nome da equipa
    team = entryTeam.get()

    # atualizar a equipa do jogador selecionado
    if team != "":
        # abrir o ficheiro 'players.txt' em modo de leitura
        file = open("players.txt", "r", encoding="utf-8")
        # ler todas as linhas do ficheiro
        lines = file.readlines()
        # fechar o ficheiro
        file.close()
        # abrir o ficheiro 'players.txt' para leitura e escrita
        file = open("players.txt", "w+", encoding="utf-8")
        # percorrer todas as linhas
        for line in lines:
            # verificar o jogador selecionado
            if values[0] in line:
                # atualizar a equipa
                file.write(values[0] + ";" + team + ";" + values[2])
            else:
                # escrever a linha original
                file.write(line)
        # fechar o ficheiro
        file.close()
        # limpar os campos
        entryPlayer.delete(0, tk.END)
        entryTeam.delete(0, tk.END)
        # apresentar todos os jogadores
        allPLayersView()

        return messagebox.showinfo("Success", f'Team of {values[0]} updated successfully to {team}')


def deletePlayer():
    # remover da treeview o jogador selecionado
    selected = treeView.selection()[0]
    values = treeView.item(selected, "values")

    file = open("players.txt", "r", encoding="utf-8")
    lines = file.readlines()
    for line in lines:
        if values[0] in line:
            # buscar a linha selecionada
            line = line
            # remover a linha selecionada
            replace = line.replace(line, "")
            # abrir o ficheiro 'players.txt' para leitura e escrita
            file = open("players.txt", "w+", encoding="utf-8")
            # percorrer todas as linhas
            for line in lines:
                # verificar o jogador selecionado
                if values[0] in line:
                    # escrever a linha original
                    file.write(replace)
                else:
                    # escrever a linha original
                    file.write(line)
    file.close()
    # apresentar todos os jogadores
    allPLayersView()
    # atualizar o número de jogadores
    count_players()


def askDeletePlayer():
    # perguntar se deseja apagar o jogador
    if messagebox.askyesno("Delete Player", "Are you sure you want to delete this player?"):
        deletePlayer()
        # limpar os campos
        entryPlayer.delete(0, tk.END)
        entryTeam.delete(0, tk.END)
        # apresentar todos os jogadores
        allPLayersView()
    else:
        return False


def count_players():
    countGK = 0
    countDEF = 0
    countMID = 0
    countATT = 0
    countAll = 0

    file = open("players.txt", "r", encoding="utf-8")
    lines = file.readlines()
    for line in lines:
        fields = line.split(";")
        if "GK" in fields[2]:
            countGK += 1
        elif "DEF" in fields[2]:
            countDEF += 1
        elif "MID" in fields[2]:
            countMID += 1
        elif "ATT" in fields[2]:
            countATT += 1
        countAll += 1
    file.close()

    entryGK.config(state="normal")
    entryGK.delete(0, tk.END)
    entryGK.insert(0, countGK)
    entryGK.config(state="readonly")

    entryDEF.config(state="normal")
    entryDEF.delete(0, tk.END)
    entryDEF.insert(0, countDEF)
    entryDEF.config(state="readonly")

    entryMID.config(state="normal")
    entryMID.delete(0, tk.END)
    entryMID.insert(0, countMID)
    entryMID.config(state="readonly")

    entryATT.config(state="normal")
    entryATT.delete(0, tk.END)
    entryATT.insert(0, countATT)
    entryATT.config(state="readonly")

    entryAll.config(state="normal")
    entryAll.delete(0, tk.END)
    entryAll.insert(0, countAll)
    entryAll.config(state="readonly")


buttonSearch.config(command=searchPlayer)
# associar o botão 'Reiniciar' à função 'resetView'
buttonReset.config(command=resetView)
# associar o botão 'Adicionar' à função 'addPlayer'
buttonAdd.config(command=addPlayer)
# associar o botão 'Editar' à função 'updatePlayer'
buttonEdit.config(command=updatePlayer)
# associar o botão 'Apagar' à função 'deletePlayer'
buttonDelete.config(command=askDeletePlayer)

count_players()
allPLayersView()
Window.mainloop()
