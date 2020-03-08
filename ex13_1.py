# 1. import argv from sys
from sys import argv

# 2. unpack the user input
# unpacking returns the command line arguments including the python-file-name
script, var1, var2, var3 = argv

# 3. print the variables
print(f"script executed : {script}")
print(f"user input 1 : {var1}")
print(f"user input 2 : {var2}")
print(f"user input 3 : {var3}")

# ValueError Exception:
# ValueError: not enough values to unpack - When less input is given than the variable count
# ValueError: too many values to unpack - When more input is given than the variable count