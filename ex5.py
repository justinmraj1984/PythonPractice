my_name = "Janny Bravo"
my_age = 35
my_height = 74
my_weight = 80
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

# The formatted string inside print statement contains the variable to be printed
# f denotes formatted string
# variable enclosed within braces is substituted during run-time

print(f"My name is {my_name}")
print(f"I am {my_age} years old")
print(f"I am {my_height} inches tall")
print(f"My weight is {my_weight} kg")
print(f"I have got {my_eyes} eyes, {my_hair} hair and {my_teeth} teeth")

total = my_height + my_weight + my_age

# braces can be used to embed an expression within the format string
print(f"If I add {my_age}, {my_height} & {my_weight}, I get the sum - {my_height + my_weight + my_age}")