# Copying binary files
# Error : reading the binary files in ASCII mode will
#         throw exception - UnicodeDecodeError: 'charmap' codec can't decode byte 0x81
# Solution : Use the file modes - rb+ and wb+ to read & write binary content
#            This works for ASCII text file content as well

from sys import argv
from os.path import exists

# Input from and to file names as Argument Values
script, from_file, to_file = argv
rootpath = "./files/"

target_file = open(rootpath + to_file, "wb+")
target_file.write(open(rootpath + from_file, "rb+").read())

print("File copied successfully!")
target_file.close()