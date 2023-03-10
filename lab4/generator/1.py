n = int(input())
def printValues(n):
    l = list()
    for i in range(1, n + 1):
        l.append(i**2)
    print(l)
        
printValues(n)