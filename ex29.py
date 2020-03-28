from sys import argv

script, people, cats = argv
# cats = int(cats)
print(f"Inputs : {people} - {cats}")

if (people == cats):
  print("People and Cats count are equal")
if (people > cats):
  print("People count is greater than cats")
if (people < cats):
  print("People count is lesser than cats")
