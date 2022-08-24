def printHelloWorld(n=3):
    print("Hello World!!" * n)
    return


def printAdd(a, b):
    print(a + b)
    return
    print("응 없어")


def add(a, b):
    return a + b


def addList(*b):
    sum = 0
    for b in b:
        sum += b
    return sum


printHelloWorld()
printHelloWorld(4)
printHelloWorld(n=5)
printAdd(1, 2)
print(add(1, 3))
print(addList(1, 2, 3, 2, 4, 5, 2, 6))
