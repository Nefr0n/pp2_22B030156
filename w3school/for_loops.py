fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print("prints each item\n")

for x in "banana":
  print(x)
print("prints each letter\n")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print("list breaks after items equals banana\n")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
print("jumps over banana\n")

for x in range(6):
  print(x)
print("counts from 0 till this number\n")

for x in range(2, 6):
  print(x)
print("counts from a to b (a,b)\n")

for x in range(2, 30, 3):
  print(x)
print("counts from a to b with c steps(a,b,c)\n")

for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

print("break!\n")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
print("prints first last till the end and then countinuous\n")

