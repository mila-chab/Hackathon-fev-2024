
SIZE = 3

def new_grid() :
    return list(range(SIZE*SIZE))

def print_taquin(taquin) :
    end = len(str(SIZE*SIZE-1))
    for k in range(0, SIZE*SIZE) :
        if (k % SIZE == 0) :
            print("\n")
        long = len(str(taquin[k]))
        print(taquin[k], end=" "*(end-long + 1))

taquin = new_grid  
print_taquin(taquin)


