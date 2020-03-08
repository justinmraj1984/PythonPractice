def add(a,b):
  sum = a+b
  print(f"Sum of {a} & {b} : {sum}")
  return sum

def subtract(a,b):
  difference = a-b
  print(f"Difference of {a} & {b} : {difference}")
  return difference

def multiply(a,b):
  product = a*b
  print(f"Product of {a} & {b} : {product}")
  return product

def divide(a,b):
  division = a/b
  print(f"{a} divided by {b} : {division}")
  return division

def modulus(a,b):
  reminder = a%b
  print(f"Reminder of {a} mod {b} : {reminder}")
  return reminder

add(10, 20)
subtract(20, 10)
multiply(10, 20)
divide(20, 10)
modulus(50, 15)