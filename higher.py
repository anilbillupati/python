def squre(num):
    return num*num


def  cube (num):
    return num * num *num 


def higher(num,operation):
    return operation(num)



print (higher(23,squre))
print (higher(23,cube))
