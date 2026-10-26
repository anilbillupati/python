my_dictionary={"anil":53,"kalyani":78}

print(my_dictionary)


print(my_dictionary["anil"])

my_dictionary["anil"]=56
print(my_dictionary["anil"])


str="anilkumarbillupati"

frequency_dict={}

for char in str:
    if char not in frequency_dict:
        frequency_dict[char] =1
    else:
        frequency_dict[char] +=1
print(frequency_dict)


listnumbers="anil.kalyani.anilkumar.billupati"
print(listnumbers.split("."))
try:
    answer=10/0
except:
    answer="cannot divide by zero"
print(answer)


try:
    answer=10/0
except Exception as nothing:
    print("error",nothing)