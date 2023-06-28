import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
from tkinter import ttk

# Load categories from categories.txt file
with open("categorias.txt") as f:
    categories = f.read().splitlines()

movies = []
# Load movies from movies.txt file
def load_movies(category):
    global movies
    movies = []
    with open("filmes.txt") as f:
        lines = f.read().splitlines()
        for line in lines:
            movie_data = line.split(";")
            if movie_data[2] == category:
                movies.append(movie_data)
    if not movies:
        tkinter.messagebox.showerror("Error", "Não há filmes para essa categoria.")
    else:
        display_movies(tree, movies)


# Function to populate Treeview with movies
def display_movies(tree, movies):
    clear_tree(tree)
    for movie in movies:
        tree.insert("", "end", values=(movie[0], movie[1]))

# Function to clear Treeview
def clear_tree(tree):
    for i in tree.get_children():
        tree.delete(i)

# Function to get the number of movies and the movie with the highest views
def get_movie_stats(movies):
    count = 0
    highest_viewed_movie = None
    highest_views = 0
    for movie in movies:
        count += 1
        if int(movie[1]) > highest_views:
            highest_views = int(movie[1])
            highest_viewed_movie = movie[0]
    resultNumfilms.config(text=f"{count}")
    resultFilmView.config(text=f"{highest_viewed_movie}")

# Function to add movie to movies.txt file
def add_movie(title, views, category):
    with open("filmes.txt", "a") as f:
        f.write(f"{title};{views};{category}\n")
        tk.messagebox.showinfo("Added", f"The movie {title} was added to the {category} category successfully!")

# Main Tkinter window
root = tk.Tk()
root.geometry("1000x500")
root.title("Filmes Dashboard")

# Label to display categories
categories_label = tk.Label(root, text="Categorias:", font=("Helvetica", 11))
categories_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

# Listbox to select category
category_listbox = tk.Listbox(root, font=("Helvetica", 11))
category_listbox.grid(row=1, column=0, padx=10, pady=10)
for category in categories:
    category_listbox.insert("end", category)

# Treeview to display movies
tree = ttk.Treeview(root, columns=("title", "views"), show="headings", padding=(0, 10))
tree.grid(row=0, column=2, rowspan=2, padx=10, pady=10)
tree.heading("title", text="Título do Filme", anchor="e")
tree.heading("views", text="Nº de Visualizações", anchor="c")

# Button to display movies for selected category
display_button = tk.Button(root, text="Exibir", command=lambda: load_movies(category_listbox.get(category_listbox.curselection()[0])))
display_button.grid(row=1, column=1)

showMore = tk.Button(root, text="Categoria| ver +", command=lambda:get_movie_stats(movies))
showMore.grid(row=2, column=0,pady=10)

numFilmsLbl = tk.Label(root, text="Nº de filmes")
numFilmsLbl.grid(row=2, column=1)

resultNumfilms = tk.Label(root, relief="sunken", bg="white", width=5)
resultNumfilms.grid(row=2, column=2, pady=(10,0))

nameFilmViews = tk.Label(root, text="Filme + visto")
nameFilmViews.grid(row=3, column=1)

resultFilmView = tk.Label(root, relief="sunken", bg="white", width=35)
resultFilmView.grid(row=3, column=2, pady=(10,0))

addMovieLabel = tk.Label(root, text="Filme")
addMovieLabel.grid(row = 0, column= 3, padx=(10,0))

inputMovie = tk.Entry(root, width=35)
inputMovie.grid(row=0, column= 4)

addViewsLabel = tk.Label(root, text="Visualizações")
addViewsLabel.grid(row = 1, column= 3, padx=(10,0))

inputViews = tk.Entry(root, width=15)
inputViews.grid(row=1, column= 4)

addMovie = tk.Button(root, text="Acrescentar Filme", command = lambda:add_movie(inputMovie.get(), inputViews.get(), category_listbox.get(category_listbox.curselection()[0])))
addMovie.grid(row = 2, column=3)

displayNew = tk.Button(root, text="Refresh vista", command= lambda:load_movies(category_listbox.get(category_listbox.curselection()[0])))
displayNew.grid(row=2,column=4)

root.mainloop()
