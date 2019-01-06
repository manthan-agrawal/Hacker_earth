y = int(input())

for x in range(2, y+1):
    a=0
    for no in range(2, int(x/2+1)):

        abc = x % no
        if abc == 0:
            a = 1
    if a==0:
        print(x, end=" ")


def manthan():
    print("manthan")
