from queue import PriorityQueue
import copy
import random

SIZE = 4

def good_grid() :
    return list(range(SIZE*SIZE))

def random_grid() :
    grid = good_grid()
    random.shuffle(grid)
    return grid

def print_taquin(taquin) :
    end = len(str(SIZE*SIZE-1))
    for k in range(0, SIZE*SIZE) :
        if (k % SIZE == 0) :
            print("\n")
        long = len(str(taquin[k]))
        print(taquin[k], end=" "*(end-long + 1))
    print("\n------------")
        

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

def dijkstra(taquin) :
    """
    Donne la distance de taquin a la solution, avec les differentes etapes
    """
    d = dict() # Donne les distances aux differents noeuds
    previous = dict() # Precedents noeuds dans le chemin optimal
    pq = PriorityQueue()
    # initialisation
    d[tuple(taquin)] = 0
    pq.put((0, taquin)) # On enfile le noeud actuel a la priorite 0
    while not pq.empty() :
        distance_actuelle, noeud_actuel = pq.get() # Tant que c'est non vide on defile celui a la plus petite priorite
        noeud_voisins = neighbours(noeud_actuel)
        for noeud_voisin in noeud_voisins :
            # Pour chaque voisin 
            tentative_distance = distance_actuelle + 1 
            voisin_tuple = tuple(noeud_voisin)
            if voisin_tuple in d :
                if tentative_distance < d[voisin_tuple] :
                    d[voisin_tuple] = tentative_distance
                    previous[voisin_tuple] = noeud_actuel 
                    pq.put((tentative_distance, noeud_voisin))
            else :
                d[voisin_tuple] = tentative_distance
                previous[voisin_tuple] = noeud_actuel 
                pq.put((tentative_distance, noeud_voisin))
    return d, previous

def dijkstra_target(taquin, target) :
    """
    Donne la distance de taquin a la solution, avec les differentes etapes
    """
    d = dict() # Donne les distances aux differents noeuds
    previous = dict() # Precedents noeuds dans le chemin optimal
    pq = PriorityQueue()
    # initialisation
    d[tuple(taquin)] = 0
    pq.put((0, taquin)) # On enfile le noeud actuel a la priorite 0
    while not pq.empty() :
        distance_actuelle, noeud_actuel = pq.get() # Tant que c'est non vide on defile celui a la plus petite priorite
        if noeud_actuel == target :
            return d, previous
        noeud_voisins = neighbours(noeud_actuel)
        for noeud_voisin in noeud_voisins :
            # Pour chaque voisin 
            tentative_distance = distance_actuelle + 1 
            voisin_tuple = tuple(noeud_voisin)
            if voisin_tuple in d :
                if tentative_distance < d[voisin_tuple] :
                    d[voisin_tuple] = tentative_distance
                    previous[voisin_tuple] = noeud_actuel 
                    pq.put((tentative_distance, noeud_voisin))
            else :
                d[voisin_tuple] = tentative_distance
                previous[voisin_tuple] = noeud_actuel 
                pq.put((tentative_distance, noeud_voisin))
    return d, previous

def reconstruct_path(previous, start, end) :
    path = []
    current = tuple(end)  # Assurez-vous que le format est un tuple
    while current in previous:
        path.append(list(current))  # Convertissez en liste uniquement pour l'ajout à la liste path
        current = tuple(previous[current])  # Assurez-vous que le format est un tuple
    path.append(list(start))
    return list(reversed(path))

def is_solvable(taquin) :
    """
    Dit si une configuration du jeu admet une solution 
    """
    new_taquin = copy.deepcopy(taquin)
    o_index = new_taquin.index(0)
    q, r = o_index // SIZE, o_index % SIZE
    parite_0 = q + r
    nb_permut = 0
    for k in range(0, SIZE*SIZE) :
        k_index = new_taquin.index(k)
        if k_index != k :
            new_taquin[k], new_taquin[k_index] = new_taquin[k_index], new_taquin[k]
            nb_permut += 1
    return nb_permut % 2 == parite_0 % 2  

# Heuristique
def manhattan(taquin, index) :
    k = taquin[index] # case en position index
    return abs(k//SIZE - index//SIZE) + abs(k%SIZE + index%SIZE)
    # Distance de manhattan entre la case en index et la position ou elle devrait etre

def heuristique(taquin) :
    """
    Doit verifier heuristique(taquin) <= vrai_distance(taquin) pour tout taquin 
    """
    n = SIZE*SIZE
    return sum([manhattan(taquin, k) for k in range(0, n)])

def solve_Astar(taquin, target) :
    """
    Retourne les differentes etapes pour resoudre le jeu de taquin, quand cela est possible
    """
    d = dict() # Donne les distances aux differents noeuds
    previous = dict() # Precedents noeuds dans le chemin optimal
    pq = PriorityQueue()
    # initialisation
    d[tuple(taquin)] = 0
    pq.put((0, taquin)) # On enfile le noeud actuel a la priorite 0
    while not pq.empty() :
        distance_actuelle, noeud_actuel = pq.get() # Tant que c'est non vide on defile celui a la plus petite priorite
        if noeud_actuel == target :
            return reconstruct_path(previous, taquin, target)
        
        noeud_voisins = neighbours(noeud_actuel)
        for noeud_voisin in noeud_voisins :
            # Pour chaque voisin 
            tentative_distance = distance_actuelle + 1 
            voisin_tuple = tuple(noeud_voisin)
            if voisin_tuple in d :
                if tentative_distance < d[voisin_tuple] :
                    d[voisin_tuple] = tentative_distance
                    previous[voisin_tuple] = noeud_actuel 
                    pq.put((tentative_distance + heuristique(noeud_voisin), noeud_voisin))
            else :
                d[voisin_tuple] = tentative_distance
                previous[voisin_tuple] = noeud_actuel 
                pq.put((tentative_distance, noeud_voisin))
    return []

################################
#                              #
#             TESTS            #
#                              #
################################

#Test Astar
taquin = random_grid()
print_taquin(taquin)
if is_solvable(taquin) :
    print("C'est solvable.")
    path = solve_Astar(taquin, good_grid())
    for grid in path :
        print_taquin(grid)
else :
    print("Non solvable !")


"""Test dijkstra
taquin = random_grid()
print_taquin(taquin)
if is_solvable(taquin) :
    print("C'est solvable.")
    d, previous = dijkstra_target(taquin, good_grid())
    path = reconstruct_path(previous, taquin, good_grid())
    for grid in path :
        print_taquin(grid)
else :
    print("Non solvable !")
"""
