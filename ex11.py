print('Input:')
print("Name :", end=' ')
name = input()
print("Age :", end=' ')
# age = input() # by default input is received as String. so any math operation (as in line no. 11) will return TypeError - "TypeError: can only concatenate str (not "int") to str"
age = int(input()) # converting input to Integer will recive the input as Integer value
print("Height :", end=' ')
height = input()

print('\nOutput:')
print('-'*50)
print(f"Name : {name}")
print(f"Age : {age}", end=' ==> ')
print(f'After 20 years you will be {age+20}')
print(f"Height : {height}")
print('-'*50)