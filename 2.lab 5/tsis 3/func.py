def histogram(values):
    curr = '*'
    for val in values:
        if val != 0:
            curr = curr * val
        else:
            curr = ''
        print(curr)
        curr = '*'
