
def solve(numheads, numlegs):
	ns = "Inputs are not valid"
	for i in range(numheads + 1):
		j = numheads - i
		if 2*i + 4*j == numlegs:
			return i, j
	return ns, ns

numheads = 35
numlegs = 94
x = solve(numheads, numlegs)
print(x)
