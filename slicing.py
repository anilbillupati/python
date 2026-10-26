# slicing in python  is used to get the sub string from the string with in the range defined
# slicing format [start :end : step ]

str="Anil Kumar"
print(str[0:4]) # Anil
print(str[5:])  # Kumar
print(str[:4])  # Anil

print(str[6:])


# string formattting in python
name="Virat"
age=20
place="India"

print("My name is {} , I am {} years old and I live in {}".format(name,age,place))