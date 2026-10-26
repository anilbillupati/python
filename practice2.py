
# import math

from math import sqrt

from array import array



value=81
result=int(sqrt(value))
print(result)


# in arrays we need to mention the unicode character in the python other wise it will be considered as the normal list 

'''
i is int
l is long
u character
f is float 
'''
arr = array('f',[])


for i in range(5):
        arr.append(float(input("enter the value:")))
print(arr)






