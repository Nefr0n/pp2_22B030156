import glob

dir_path = r'C:\Users\Darling\Desktop\New_folder\example\lab 6*\*.*'
for file in glob.glob(dir_path, recursive=True):
    print(file)