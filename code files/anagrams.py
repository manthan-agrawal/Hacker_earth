a = input()
string1 = raw_input()
string2 = raw_input()
list1_len = len(string1)
list2_len = len(string2)

list1 = []
list2 = []
list3 = []
for man in range(list1_len):
    list1.append(string1[man])
for an in range(list2_len):
    list2.append(string2[an])

arbitary= list2_len

for list1_for in range(list1_len):
    for list2_for in range(arbitary):
        if list1[list1_for] == list2[list2_for]:
            list3.append(list2[list2_for])
            del list1[list1_for]
            del list2[list2_for]
            arbitary= list2_len -1



new_length1 = len(list1)
new_length2 = len(list2)
x = len(list3)
w = (new_length1+new_length2)-(2*x)
print(w)




print("hello")

