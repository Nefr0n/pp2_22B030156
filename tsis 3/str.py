from itertools import permutations

def all_permutations(s):

    char_list = [s[i] for i in range(0, len(s))]

    char_list.sort()

    prms = permutations(char_list)

    for permutation in prms:

        print(permutation)

a = input("Write the word: ")
all_permutations(a)