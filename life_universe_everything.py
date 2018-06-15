abc = []
for _ in range(1000000):

    x = int(input())

    if x !=42:
       abc.append(x)
    else :
        break

for q in range(len(abc)):
    print(abc[q])

