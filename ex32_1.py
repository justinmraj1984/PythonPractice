import copy

# Input 2D Matrix and Print it
x = int(input("Enter value for X: "))
y = int(input("Enter value for Y: "))
xlist = []
ylist = []

if (x==1 or y==1):
  print("Input values must be >=2")
else:
  # Input values for 2D Matrix
  for j in range(0,y):
    for i in range(0,x):
      xval = input(f"Enter [{j+1}][{i+1}]: ")
      xlist.append(xval)
    # ylist.append(xlist) --> Appends a pointer of xlist into ylist. So when xlist changes in next iteration, it changes the previous data appended into ylist
    ylist.append(copy.deepcopy(xlist)) # deepcopy will copy the values instead of pointer
    xlist.clear()

  # Print the Matrix
  print("\n2D Matrix:")
  for xlist in ylist:
    for x in xlist:
      print(x, end=" ")
    print()