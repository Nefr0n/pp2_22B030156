import re

txt = str(input())

x = re.search('ab?', txt)

print(x)