mytuple = ("apple", "banana", "cherry")
print(mytuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#tuples allow to duplicate values
print(len(thistuple))
#len(tuple) number of items in tuple

thistuple1 = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple1 = ("apple")
print(type(thistuple))
#to create an one item tuple you have to add comma
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple1 = ("abc", 34, True, 40, "male")
#tuple can contain any types even in one tuple
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#type(tuple) can show the type of item
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
#tuple((smth)) makes it tuple