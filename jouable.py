from random import *
from time import *
import pygame

SIZE = 3 
taquin = [0,1,2,3,4,5,6,7,8]

def print_taquin(taquin) :
    for k in range(0, SIZE*SIZE) :
        if (k % SIZE == 0) :
            print("\n")
        print(taquin[k], end=" ")

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
    for i in range(SIZE - 1, len(t)) :
        mov.append(t[i])
    return mov

def moveable_up(t) :
    mov = []
    for i in range(len(t) - SIZE) :
        mov.append(t[i])
    return mov

#fonction qui échange deux cases si commande utilisateur
def vide(t) :
    for i in range(len(t)) :
        if t[i] == 0 :
            return i
        
def up(t) :
    i0 = vide(t)
    if i0 in moveable_down(t) :
        j = i0 + SIZE
        t[i0] = t[j]
        t[j] = 0
    print_taquin(t) 

def down(t) :
    i0 = vide(t)
    if i0 in moveable_up(t) :
        j = i0 - SIZE
        t[i0] = t[j]
        t[j] = 0
    print_taquin(t) 

def right(t) :
    i0 = vide(t)
    if i0 in moveable_left(t) :
        j = i0 - 1
        t[i0] = t[j]
        t[j] = 0
    print_taquin(t) 

def left(t) :
    i0 = vide(t)
    if i0 in moveable_right(t) :
        j = i0 + 1
        t[i0] = t[j]
        t[j] = 0
    print_taquin(t) 

#fonction de jeu
def play() :
    t = taquin #a remplacer par rendu de la fonction random taquin quand elle existera
    print_taquin(taquin)
    running = True
    pygame.init()
    while running :
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        up(t)
                    elif event.key == pygame.K_DOWN:
                        down(t)
                    elif event.key == pygame.K_LEFT:
                        left(t)
                    elif event.key == pygame.K_RIGHT:
                        right(t)
                    elif event.key == pygame.K_q:
                        running = False
    pygame.quit()
