def uniques(elements):
    uniques = dict(())
    for elem in elements:
        if(elem not in uniques.keys()):
            uniques[elem] = 0
    return uniques.keys()
nums = list(map(int, input().split()))
print(uniques(nums))