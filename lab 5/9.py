import re
txt = str(input())

x = re.sub(r"(\w)([A-Z])", r"\1 \2", txt)

print(x)