from sys import argv

script, people, cars, trucks = argv
print(f"Inputs : {people} - {cars} - {trucks}")

if (cars >= trucks):
  if (people <= cars):
    print("More cars to choose. First come First serve !!")
  elif (people > cars):
    print("Prefer to choose truck or car pool")
elif (cars < trucks):
  if (people <= trucks):
    print("More trucks to choose")
  elif (people > trucks):
    print("Share the trucks to accomodate all people")
