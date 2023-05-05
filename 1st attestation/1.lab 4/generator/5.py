n = int(input())

def rev(n):
    while n >= 0:
        yield n
        n -= 1

for i in rev(n):
    print(i)