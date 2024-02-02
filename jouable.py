from random import *
import pygame

SIZE = 3 
taquin = [0,1,2,3,4,5,6,7,8]
shuffle(taquin)

def print_taquin(taquin) :
    for k in range(0, SIZE*SIZE) :
        if (k % SIZE == 0) :
            print("\n")
        print(taquin[k], end=" ")
        
def string_taquin(taquin) :
    s = ""
    for k in range(0, SIZE*SIZE) :
        if (k % SIZE == 0) :
            s += "\n"
        s += str(taquin[k])
    s += " "
    return s

print_taquin(taquin)

#tableau des cases échangeables 
def moveable_right(t) :
    mov = []
    for i in range(len(t)) :
        if i%SIZE != SIZE - 1 :
            mov.append(t[i])
    return mov

def moveable_left(t) :
    mov = []
    for i in range(len(t)) :
        if i%SIZE != 0 :
            mov.append(t[i])
    return mov

def moveable_down(t) :
    mov = []
    for i in range(len(t) - SIZE) :
        mov.append(t[i])
    return mov

def moveable_up(t) :
    mov = []
    for i in range(SIZE, len(t)) :
        mov.append(t[i])
    return mov

#fonction qui échange deux cases si commande utilisateur
def vide(t) :
    for i in range(len(t)) :
        if t[i] == 0 :
            return i
        
def up(t) :
    i0 = vide(t)
    if 0 in moveable_down(t) :
        j = i0 + SIZE
        t[i0] = t[j]
        t[j] = 0
    return t 

def down(t) :
    i0 = vide(t)
    if 0 in moveable_up(t) :
        j = i0 - SIZE
        t[i0] = t[j]
        t[j] = 0
    return t 

def right(t) :
    i0 = vide(t)
    if 0 in moveable_left(t) :
        j = i0 - 1
        t[i0] = t[j]
        t[j] = 0
    return t 

def left(t) :
    i0 = vide(t)
    if 0 in moveable_right(t) :
        j = i0 + 1
        t[i0] = t[j]
        t[j] = 0
    return t 

def graphicplate(t, screen):
        font = pygame.font.Font(None, 100)
        color = (40,58,82)
        for y in range(SIZE):
            for x in range(SIZE):
                if t[x + y*SIZE] != 0:
                    pygame.draw.rect(screen, color, pygame.Rect(16+x*146, 16+y*146, 142, 142), border_radius=20)
                    screen.blit( font.render(str(t[x + y*SIZE]),1 ,(255,255,255)) , (70 + 144*x , 58 + 144*y) )
                    
#fonction de jeu
def play() :
    t = taquin #a remplacer par rendu de la fonction random taquin quand elle existera
    running = True
    white = (255, 255, 255)
    blue = (0, 0, 128)
    green = (9,44,28)
    marroon = (66,42,100)
    marroon_light = (200,200,240)
    pygame.init()
    display_surface = pygame.display.set_mode((600, 600))
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(string_taquin(t), True, blue, white)
    textRect = text.get_rect()
    textRect.center = (300, 300)
    while running :
       # display_surface.fill(white)
       # display_surface.blit(text, textRect)
       # display_surface.fill( green )
        pygame.draw.rect(display_surface, marroon, pygame.Rect(10, 10, 585, 585))
        pygame.draw.rect(display_surface, marroon_light, pygame.Rect(16, 16, 584, 584))
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        t = up(t)
                    elif event.key == pygame.K_DOWN:
                        t = down(t)
                    elif event.key == pygame.K_LEFT:
                        t = left(t)                        
                    elif event.key == pygame.K_RIGHT:
                        t = right(t)
                    elif event.key == pygame.K_q:
                        running = False
                #text = font.render(string_taquin(t), True, blue, white)
        if t == [1,2,3,4,0,5,6,7,8] :
            running = False
            import tkinter as tk
            fenetre = tk.Tk()
            photo = tk.PhotoImage(file='balkany.jpg')
            label = tk.Label(fenetre, image=photo)
            label.pack()
             
            fenetre.mainloop()
        graphicplate(t, display_surface)
        pygame.display.update()

    pygame.quit()
