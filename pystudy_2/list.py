#list1=["w", "a", "s", "n"]
#print(list1[0]+list1[1], list1[2]+list1[1]+list1[3]+list1[2])
list1=["0", "3"]
del list1[1]
list1.remove("0")
list1.append("w")
list1.append("e")
list1.insert(1,"a")
list1.remove("e")
list1.append("1")
list1.pop()
list1.append("s")
list1.append("n")


print(list1[0]+list1[1], list1[2]+list1[1]+list1[3]+list1[2])

print(list1[1:3])
print(list1[:3])
print(list1[1:])