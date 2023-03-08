import os
fname = str(input("Please write right name of a file: "))
def path_length(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i 

print("Number of lines in the file: ", path_length(fname))