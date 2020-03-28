num = int(input("Enter num: "))

if (num > 0):
  i = 0
  numlist = []
  while (i < num+1):
    numlist.append(i)
    i = i+1
  print(numlist)

else:
  print("Invalid input.. Please enter a number > 0")
