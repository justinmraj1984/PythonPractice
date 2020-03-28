from sys import argv

print("Enter an option:")
print("[1] .. Turn RIGHT")
print("[2] .. Turn LEFT")
option = input("> ")

if (option == "1"):
  print("You have turned RIGHT")
elif (option == "2"):
  print("You have turned LEFT")
else:
  print("Invalid option")
