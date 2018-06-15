def prime_no(x):
    a = 0
    for i in range(2, int(x / 2) + 1):
        y = x % i
        if y == 0:
            a = 1
    if a == 0:
        return (x)

abc = int(input())

for asdsd in range(abc):
    aaaaa= input()
    z = input()
    for a in z:
            for c in range(1, 20):
                m = ord(a) + c
                if m == prime_no(m):
                    yx = m
                    break
            for c in range(1, 20):
                n = ord(a) - c
                if n == prime_no(n):
                    we = n
                    break
            if ord(a) > 119 :
                print("q",end="")
            elif ord(a) < 67 :
                print("C",end="")
            elif ord(a)>90 and ord(a)<94 :
                print("Y",end="")
            elif ord(a)>93 and ord(a)<97 :
                print("a",end="")
            elif ord(a) == prime_no(ord(a)):
                print(a, end="")
            elif (ord(a) - we) == (yx - ord(a)):
                print(chr(we), end="")
            elif (ord(a) - we) > (yx - ord(a)):
                print(chr(yx), end="")
            elif (ord(a) - we) < (yx - ord(a)):
                print(chr(we), end="")

    print("")
