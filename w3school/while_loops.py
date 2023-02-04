i = 1
while i < 6:
  print(i)
  i += 1
print("#prints number till 5")
print(" ")

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

print("loop breaks when reach 3")
print(" ")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

  #jump over 4th operation

print("jumps over 4th operation")
print(" ")


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
print(" ")
print("plus 1 condition")

