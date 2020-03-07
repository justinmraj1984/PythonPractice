f_string = '{} {} {} {}'

# substitute value of any data-type to the f-string
print(f_string.format(1, 2, 3, 4))
print(f_string.format('One', 'Two', 'Three', 'Four'))
print(f_string.format(True, False, False, True))
print(f_string.format(f_string, f_string, f_string, f_string))

# print(f_string.format('My Text', 'Value is', 'Incomplete'))
# above print statement gives error - "IndexError: Replacement index 3 out of range for positional args tuple"

print(f_string.format('My Text', 'Value is', 'Incomplete -', True))
