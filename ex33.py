num = 0
isNum = False

try:
  num = int(input("Enter num: "))
  isNum = True
except Exception as ex:
  print("Invalid input.. Please enter a number > 0")
  print("Exception: ", ex)

if (isNum):
  i = 0
  numlist = []
  while (i < num+1):
    numlist.append(i)
    i = i+1
  print(numlist)

else:
  print("Aborted...")
