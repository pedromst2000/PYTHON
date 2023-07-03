# libraries
import tkinter as tk
from tkinter import StringVar

# criar um simulador de Peso Ideal

window = tk.Tk()

# tamanho da janela
window.geometry("1200x600")
window.title("Peso Ideal")


# criar um input para introduzir a altura em cm
lblAltura = tk.Label(window, text="Altura em cm:", fg="blue")
lblAltura.place(x=20, y=40, width=200, height=50)

txtAltura = tk.Entry(window)
# posicionar a caixa de texto ao lado do label
txtAltura.place(x=180, y=52, width=200, height=20)

# definir um container com título 'Género' com cor azul
lblGenero = tk.LabelFrame(window, text="Género",
                          fg="blue", borderwidth=5, relief="sunken")
# posicionar o container abaixo do label 'Altura'
lblGenero.place(x=85, y=100, width=280, height=100)

# colocar dois radio buttons dentro do container 'Género'
selected = StringVar()
selected.set('M')

# Masculino
rbMasculino = tk.Radiobutton(
    lblGenero, text="Masculino", value='M', variable=selected)
rbMasculino.place(x=20, y=20, width=100, height=20)

# Feminino
rbFeminino = tk.Radiobutton(
    lblGenero, text="Feminino", value='F', variable=selected)
rbFeminino.place(x=20, y=50, width=100, height=20)

# inserir um botão para calcular o peso ideal ao lado do container 'Género'
btnCalcular = tk.Button(window, text="Calcular Peso Ideal",
                        fg="black", relief="raised", borderwidth=5)

# posicionar o botão ao lado do container 'Género'
btnCalcular.place(x=400, y=100, width=100, height=100)

# fazer wrap do texto do botão
btnCalcular.config(wraplength=80)

# definir um container e posicionar ao lado do botão 'Calcular'
lblPesoIdeal = tk.LabelFrame(window, borderwidth=5, relief="sunken")
lblPesoIdeal.place(x=520, y=100, width=280, height=100)

# colocar um texto com cor azul dentro do container 'Peso Ideal'
lblPesoIdeal = tk.Label(lblPesoIdeal, text="Peso Ideal em Kg", fg="blue")
lblPesoIdeal.place(x=20, y=20, width=100, height=20)

# criar uma caixa de texto para apresentar o resultado
txtPesoIdeal = tk.Entry(window)
# posicionar em baixo do texto 'Peso Ideal'
txtPesoIdeal.place(x=540, y=150, width=120, height=20)


def calcular_peso():
    # 2 = Feminino
    # 4 = Masculino

    # obter o valor da altura
    altura = float(txtAltura.get())

    # obter o valor do género
    genero = selected.get()

    # calcular o peso ideal
    if genero == 'M':
        peso_ideal = (altura - 100) - (altura - 150) / 4
    else:
        peso_ideal = (altura - 100) - (altura - 150) / 2

    # apresentar o resultado na caixa de texto
    txtPesoIdeal.delete(0, tk.END)
    txtPesoIdeal.insert(0, peso_ideal)


# associar o botão 'Calcular' ao método 'calcular_peso'
btnCalcular.config(command=calcular_peso)

# abrir janela
window.mainloop()