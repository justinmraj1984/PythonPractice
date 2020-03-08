from sys import argv

prompt = "> "
script, username = argv

print(f""" 
Hi {username}! This is {script}.
I need few information to setup your profile.
""")

print("What is your Gender?")
gender = input(prompt)
print(f"What is your Age?")
age = input(prompt)
print(f"Which school did you study?")
school = input(prompt)
print(f"Where do you live?")
lives_in = input(prompt)

print(f""" 

------------------------
: User Profile Updates :
------------------------
Username : {username}
Age      : {age}
Gender   : {gender}
School   : {school}
Lives In : {lives_in}
------------------------
""")