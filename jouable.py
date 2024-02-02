from random import *
import pygame
from Dijkstra import solve_Astar, good_grid, random_grid, is_solvable
import time
import tkinter as tk

SIZE = 3 
taquin = random_grid()
while not is_solvable(taquin) :
    taquin = random_grid()


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
                    pygame.draw.rect(screen, color, pygame.Rect(20+x*185, 20+y*185, 180, 180), border_radius=20)
                    screen.blit( font.render(str(t[x + y*SIZE]),1 ,(255,255,255)) , (90 + 183*x , 74 + 183*y) )

def play_sound(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_sound():
    pygame.mixer.music.stop()



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
    play_sound("tetris.mp3")
    def display_victory_image():
        victory_image = pygame.image.load("balkabravo.png")  # Ajoutez le chemin complet si nécessaire
        new_width, new_height = 600, 600
        resized_victory_image = pygame.transform.scale(victory_image, (new_width, new_height))

        image_width, image_height = resized_victory_image.get_size()
        x_coordinate = (600 - image_width) // 4
        y_coordinate = (600 - image_height) // 4
        display_surface.blit(resized_victory_image, (x_coordinate, y_coordinate))        
        pygame.display.update()
    while running :
       # display_surface.fill(white)
       # display_surface.blit(text, textRect)
       # display_surface.fill( green )
        pygame.draw.rect(display_surface, marroon, pygame.Rect(10, 10, 585, 585))
        pygame.draw.rect(display_surface, marroon_light, pygame.Rect(0, 0, 600, 600))
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
                    elif event.key == pygame.K_s:
                        configurations = solve_Astar(t, good_grid())
                        print(configurations)
                        for t_ in configurations :
                            t = t_
                            pygame.init()
                            pygame.draw.rect(display_surface, (141, 104, 147), pygame.Rect(0, 0, 600, 600))
                            graphicplate(t, display_surface)
                            pygame.display.update()
                            time.sleep(0.5)
                #text = font.render(string_taquin(t), True, blue, white)
        if t == [0,1,2,3,4,5,6,7,8] :
            stop_sound()
            play_sound("balkany oui.mp3")
            pygame.draw.rect(display_surface, (141, 104, 147), pygame.Rect(0, 0, 600, 600))
            display_victory_image()
            time.sleep(2000)
            running=False

        graphicplate(t, display_surface)
        pygame.display.update()

    pygame.quit()
