from sys import argv

# 1. Receive filename as argument 
script, filename = argv
rootpath = "./files/"

print(f"""We are going to overwrite the file - '{rootpath + filename}'.
Press [CTRL+C] to cancel or else Hit [RETURN] to continue...""")
input('?')

# 2. Open file in Read mode and Display existing file content
targetfile = open(rootpath + filename)
print(f"""
~~~ Content of '{rootpath + filename}' ~~~
{targetfile.read()}
~~~ End of File ~~~
""");

# 2. Open file in Write mode and Trucate it
targetfile = open(rootpath + filename, 'w+')
targetfile.truncate()
print(f"""File Truncated Successfully.\n
Input 3 lines to be written into this file...""")

# 3. Input new lines and write them into the file
line1 = input("Enter Line1 : ")
line2 = input("Enter Line2 : ")
line3 = input("Enter Line3 : ")

print(f"\nWriting new lines to the file - '{rootpath + filename}'.")
targetfile.write(f"""{line1}
{line2}
{line3}""")
# 4. Close the file after writing new lines into it
targetfile.close()

# 5. Open the file again in read mode to Display the updated content
targetfile = open(rootpath + filename)
print(f"""
Lines written successfully.
~~~ Content of '{rootpath + filename}' ~~~
{targetfile.read()}
~~~ End of File ~~~
""")
