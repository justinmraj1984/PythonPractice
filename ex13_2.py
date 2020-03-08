# Combine argv and input
from sys import argv

# Get the name of the value to be received from user as argument
script, var1 = argv
# Prompt Input for the variable
var2 = input(f"Enter {var1} : ")
# Print the Variable and its Value
print(f"{var1} value is {var2}")