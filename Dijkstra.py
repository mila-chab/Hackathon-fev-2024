from queue import PriorityQueue

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
    # trouver le 0
    k = 0
    while (taquin[k] != 0) :
        k += 1
    q, r = k / SIZE, k % SIZE



################################
#                              #
#             TESTS            #
#                              #
################################

taquin = new_grid()
print_taquin(taquin)