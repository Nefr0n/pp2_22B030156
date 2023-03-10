n = int(input())
gap = []

def EvG(n):
    i = 0
    while i <= n:
        if i%2==0:
            yield i
        i += 1

for i in EvG(n):
    gap.append(str(i))

print(",".join(gap))