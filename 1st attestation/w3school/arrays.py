cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(cars)
print("x")
#arr[index] get the value of array item
cars[0] = "Toyota"
#arr[index] = smth can change the item 
e = len(cars)
print(e)
#len(arr) shows the number of items
for x in cars:
  print(x)
#prints items in array
cars.append("Honda")
print(cars)
#adds an item to array
cars.pop(2)
print(cars)
#arr.pop(index) can delete an item in array
cars.remove("Volvo")
print(cars)
#arr.remove("smth") can also delete an item

