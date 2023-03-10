nl=[]
n = int(input())
def printValues(n):
    for i in range(0, n + 1):
        if (i%3==0) and (i%4==0):
            nl.append(i)
    print(nl)

printValues(n)