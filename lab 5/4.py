import re

txt = str(input())

x = re.search("[A-Z]{1}[a-z]{1,}", txt)

print(x)