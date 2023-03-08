import os

print('Exist:', os.access(r"C:\Users\Darling\Desktop\New_folder\example", os.F_OK))

print('Readable:', os.access(r"C:\Users\Darling\Desktop\New_folder\example", os.R_OK))

print('Writable:', os.access(r"C:\Users\Darling\Desktop\New_folder\example", os.W_OK))

print('Executable:', os.access(r"C:\Users\Darling\Desktop\New_folder\example", os.X_OK))