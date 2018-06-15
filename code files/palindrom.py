q = input()
z= len(q)

for a in range(int(z/2)):
    a = 0
    if q[a] == q[z-1]:
        a=1

if a!=0:
    print("YES")
else :
    print ("NO")
    