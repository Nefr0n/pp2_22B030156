import re

txt = "Messi is the GOAT, and CR7 is the best athlete."

x = re.sub("[\s,.]", ":", txt)


print(x)