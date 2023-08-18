import tkinter as tk

Window = tk.Tk()
Window.title("button Images")
Window.geometry("1000x500")

# SEARCH BUTTON
btnSearch = tk.Button(Window, text="", width=35, height=35)
btnSearch.place(x=10, y=10)

# incluir uma imagem no botão 'pesquisar.png' na pasta imagens
imgSearch = tk.PhotoImage(file="images/pesquisar.png")
# reduzir o tamanho da imagem
imgSearch = imgSearch.subsample(12, 12)
# remover a borda do botão
btnSearch.config(bd=0)
btnSearch.config(image=imgSearch, compound=tk.TOP, cursor="hand2")

# ASC BUTTON
ascButton = tk.Button(Window, text="", width=45, height=65)
# posicionar o botão ao lado do botão de pesquisa 
ascButton.place(x=60, y=10)
    
imgAsc = tk.PhotoImage(file="images/asc.png")
# aumentar o tamanho da imagem
imgAsc = imgAsc.zoom(2, 2)
ascButton.config(bd=0)
ascButton.config(image=imgAsc, compound=tk.TOP, cursor="hand2")


Window.mainloop()