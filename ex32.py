# Common function to print a list
def print_fruits(fruits):
  print("\nList of Fruits:")
  for fruit in fruits:
    print(fruit)

# 1. Printing a list
fruits = ["apple","banana","orange","pomegranate"]
print("1. List of Fruits:")
print_fruits(fruits)

# 2. Getting input to populate a list
print("\n2. Add Fruits to the list:")
no_of_fruits = int(input("How many fruits: "))
for i in range(0, no_of_fruits):
  fruit = input(f"Fruit# {i+1}: ")
  fruits.append(fruit)
print_fruits(fruits)
