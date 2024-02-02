
SIZE = 3

taquin = [0,1,2,3,4,5,6,7,8]

def print_taquin(taquin) :
    for k in range(0, SIZE*SIZE) :
        if (k % SIZE == 0) :
            print("\n")
        print(taquin[k], end=" ")
        
print_taquin(taquin)


