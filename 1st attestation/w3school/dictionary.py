thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#dictionaries wont allow duplicates, but ordered and changeables
print(thisdict["brand"])
#to reffer value pairs use the key name

mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(mydict)
#duplicate values will overwrite existing values
print(len(mydict))
#len(name) shows numbers of items
dict1 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
#dictionary can contain any types
dict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(dict2))
#from python perspective dictionaries are defined with type 'dict'
dict3 = dict(name = "John", age = 36, country = "Norway")
print(dict3)
#dict(smth) can constructor to dictionary
