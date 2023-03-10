nums = [int(x) for x in input().split()]

product = 1
for num in nums:
    product *= num
print(product)