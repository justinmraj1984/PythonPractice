from sys import argv

def print_all(f):
  print("~" * 43)
  print(f"~~~ Filename : {in_file.name} ~~~")
  print("~" * 43)
  print(f.read())
  print("~" * 43)

def rewind(f):
  f.seek(0)

def print_a_line(f):
  print(f.readline())

script, in_file = argv
rootpath = "./files/"
in_file = open(rootpath + in_file) # File object

print("1. Read file first time")
print_all(in_file)

print("2. Read file second time using the same file object")
print_all(in_file) # does not return the file content as the pointer will now be at EOF

print("3. Reset the file pointer to Start of File using 'seek' function ")
rewind(in_file)

print("4. Read the file line by line")
print_a_line(in_file)
print_a_line(in_file)
print_a_line(in_file)