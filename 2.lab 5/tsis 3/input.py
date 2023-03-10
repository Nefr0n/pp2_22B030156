from math import sqrt
def filter_prime(nums):
    primes = []
    num_prime = True
    
    for num in nums:
        for i in range(2, int(sqrt(num))):
            if num % i == 0:
                num_prime = False
                break
        if num_prime is True:
            primes.append(num)
        num_prime = True
    return primes
nums = list(map(int, input().split()))
print(filter_prime(nums))