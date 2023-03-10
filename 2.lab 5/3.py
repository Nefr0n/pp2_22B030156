import re

txt = str(input())

x = re.search("[a-z]_" , txt)

print(x)