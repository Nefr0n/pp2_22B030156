import re

name = str(input"please write camel case: ")
name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
print(name)