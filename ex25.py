def add(a,b):
  """
  Addition of 2 numbers
  """
  sum = a+b
  print(f"Sum of {a} & {b} : {sum}")
  return sum

def subtract(a,b):
  """
  Subtraction of 2 numbers
  """
  difference = a-b
  print(f"Difference of {a} & {b} : {difference}")
  return difference

def multiply(a,b):
  """
  Product of 2 numbers
  """
  product = a*b
  print(f"Product of {a} & {b} : {product}")
  return product

def divide(a,b):
  """
  Division of 2 numbers
  """
  division = a/b
  print(f"{a} divided by {b} : {division}")
  return division

def modulus(a,b):
  """
  Modulus of 2 numbers
  """
  reminder = a%b
  print(f"Reminder of {a} mod {b} : {reminder}")
  return reminder

"""
Execution steps:
In the python console, import this script as library and execute the functions

>>> import ex25
>>> help(ex25)
>>> add(10, 20)
>>> subtract(20, 10)
>>> multiply(10, 20)
>>> divide(20, 10)
>>> modulus(50, 15)
"""