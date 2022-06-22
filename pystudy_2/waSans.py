list2 = [87, 65, 83, 78]

list1 = []
for i in range(0,4):
    list1.append(0)
    for j in range(0,128):

        list1[i]=list1[i]+1
        if list1[i] == list2[i]:
            break


    list1[i]=chr(list1[i])



print(list1[0]+list1[1], list1[2]+list1[1]+list1[3]+list1[2])