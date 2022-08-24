
def printHelloWorld(n=3):
    print("Hello World!!" * n)
    return


def printAdd(a, b):
    print(a + b)
    return
    print("응 없어")


def add(a, b):
    return a + b


def printWithComma(*b):
    print(b)


printHelloWorld()
printHelloWorld(4)
printHelloWorld(n=5)
printAdd(1, 2)
print(add(1, 3))
printWithComma(1,2,3,4,2,4)