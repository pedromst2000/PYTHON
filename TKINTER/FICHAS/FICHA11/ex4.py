import tkinter as tk
# intvar
from tkinter import IntVar

# window
window = tk.Tk()
# tamanho da janela
window.geometry("1000x600")
# titulo da janela
window.title("Massa Corporal")

# container quadratico no canto superior esquerdo da janela
frame = tk.LabelFrame(window, relief="raised",
                      borderwidth=3, width=300, height=250)
frame.place(x=40, y=40)


# colocar um label dentro do container anterior com o texto 'Peso :' com a cor azul
peso = IntVar()
label_peso = tk.Label(frame, text="Peso :", fg="blue", font=("Arial", 10))
label_peso.place(x=30, y=50)

# colocar uma caixa de texto ao lado do label anterior
entry_peso = tk.Entry(frame, width=10, textvariable=peso)
entry_peso.place(x=80, y=50)

altura = IntVar()
# colocar um label abaixo do peso com o texto 'Altura(cm) :' com a cor azul
label_altura = tk.Label(frame, text="Altura(cm) :",
                        fg="blue", font=("Arial", 10))
label_altura.place(x=30, y=100)

# colocar uma caixa de texto ao lado do label anterior
entry_altura = tk.Entry(frame, width=10, textvariable=altura)
entry_altura.place(x=110, y=100)

# container para o resultado abaixo do container anterior
frame2 = tk.LabelFrame(window, relief="raised",
                       borderwidth=3, width=300, height=250)
frame2.place(x=40, y=300)


# colocar um label dentro do container anterior com o texto 'índice de Massa Corporal' com a cor azul
label_imc = tk.Label(frame2, text="índice de Massa Corporal",
                     fg="blue", font=("Arial", 10))
label_imc.place(x=30, y=50)

# colocar um label abaixo do imc com o texto 'Resultado :' com a cor preta
label_resultado = tk.Label(frame2, text="Resultado :",
                           fg="black", font=("Arial", 10))
label_resultado.place(x=30, y=100)

# colocar um texto ao lado do label anterior com o resultado do calculo
label_imc = tk.Label(frame2, text="", fg="black", font=("Arial", 10))
label_imc.place(x=110, y=100)


# colocar dois butões centrados ao lado dos containers anteriores
# botão para calcular 'Calcular IMC'
btn_calc = tk.Button(window, text="Calcular IMC", width=10, height=7)
btn_calc.place(x=400, y=100)

# warp no texto do botão 'Calcular IMC'
btn_calc.config(wraplength=50)

# Botão Sair 'Sair'
btn_sair = tk.Button(window, text="Sair", width=10, height=7)
btn_sair.place(x=400, y=250)

# colocar um canvas ao lado dos botões
canvas = tk.Canvas(window, width=400, height=340,
                   relief="raised", borderwidth=3)
canvas.place(x=500, y=50)

# colocar uma imagem dentro do canvas
img = tk.PhotoImage(file="images.png")
canvas.create_image(200, 170, image=img)


def calcular_IMC():
   # buscar o valor do peso
    peso = float(entry_peso.get())
    # buscar o valor da altura
    altura = int(entry_altura.get())
    imc = peso / (altura/100)**2

    # arrendondar o valor do imc
    imc = round(imc, 2)

    # apresentar cores diferentes para o resultado
    if imc < 18.5:
        # cor azul claro bold
        label_imc.config(text="Abaixo do Peso", fg="light blue",
                         font=("Arial", 10, "bold"))
    elif imc >= 18.5 and imc < 25:
        # cor verde claro bold
        label_imc.config(text="Peso Normal", fg="light green",
                         font=("Arial", 10, "bold"))
    elif imc >= 25 and imc < 30:
        # cor amarelo claro bold
        label_imc.config(text="Sobrepeso", fg="yellow",
                         font=("Arial", 10, "bold"))
    elif imc >= 30 and imc < 35:
        # amarelo escuro bold
        label_imc.config(text="Obesidade Grau 1", fg="yellow4",
                         font=("Arial", 10, "bold"))
    elif imc >= 35 and imc < 40:
        # cor laranja bold
        label_imc.config(text="Obesidade Grau 2", fg="orange",
                         font=("Arial", 10, "bold"))
    else:
        # cor vermelho bold
        label_imc.config(text="Obesidade Grau 3", fg="red",
                         font=("Arial", 10, "bold"))


def sair():
    # função para sair do programa
    window.destroy()


# associar o botão calcular com a função calcular_IMC
btn_calc.config(command=calcular_IMC)
# associar o botão sair com a função sair
btn_sair.config(command=sair)

window.mainloop()
