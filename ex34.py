# 1. Accessing elements in a list - cardinal / ordinal reference
animals = ['tiger','lion','sheep','wolf','camel','goat','giraffe','rat','cat']

# print all elements in a list
for animal in animals:
  print(animal)

# access an element in a list
print('Animal at 1 : ', animals[0]) # cardinal number reference
print('The third animal : ', animals[2]) # ordinal number reference
print('The first animal : ', animals[0])
print('Animal at 3 : ', animals[2])
print('The fifth animal : ', animals[4])
print('Animal at 2 : ', animals[1])
print('The sixth animal : ', animals[5])
print('Animal at 4 : ', animals[3])


# 2. Exceptions while processing a list
# 2.1. IndexError: list index out of range
mylist = []
# print(mylist[0]) - throws IndexError
# Exception Handling
# OPTION 1: if not(mylist):
mylist = ['']
if not(mylist):
  print(mylist[0])
else:
  print("Option #1 : Empty list cannot be processed")

# OPTION 2: if len(mylist) > 0:
mylist = []
if len(mylist) > 0:
  print(mylist[0])
else:
  print("Option #2 : Empty list cannot be processed")
