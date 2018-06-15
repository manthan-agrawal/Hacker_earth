w = input()
L = int (w)
q = input()
N = int(q)
for _ in range(N):
    x = input()
    y = x.split()
    W =int( y[0])
    H = int(y[1])
    if W < L or H < L:
        print("UPLOAD ANOTHER")
    else :
        if W==H:
            print("ACCEPTED")

        else:
            print("CROP IT")