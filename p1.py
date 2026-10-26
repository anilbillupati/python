from typing import List


msg1,msg2="World","Hello"  

msg3,msg4,msg5 ="Anil","Kumar","Billupati" 

msg1,msg2=msg2,msg1

print (msg1,msg2)

print (int(10.4567899))

# anil="Anil Kumar Billupati"
# print(int(anil))

var = None 

print(type(var))

print (13/2)  # this will gives quotient in float    

print(13//2)  # quotient in integer 

print(13%2)   # gives us the remainder in the division 


a,b,c,d=False,False,True,True

print(a or b or c or d)


#  writing the program to print multiples of 10 


# i=0
# while i<10:
#     print(i*10)
#     i+=1

# for i in range(-10,10,2):
#     print(i)

# print (*range(0,100,2))

for i in reversed(range(20,10,-3)):
    print(i)


for i in range(1,4):
    print(i)
    for j in range(1,4):
        pass
        print(i,j)

def longer_string(name:str,name2:str)->str:
    if len(name)>=len(name2):
        return name
    else:
        return name2
    
print(longer_string("AnilB","Kumar"))


surname="Billupati"

print(surname[len(surname)-1])

for i in range (len(surname)):
    print(surname[i])
    
my_list=[1,2,3,4,5,2,3,4,1,2,3,4,5,6,1,3,4,565,6] 

def count_occurrence(mylist:List[int],target)->int:
    count=0
    for i in  mylist:
        if i == target:
            count +=1
    return count

my_list.append(3)
print("count of occurances is " ,count_occurrence( my_list,3))

tupleprac=(1,2,"Smil")

for ele in tupleprac:
    print(ele)

my_tuple =(12,34,56,6,87,78,6,43,14)
print(my_tuple.count(56))

  