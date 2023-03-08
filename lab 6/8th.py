import os
if os.path.exists("legend.txt"):
  os.remove("legend.txt")
else:
  print("The file does not exist")