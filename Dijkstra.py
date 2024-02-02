from queue import PriorityQueue
import copy


SIZE = 5

def new_grid() :
    return list(range(SIZE*SIZE))

def print_taquin(taquin) :
    end = len(str(SIZE*SIZE-1))
    for k in range(0, SIZE*SIZE) :
        if (k % SIZE == 0) :
            print("\n")
        long = len(str(taquin[k]))
        print(taquin[k], end=" "*(end-long + 1))
        

def neighbours(taquin) :
    """
    Donne la liste des voisins d'un jeu de taquin dans le graphe des jeux
    """
    voisins = [] # Liste de taquins
    # trouver le 0
    k = 0
    while (taquin[k] != 0) :
        k += 1
    q, r = k // SIZE, k % SIZE
    # Determination des nouvelles pos
    # Mouvement horizontal
    for droite_gauche in [-1, 1]:
        if (droite_gauche == -1 and r > 0) or (droite_gauche == 1 and r < SIZE - 1) :
            # Possibilite de bouger
            new_r = r + droite_gauche
            while not ((droite_gauche == -1 and new_r < 0) or (droite_gauche == 1 and new_r > SIZE - 1)) :
                # Ajout de la position : on fait glisser de new_r a r
                new_taquin = copy.deepcopy(taquin)
                r_act = new_r
                new_taquin[SIZE*q + new_r] = 0
                while r_act != r :
                    r_act -= droite_gauche
                    new_taquin[SIZE*q + r_act] = taquin[SIZE*q + r_act + droite_gauche]
                voisins.append(new_taquin)
                new_r += droite_gauche
    # Mouvement vertical
    for haut_bas in [-1, 1]:
        if (haut_bas == -1 and q > 0) or (haut_bas == 1 and q < SIZE - 1) :
            # Possibilite de bouger
            new_q = q + haut_bas
            while not ((haut_bas == -1 and new_q < 0) or (haut_bas == 1 and new_q > SIZE - 1)) :
                # Ajout de la position : on fait glisser de new_r a r
                new_taquin = copy.deepcopy(taquin)
                q_act = new_q
                new_taquin[SIZE*new_q + r] = 0
                while q_act != q :
                    q_act -= haut_bas
                    new_taquin[SIZE*q_act + r] = taquin[SIZE*(q_act + haut_bas) + r]
                voisins.append(new_taquin)
                new_q += haut_bas
    return voisins


################################
#                              #
#             TESTS            #
#                              #
################################

taquin = [7, 1, 2, 3, 4, 5, 6, 0, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
print_taquin(taquin)
voisins = neighbours(taquin)
for voisin in voisins :
    print("\n------------------")
    print_taquin(voisin)
    