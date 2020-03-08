from sys import argv

script, filename = argv
rootpath = "./files/"
filecontent = open(rootpath + filename)

print(f"""
~~~ Content of "{rootpath + filename}" ~~~
{filecontent.read()}
~~~ End of File ~~~
""")