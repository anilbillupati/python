print("Hello Anil")
print(2+16)

#string printing "" quotes we use the \(Backslash)
print("Hello Anil Kumar,\"Billupati\"")

#printing the same string multiple times variable declaration is used here
message ="Anil"
print(message)
print(message)

#variables can be numbers,alphabets and underscore , but not start with number , not a keyword & not a space 

capital_city_of_India="New Delhi"
print(capital_city_of_India)

# data types in python

num=10
temp=32.34
is_true=False
str="Anil"
arr_list=[1,3,3,4,5,56,7,8]

print(num,temp,is_true,str,arr_list)

print(type(num))

# type casting

a=10.234
b=int(a)
print(b)   # output is 10  ;

# arithmetic operators + ,- ,*,/,//,%
#count +=count

# logical operators  or ,and ,not 

a=False
b=True
print(a or b)
print(a and b)
print(not b)

# Taking users input 

name =input("what is your name:?").strip().title()

##string methods 
# name.strip()
# name.capitalize()
# name.title()

print("hello", name)

"""
inside the print we have (* objects,sep=' ',end="\n")
this is the reason why we get the space and next line for the each print in python 
"""

x=int(input("what is the x value?") )
y=int(input("what is the y value?"))

print(x+y) # this results like the Strings addition but it should not work like that  

n=float(input("what is the value of n?"))
m=float(input("what is the value of m?"))

answer=round(n+m,3)

print(answer)


# comparision operators ==,>,<,>=,<= !=
def ableto_withdraw (x:float)->None:
     if(x==0):
          print("you have no money to withdraw")
     elif(x>0):
          print("You can withdraw your money")
     else:
          print("you can't withdraw money")

#loops to print 

i=3
while i!=0:
     print("Meow")
     i=i-1

#  print the arrays 

students= ["Anil","Kumar","Billupati"]

for i in  students:
     print(i)

# len is used to find the size of the list in python 

for i in range (len(students)):
     print(i+1,students[i])
 
# dictionary -> which is similar map in java used to store the data in key value pair 

students={
     "Anil":"Billupati",
     "Krishna":"Tirumuru",
     "Sunil" :"bheemishetty",
     "Gunji":"Abhiram"
}


for student in students:
     print(student,students[student])

str="Anil Kumar"
print(str[9])
print(str[len(str)-1])

