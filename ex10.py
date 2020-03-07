# printing with escape characters within string

tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat"
fat_cat = """
I'll do a List:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""
super_cat = '''
I am the new fat-cat and I'll do a List:
\t* {}
\t* {}
\t* {}
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(super_cat.format("Cooking", "Fishing", "HouseKeeping"))

# ASCII bell
print("\a")