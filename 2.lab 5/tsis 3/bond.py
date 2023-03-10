def spy_game(nums):
    Bond = False
    for i in range(2, len(nums)):
        agent = nums[i-2] * 100 + nums[i-1] * 10 + nums[i]
        if agent == 7:
            Bond = True
            break
    return Bond
nums = list(map(int, input().split()))
print(spy_game(nums))