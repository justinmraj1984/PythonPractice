from sys import argv
from os.path import exists

# Input from and to file names as Argument Values
script, from_file, to_file = argv
rootpath = "./files/"
from_file = rootpath + from_file
to_file = rootpath + to_file

print(f"from_file : {from_file} : exists - {exists(from_file)}")
print(f"to_file   : {to_file} : exists - {exists(to_file)}")

source_file = open(from_file)
source_data = source_file.read()
print(f"from_file : '{from_file}' : size - {len(source_data)} bytes")

target_file = open(to_file, "w+")
target_file.write(source_data)

print("File copied successfully!")
target_file.close()
source_file.close()
