import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageTk
from Dijkstra import *  # Assurez-vous que Dijkstra.py contient la définition des fonctions nécessaires

SIZE = 3  # Taille de la grille (3x3 dans ce cas)
CELL_SIZE = 80  # Taille de chaque cellule en pixels

def create_image(text, width, height, bg_color, font_size, font_color):
    image = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", font_size)
    text_size = draw.textbbox((0, 0), text, font=font)  # Correction de la méthode à utiliser ici
    text_width, text_height = text_size[2] - text_size[0], text_size[3] - text_size[1]
    draw.text(((width - text_width) // 2, (height - text_height) // 2), text, font=font, fill=font_color)
    return image

def afficher_grille(frame, grille):
    for i in range(SIZE):
        for j in range(SIZE):
            cell_value = grille[i * SIZE + j]
            if cell_value == 0:
                image = create_image('', CELL_SIZE, CELL_SIZE, "lightgray", CELL_SIZE // 4, "black")
            else:
                image = create_image(str(cell_value), CELL_SIZE, CELL_SIZE, "lightblue", CELL_SIZE // 4, "black")
            tk_image = ImageTk.PhotoImage(image)  # Convertir l'image PIL en ImageTk.PhotoImage
            img_label = tk.Label(frame, image=tk_image)
            img_label.grid(row=i, column=j)
            img_label.image = tk_image  # Gardez une référence à l'image pour éviter qu'elle ne soit supprimée par le ramasse-miettes

def resoudre_taquin(grille_initiale, configurations):
    root = tk.Tk()
    root.title("Résolution du Taquin")

    frame = tk.Frame(root)
    frame.pack()

    label = tk.Label(frame, text="Grille Initiale")
    label.grid(row=SIZE, columnspan=SIZE)

    afficher_grille(frame, grille_initiale)

    def afficher_configuration(configs):
        for config in configs:
            label.config(text="Configuration en cours:")
            afficher_grille(frame, config)
            root.update()
            root.after(1000)  # Délai de 1 seconde
            root.update_idletasks()  # Force la mise à jour de l'interface

    def resoudre():
        afficher_configuration(configurations)

    bouton_resoudre = tk.Button(root, text="Résoudre", command=resoudre)
    bouton_resoudre.pack()

    root.mainloop()

# Exemple d'utilisation
grille_initiale = random_grid()
configurations = solve_Astar(grille_initiale, good_grid())

resoudre_taquin(grille_initiale, configurations)
