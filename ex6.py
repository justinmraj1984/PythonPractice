type_of_people = 10
x = f"There are {type_of_people} types of people"

binary = "binary"
do_not = "don't"
y = f'Those who know {binary} and those who {do_not}'

print(x)
print(y)

# f-string within another f-string
print(f"I said : {x}")
print(f"I also said : {y}")

# embedding binary variables/values into f-string
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

left = "This is the left side of"
right = "a string with the right side"
print(left + right)

print(f"Are you really happy with programming? {1<2}")
