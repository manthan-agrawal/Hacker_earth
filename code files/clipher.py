string_A = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
string_a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
string_0 = ["0","1","2","3","4","5","6","7","8","9"]

xyz = input()
increament = int(input())
abc = []
for x in range(len(xyz)+1):
    if [ord(xyz[x]) >= 48 and ord(xyz[x]) <= 57] or [ord(xyz[x]) >= 65 and ord(xyz[x]) <= 90] or [ord(xyz[x]) >= 97 and ord(xyz[x]) <= 122]:
        print()

    else:
        print(xyz[x], end="")