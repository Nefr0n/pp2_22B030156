n = 5
def printSquares(n):
    l = list()
    for i in range(n):
        l.append(i*i)
        yield i**2
    print(l)
printSquares(n)