# reducing lines in ex17.py
from sys import argv
from os.path import exists

# Input from and to file names as Argument Values
script, from_file, to_file = argv
rootpath = "./files/"

target_file = open(rootpath + to_file, "w+")
target_file.write(open(rootpath + from_file).read())

print("File copied successfully!")
target_file.close()