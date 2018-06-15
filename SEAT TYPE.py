y = int(input())

for x in range(y):
    seat = int(input())
    z = seat % 12
    if z == 0:
        print(seat-11, "WS")
    elif z == 1:
        print(seat+11, "WS")
    elif z == 2:
        print(seat+9, "MS")
    elif z == 3:
        print(seat+7, "AS")
    elif z == 4:
        print(seat+5, "AS")
    elif z == 5:
        print(seat+3, "MS")
    elif z == 6:
        print(seat+1, "WS")
    elif z == 7:
        print(seat-1, "WS")
    elif z == 8:
        print(seat-3, "MS")
    elif z == 9:
        print(seat-5, "AS")
    elif z == 10:
        print(seat-7, "AS")
    elif z == 11:
        print(seat-9, "WS")











