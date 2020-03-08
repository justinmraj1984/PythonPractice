#define one function to return results of all the arith operations
def arithmetic_operations(a,b):
  sums = a + b
  diff = a - b
  prod = a * b
  divi = a / b
  modu = a % b
  return sums, diff, prod, divi, modu

results = arithmetic_operations(10, 20) #all the return values are received in 'results' variable
print("""Arithmetic Operation Results:
Sum : {}
Difference : {}
Product : {}
Division : {}
Mod : {}
""".format(*results)); #using this format option, all the return values are substituted